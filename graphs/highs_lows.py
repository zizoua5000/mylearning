import csv

from datetime import datetime

import matplotlib.pyplot as plt

filename = "data/sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)
    print(highs)


# plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c="blue")

# Format plot
plt.title("Daily high temperatures, 2014", fontsize=14)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature F", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()