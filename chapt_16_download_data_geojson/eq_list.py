from pathlib import Path
import json
import os

#get the actual diretory
current_dir = os.path.dirname(__file__)

# Define the relative path do subdirectory and file
relative_path = os.path.join(current_dir, 'files', 'eq_1_day_m1.geojson')

# Define the absolute path to file
absolute_path = os.path.abspath(relative_path)

path = Path(absolute_path)
contents = path.read_text()
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats = [], [], []   
for eq_dict in  all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)


print(mags[:10])
print(lons[:5])
print(lats[:5])