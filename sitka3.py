import matplotlib.pyplot as plt
import csv
from datetime import datetime


open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file,delimiter=",")

header_row = next(csv_file)

print(type(header_row)) #would return a list bcs the header is a list

for index, column_header in enumerate(header_row): #enumerate is a function used w/ lists
    print(index, column_header)

#testing to convert date from string
mydate = datetime.strptime('2018-07-01','%Y-%m-%d')
print(type(mydate))




highs = []
dates = []
lows = []


for row in csv_file:
    highs.append(int(row[5]))   #append adds to the empty list
    lows.append(int(row[6]))
    the_date =  datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(the_date)

print(highs)
print(dates)



fig = plt.figure()

plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.plot(dates,highs,c="red", alpha=0.5) #this is where we gave the data to be plotted
plt.plot(dates,lows, c="blue", alpha=0.5)

plt.fill_between(dates,highs,lows, facecolor='blue', alpha=0.1)

fig.autofmt_xdate()

plt.show()
