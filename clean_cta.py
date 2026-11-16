import json
import os
import re

import pandas as pd
from shapely import wkt
from shapely.geometry import Point, shape

os.makedirs("cleaned", exist_ok=True)

LINE_COLS = {"RED": "red", "BLUE": "blue", "G": "green", "BRN": "brown",
             "P": "purple", "Y": "yellow", "Pnk": "pink", "O": "orange"}


def clean_name(s):
    return re.sub(r"\s+", " ", str(s)).strip().upper()


ca_geo = json.load(open("ext/chicago_community_areas.geojson"))
community_areas = []
for f in ca_geo["features"]:
    name = clean_name(f["properties"]["community"])
    if name == "OHARE":   # health file spells it O'HARE
        name = "O'HARE"
    community_areas.append({
        "community_area_num": int(f["properties"]["area_numbe"]),
        "community_area": name,
        "area_sq_mi": float(f["properties"]["shape_area"]) / 27_878_400,  # sq ft -> sq mi
        "geom": shape(f["geometry"]),
    })
ca_df = pd.DataFrame(community_areas)
assert len(ca_df) == 77

nb = pd.read_csv("neighborhood_boundaries.csv")
nb["geom"] = nb["the_geom"].apply(wkt.loads)
nb["neighborhood"] = nb["PRI_NEIGH"].apply(clean_name)
assert len(nb) == 98


def locate(lat, lon):
    p = Point(lon, lat)   # shapely uses (x=lon, y=lat)
    ca = ca_df[ca_df.geom.apply(lambda g: g.covers(p))]
    n = nb[nb.geom.apply(lambda g: g.covers(p))]
    return (int(ca.community_area_num.iloc[0]) if len(ca) else pd.NA,
            ca.community_area.iloc[0] if len(ca) else pd.NA,
            n.neighborhood.iloc[0] if len(n) else pd.NA)


stops = pd.read_csv("CTA_train.csv")

coords = stops["Location"].str.strip().str.extract(r"\(\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)")
stops["lat"] = coords[0].astype(float)
stops["lon"] = coords[1].astype(float)
assert stops[["lat", "lon"]].notna().all().all(), "unparsed Location values"

stops = stops.rename(columns=LINE_COLS)
for c in ["STOP_NAME", "STATION_NAME", "STATION_DESCRIPTIVE_NAME", "DIRECTION_ID"]:
    stops[c] = stops[c].str.replace(r"\s+", " ", regex=True).str.strip()

no_line = stops[stops[list(LINE_COLS.values())].sum(axis=1) == 0]

agg = {"STATION_NAME": "first", "STATION_DESCRIPTIVE_NAME": "first",
       "lat": "mean", "lon": "mean", "ADA": "max", "STOP_ID": "count"}
agg.update({c: "max" for c in LINE_COLS.values()})
stations = (stops.groupby("MAP_ID", as_index=False).agg(agg)
            .rename(columns={"MAP_ID": "station_id", "STATION_NAME": "station_name",
                             "STATION_DESCRIPTIVE_NAME": "station_full_name",
                             "ADA": "ada_accessible", "STOP_ID": "num_platform_stops"}))
stations["num_lines"] = stations[list(LINE_COLS.values())].sum(axis=1)
stations["lines_served"] = stations[list(LINE_COLS.values())].apply(
    lambda r: ", ".join(k.title() for k, v in r.items() if v), axis=1)

# 2d. Spatial join to community area + neighborhood
stations[["community_area_num", "community_area", "neighborhood"]] = stations.apply(
    lambda r: pd.Series(locate(r.lat, r.lon)), axis=1)
stations["in_chicago"] = stations.community_area.notna()
stations["community_area_num"] = stations["community_area_num"].astype("Int64")

outside = stations[~stations.in_chicago]

stations = stations[["station_id", "station_name", "station_full_name", "lat", "lon",
                     "community_area_num", "community_area", "neighborhood", "in_chicago",
                     "ada_accessible", "num_lines", "lines_served", "num_platform_stops",
                     *LINE_COLS.values()]].sort_values("station_id")
