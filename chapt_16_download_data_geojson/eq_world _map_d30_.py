from pathlib import Path
import json
import os
import plotly.express as px

#get the actual diretory
current_dir = os.path.dirname(__file__)

# Define the relative path do subdirectory and file
relative_path = os.path.join(current_dir, 'files', 'eq_data_30_day_m1.geojson')

# Define the absolute path to file
absolute_path = os.path.abspath(relative_path)

path = Path(absolute_path)
contents = path.read_text()
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], [] 
for eq_dict in  all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)


title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
	color=mags,
	color_continuous_scale='Viridis',
	labels={'color':'Magnitude'},
	projection='natural earth',
    hover_name=eq_titles,
)
fig.show()