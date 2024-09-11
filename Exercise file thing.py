# The file below has missing data points. Any row with a missing data point should be left out.
# You must not edit the file manually. Any editing must be done through code.

# Open the file
f = open("exercise.csv", 'r')
a = f.read()
f.close()

#Split the content into rows
lines = a.strip().split('\n')

#Extract the header and data rows
header = lines[0].split(',')
data_rows = [line.split(',') for line in lines[1:]]

#Convert the data to a usable format, skipping rows with missing data or incorrect length
cleaned_data = []
for row in data_rows:
    if len(row) == len(header) and '' not in row:  #skip rows with missing data points or incorrect length
        #Convert the numeric values
        duration = int(row[0])
        pulse = int(row[1])
        maxpulse = int(row[2])
        calories = float(row[3])
        cleaned_data.append((duration, pulse, maxpulse, calories))

#Organize data by session duration (first column)
from collections import defaultdict

duration_data = defaultdict(list)
for row in cleaned_data:
    duration = row[0]
    calories = row[3]
    duration_data[duration].append(calories)

#calculate average calories burned for each duration
average_calories = {duration: sum(values) / len(values) for duration, values in duration_data.items()}

#Calculate top 20 and bottom 20 averages for each session type
top_20_calories = {}
bottom_20_calories = {}

for duration, calories in duration_data.items():
    sorted_calories = sorted(calories, reverse=True)
    top_20 = sorted_calories[:20]
    bottom_20 = sorted_calories[-20:]
    top_20_calories[duration] = sum(top_20) / len(top_20) if len(top_20) > 0 else 0
    bottom_20_calories[duration] = sum(bottom_20) / len(bottom_20) if len(bottom_20) > 0 else 0

#Display the results in a table-like format
print(f"{'Session Duration(m)':<20} {'Average Calories burned':<25} {'Top 20 Average':<20} {'Bottom 20 Average':<20}")
for duration in average_calories:
    print(f"{duration:<20} {average_calories[duration]:<25} {top_20_calories[duration]:<20} {bottom_20_calories[duration]:<20}")
