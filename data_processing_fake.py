import pandas as pd
import geopandas as gpd
import json

def process_data():
    # Path to shapefile
    dir_tiger = "data/tiger/tl_2023_us_zcta520"
    tiger_filename = "tl_2023_us_zcta520.shp"
    shapedata = gpd.read_file(f"{dir_tiger}/{tiger_filename}")

    # List of ZIP codes for Colorado Springs (example)
    COS_zips = ["80901", "80902", "80903", "80904", "80905", "80906", "80907", "80908", "80909", "80910", "80911", "80912", "80913", "80914", "80915", "80916", "80917", "80918", "80919", "80920", "80921", "80922", "80923", "80924", "80925", "80926", "80927", "80928", "80929", "80930", "80931", "80932", "80933", "80934", "80935", "80936", "80937", "80938", "80939", "80941", "80942", "80943", "80944", "80945", "80946", "80947", "80949", "80950", "80951", "80960", "80962", "80970", "80977", "80995", "80997"]

    # Filter the ZCTA data for Colorado Springs ZIP codes
    COS_shape_data = shapedata[shapedata['GEOID20'].isin(COS_zips)]

    # Generate fake data for ZIP code changes in home values
    fake_data = pd.DataFrame({
        'GEOID20': COS_shape_data['GEOID20'],
        'home_value_change': pd.Series([10, -5, 15] * (len(COS_shape_data) // 3 + 1)).sample(len(COS_shape_data)).values
    })

    # Merge with COS data
    COS_data = COS_shape_data.merge(fake_data, on="GEOID20")

    # Save processed data to GeoJSON file
    COS_data.to_file("data/processed/processed_data_fake.geojson", driver="GeoJSON")

if __name__ == '__main__':
    process_data()

