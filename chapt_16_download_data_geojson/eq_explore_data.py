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

relative_path = os.path.join(current_dir, 'files', 'readable_eq_data.geojson')
absolute_path = os.path.abspath(relative_path)
path = Path(absolute_path)

readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)




""" path = Path('files/eq_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)


path = Path('files/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)
 """
