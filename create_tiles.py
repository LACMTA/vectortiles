import os
import subprocess

input_dir = 'input'
output_dir = '..'

for filename in os.listdir(input_dir):
    if filename.endswith('.geojson'):
        base_name = os.path.splitext(filename)[0]
        mbtile_file = os.path.join(output_dir, base_name + '.mbtiles')
        tile_dir = os.path.join(output_dir, base_name)

        # Create mbtile format vector tile with tippecanoe
        subprocess.run(['tippecanoe', '-o', mbtile_file, '-Z0', '-z15', '-pk', '-pf', '-f', '-l', base_name, os.path.join(input_dir, filename)], check=True)

        # Convert the mbtile to a directory of tiles with mb-util
        subprocess.run(['mb-util', mbtile_file, tile_dir], check=True)

        # Delete the geojson file
        os.remove(os.path.join(input_dir, filename))