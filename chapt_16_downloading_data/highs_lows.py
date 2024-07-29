import csv
import os

# Get the current directory where high_lows.py is located
current_dir = os.path.dirname(__file__)

# Define the relative path to the sitka_weather_07-2014.csv file
relative_path = os.path.join(current_dir, 'files', 'sitka_weather_07-2014.csv')

# Define the absolute path to the sitka_weather_07-2014.csv file
absolute_path = os.path.abspath(relative_path)

with open(absolute_path, mode='r') as file_name:
    reader = csv.reader(file_name)
    header_row = next(reader)

    highs = []
    for row in reader:
        # Append the high temperature value to the highs list
        highs.append(int(row[1]))  # Assuming the temperature values are integers
              
    print(highs)
