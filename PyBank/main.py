# import pandas as pd


# #Adding file path to be able to read the csv file
# file_path = 'Resources/budget_data.csv'

# df = pd.read_csv(file_path)

# print("Financial Analysis")
# print("-------------------")
# #To count the total number of months included in the data set
# totalMonths = df.shape[0]
# print(f"Total Months: {totalMonths}")

# #Net total amount of profit/losses over the whole period
# netTotal = df['Profit/Losses'].sum()
# print(f"Total: {netTotal}")

# #changes in profit/losses over the time period and then the
# #average of those changes
# df['Change'] = df['Profit/Losses'].diff()

# #dropping 1st row because of titles
# df = df.dropna(subset=['Change'])

# average_change = df['Change'].mean()
# print(f"Average Change: {average_change}")

# #greatest increase in profits (date and amount) over 
# #the entire period
# max_increase = df.loc[df['Change'].idxmax()]
# greatest_increaseDate = max_increase['Date']
# greatest_increaseValue = max_increase['Change']
# print(f"Greatest increase in Profits: {greatest_increaseDate} (${greatest_increaseValue})")

# #greatest decrease in profits
# max_decrease = df.loc[df['Change'].idxmin()]
# greatest_decreaseDate = max_decrease['Date']
# greatest_decreaseValue = max_decrease['Change']
# print(f"Greatest Decrease in Profits: {greatest_decreaseDate} (${greatest_decreaseValue})")

# #exporting text file
# output_file_path = 'Analysis/output.txt'
# with open(output_file_path,'w') as file:
#     file.write("Financial Analysis\n")
#     file.write("-------------------\n")
#     file.write(f"Total Months: {totalMonths}\n")
#     file.write(f"Total: {netTotal}\n")
#     file.write(f"Average Change: {average_change}\n")
#     file.write(f"Greatest increase in Profits: {greatest_increaseDate} (${greatest_increaseValue})\n")
#     file.write(f"Greatest Decrease in Profits: {greatest_decreaseDate} (${greatest_decreaseValue})\n")

#Without using Pandas:

import csv

# Adding file path to be able to read the csv file
file_path = 'Resources/budget_data.csv'

# Reading the CSV file and processing data
with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

print("Financial Analysis")
print("-------------------")

# To count the total number of months included in the data set
totalMonths = len(data)
print(f"Total Months: {totalMonths}")

# Net total amount of profit/losses over the whole period
netTotal = sum(int(row['Profit/Losses']) for row in data)
print(f"Total: {netTotal}")

# Changes in profit/losses over the time period and then the average of those changes
changes = []
for i in range(1, totalMonths):
    current_profit = int(data[i]['Profit/Losses'])
    previous_profit = int(data[i - 1]['Profit/Losses'])
    change = current_profit - previous_profit
    changes.append((data[i]['Date'], change))

# Dropping 1st row because of titles
average_change = sum(change for _, change in changes) / len(changes)
print(f"Average Change: {average_change}")

# Greatest increase in profits (date and amount) over the entire period
greatest_increase_date, greatest_increase_value = max(changes, key=lambda x: x[1])
print(f"Greatest increase in Profits: {greatest_increase_date} (${greatest_increase_value})")

# Greatest decrease in profits
greatest_decrease_date, greatest_decrease_value = min(changes, key=lambda x: x[1])
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})")

# Exporting text file
output_file_path = 'Analysis/output.txt'
with open(output_file_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------\n")
    file.write(f"Total Months: {totalMonths}\n")
    file.write(f"Total: {netTotal}\n")
    file.write(f"Average Change: {average_change}\n")
    file.write(f"Greatest increase in Profits: {greatest_increase_date} (${greatest_increase_value})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})\n")