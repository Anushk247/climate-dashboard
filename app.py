# from flask import Flask, request, jsonify
# import xarray as xr
# import os

# app = Flask(__name__)

# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route("/upload", methods=["POST"])
# def upload():

#     file = request.files["file"]

#     filepath = os.path.join(UPLOAD_FOLDER, file.filename)

#     # save file first
#     file.save(filepath)

#     # now open dataset
#     ds = xr.open_dataset(filepath)

#     variables = list(ds.data_vars)

#     data = {}

#     for var in variables:
#         values = ds[var].values.flatten()[:100]
#         data[var] = values.tolist()

#     return jsonify({
#         "variables": variables,
#         "data": data
#     })

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify
import xarray as xr
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        # Load NetCDF file using xarray
        ds = xr.open_dataset(filepath)
        
        # Get the first main variable (e.g., 'temperature', 'precipitation')
        var_name = list(ds.data_vars)[0]
        data_var = ds[var_name]

        # 1. Prepare Heatmap Data (Taking the first time slice)
        # Assuming dimensions are named 'lat', 'lon', 'time' (Standard NetCDF format)
        heatmap_data = data_var.isel(time=0).to_dict()
        
        # 2. Prepare Time-Series Data (Global average over time)
        # We average out the latitudes and longitudes to get one value per time step
        time_series = data_var.mean(dim=['lat', 'lon']).to_dataframe().reset_index()
        time_series['time'] = time_series['time'].astype(str) # Convert dates to string for JSON
        
        response_data = {
            'variable': var_name,
            'timeseries_dates': time_series['time'].tolist(),
            'timeseries_values': time_series[var_name].tolist(),
            'heatmap_z': data_var.isel(time=0).values.tolist(), # Z values for map
            'lat': ds['lat'].values.tolist() if 'lat' in ds else [],
            'lon': ds['lon'].values.tolist() if 'lon' in ds else []
        }
        
        ds.close()
        return jsonify(response_data)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)