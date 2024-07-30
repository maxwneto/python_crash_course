import csv
import os
import json


# Get the current directory where world_population.py is located
current_dir = os.path.dirname(__file__)

# Define the relative path to the population_data.json file
relative_path = os.path.join(current_dir, 'files', 'population_data.json')

# Define the absolute path to the population_data.json file
absolute_path = os.path.abspath(relative_path)

with open(absolute_path) as file_object:
    pop_data = json.load(file_object)

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        print(country_name + ": " + str(population))