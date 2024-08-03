from flask import Flask, render_template, jsonify
import geopandas as gpd
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    # Load preprocessed data
    COS_data = gpd.read_file("data/processed/processed_data_fake.geojson")

    # Convert GeoDataFrame to GeoJSON format
    COS_data_json = json.loads(COS_data.to_json())

    return jsonify(COS_data_json)

if __name__ == '__main__':
    app.run(debug=True)
