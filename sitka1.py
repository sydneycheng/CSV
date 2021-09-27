import csv
from os import X_OK

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file,delimiter=",")

header_row = next(csv_file)

print(type(header_row)) #would return a list bcs the header is a list

for index, column_header in enumerate(header_row): #enumerate is a function used w/ lists
    print(index, column_header)


highs = []

for row in csv_file:
    highs.append(int(row[5]))   #.append adds to the empty list

print(highs)

import matplotlib.pyplot as plt

plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.plot(highs,c="red") #this is where we gave the data to be plotted

plt.show()