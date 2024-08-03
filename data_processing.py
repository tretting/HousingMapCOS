import pandas as pd
import geopandas as gpd
import pyreadr

def read_rds_file(file_path):
    result = pyreadr.read_r(file_path)
    df = next(iter(result.values()))
    return df

def process_data():
    # Path to shapefile
    dir_tiger = "data/tiger/tl_2023_us_zcta520"
    tiger_filename = "tl_2023_us_zcta520.shp"
    dir_RDS = "data/RDSfiles/"
    RDS_filename = "zhvi_demographic_043024.RDS"
    shapedata = gpd.read_file(f"{dir_tiger}/{tiger_filename}")

    # List of ZIP codes for Colorado Springs (example)
    COS_zips = ["80901", "80902", "80903", "80904", "80905", "80906", "80907", "80908", "80909", "80910", "80911", "80912", "80913", "80914", "80915", "80916", "80917", "80918", "80919", "80920", "80921", "80922", "80923", "80924", "80925", "80926", "80927", "80928", "80929", "80930", "80931", "80932", "80933", "80934", "80935", "80936", "80937", "80938", "80939", "80941", "80942", "80943", "80944", "80945", "80946", "80947", "80949", "80950", "80951", "80960", "80962", "80970", "80977", "80995", "80997"]

    # Filter the ZCTA data for Colorado Springs ZIP codes
    COS_shape_data = shapedata[shapedata['GEOID20'].isin(COS_zips)].copy()
    COS_shape_data['GEOID20'] = COS_shape_data['GEOID20'].astype(str)

    # Save the shape data to a separate GeoJSON file
    COS_shape_data.to_file("data/processed/COS_shape_data.geojson", driver="GeoJSON")

    # Read your RDS data
    full_data = read_rds_file(f"{dir_RDS}/{RDS_filename}")

    # Filter the data for the used ZIP codes
    filtered_data = full_data[full_data['RegionName'].isin(COS_zips)].copy()
    filtered_data['RegionName'] = filtered_data['RegionName'].astype(str)

    # Save the economic data to a separate CSV file
    filtered_data.to_csv("data/processed/COS_economic_data.csv", index=False)

if __name__ == '__main__':
    process_data()