stations.to_csv("cleaned/cta_stations_cleaned.csv", index=False)


def summarise(df, key):
    g = df.groupby(key)
    out = pd.DataFrame({
        "cta_station_count": g.size(),
        "cta_ada_station_count": g.ada_accessible.sum(),
        "cta_lines_count": g[list(LINE_COLS.values())].max().sum(axis=1),
        "cta_lines_served": g[list(LINE_COLS.values())].max().apply(
            lambda r: ", ".join(k.title() for k, v in r.items() if v), axis=1),
        "cta_station_names": g.station_full_name.apply(lambda s: "; ".join(sorted(s))),
    })
    return out.reset_index()


in_city = stations[stations.in_chicago]

by_ca = ca_df[["community_area_num", "community_area", "area_sq_mi"]].merge(
    summarise(in_city, ["community_area_num", "community_area"]),
    on=["community_area_num", "community_area"], how="left")
for c in ["cta_station_count", "cta_ada_station_count", "cta_lines_count"]:
    by_ca[c] = by_ca[c].fillna(0).astype(int)
by_ca[["cta_lines_served", "cta_station_names"]] = by_ca[
    ["cta_lines_served", "cta_station_names"]].fillna("")
by_ca["has_cta_rail"] = by_ca.cta_station_count > 0
by_ca["cta_stations_per_sq_mi"] = (by_ca.cta_station_count / by_ca.area_sq_mi).round(3)
by_ca["area_sq_mi"] = by_ca.area_sq_mi.round(3)
by_ca = by_ca.sort_values("community_area_num")
by_ca.to_csv("cleaned/cta_by_community_area.csv", index=False)

by_nb = nb[["neighborhood"]].merge(
    summarise(in_city.dropna(subset=["neighborhood"]), "neighborhood"),
    on="neighborhood", how="left")
for c in ["cta_station_count", "cta_ada_station_count", "cta_lines_count"]:
    by_nb[c] = by_nb[c].fillna(0).astype(int)
by_nb[["cta_lines_served", "cta_station_names"]] = by_nb[
    ["cta_lines_served", "cta_station_names"]].fillna("")
by_nb["has_cta_rail"] = by_nb.cta_station_count > 0
by_nb.sort_values("neighborhood").to_csv("cleaned/cta_by_neighborhood.csv", index=False)


rail = pd.read_csv("CTA_RailLines.csv")
assert (rail.Name == rail.Field_1).all() and (rail.Name == rail.LINES).all()
rail = rail.drop(columns=["Z", "SHAPE", "Field_1", "LINES"]).rename(columns={
    "X": "lon", "Y": "lat", "Name": "lines", "ALT_LEGEND": "alt_legend", "BRANCH": "branch",
    "DESCRIPTIO": "segment", "LEGEND": "legend", "OWL": "owl_24hr_service",
    "SHAPE.LEN": "segment_length_ft", "TYPE": "track_type"})
rail["owl_24hr_service"] = rail.owl_24hr_service.astype(bool)
rail["segment_length_mi"] = (rail.segment_length_ft / 5280).round(3)
rail[["community_area_num", "community_area", "neighborhood"]] = rail.apply(
    lambda r: pd.Series(locate(r.lat, r.lon)), axis=1)
rail["community_area_num"] = rail["community_area_num"].astype("Int64")
rail.to_csv("cleaned/cta_raillines_cleaned.csv", index=False)


health = pd.read_csv("chicago_health_cleaned.csv")
grocery = pd.read_csv("Grocery_Stores.csv")
h_keys = set(zip(health.GEOID, health.Name.apply(clean_name)))
g_keys = set(zip(grocery["COMMUNITY AREA"], grocery["COMMUNITY AREA NAME"].apply(clean_name)))
c_keys = set(zip(by_ca.community_area_num, by_ca.community_area))
g_nums, c_nums = set(grocery["COMMUNITY AREA"]), set(by_ca.community_area_num)