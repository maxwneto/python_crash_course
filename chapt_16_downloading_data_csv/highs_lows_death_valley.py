import csv
import os
from matplotlib import pyplot as plt
from datetime import datetime

# Get the current directory where high_lows.py is located
current_dir = os.path.dirname(__file__)

# Define the relative path to the sitka_weather_07-2014.csv file
relative_path = os.path.join(current_dir, 'files', 'death_valley_2014.csv')

# Define the absolute path to the sitka_weather_07-2014.csv file
absolute_path = os.path.abspath(relative_path)

with open(absolute_path, mode='r') as file_name:
    reader = csv.reader(file_name)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            # convert string in date and add at current_date
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])

        except ValueError:
            print(current_date, 'missing data')
        
        else:
            dates.append(current_date)
            # Append the high temperature value to the highs list
            highs.append(high)  # Assuming the temperature values are integers
            # Append the low temperature value to the lows list
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(10,6))
# control tansparency
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = "Daily high and low temperatures 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)

fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()