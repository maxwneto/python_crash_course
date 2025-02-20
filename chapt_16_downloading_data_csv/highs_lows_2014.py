import csv
import os
from matplotlib import pyplot as plt
from datetime import datetime

# Get the current directory where high_lows.py is located
current_dir = os.path.dirname(__file__)

# Define the relative path to the sitka_weather_07-2014.csv file
relative_path = os.path.join(current_dir, 'files', 'sitka_weather_2014.csv')

# Define the absolute path to the sitka_weather_07-2014.csv file
absolute_path = os.path.abspath(relative_path)

with open(absolute_path, mode='r') as file_name:
    reader = csv.reader(file_name)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        # convert string in date and add at current_date
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        # Append the high temperature value to the highs list
        high = int(row[1])
        highs.append(high)  # Assuming the temperature values are integers
              
    
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red')

plt.title("Daily high temperatures 2014", fontsize=24)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()