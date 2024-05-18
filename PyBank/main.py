import pandas as pd


#Adding file path to be able to read the csv file
file_path = 'Resources/budget_data.csv'

df = pd.read_csv(file_path)

print("Financial Analysis")
print("-------------------")
#To count the total number of months included in the data set
totalMonths = df.shape[0]
print(f"Total Months: {totalMonths}")

#Net total amount of profit/losses over the whole period
netTotal = df['Profit/Losses'].sum()
print(f"Total: {netTotal}")

#changes in profit/losses over the time period and then the
#average of those changes
df['Change'] = df['Profit/Losses'].diff()

#dropping 1st row because of titles
df = df.dropna(subset=['Change'])

average_change = df['Change'].mean()
print(f"Average Change: {average_change}")

#greatest increase in profits (date and amount) over 
#the entire period
max_increase = df.loc[df['Change'].idxmax()]
greatest_increaseDate = max_increase['Date']
greatest_increaseValue = max_increase['Change']
print(f"Greatest increase in Profits: {greatest_increaseDate} (${greatest_increaseValue})")

#greatest decrease in profits
max_decrease = df.loc[df['Change'].idxmin()]
greatest_decreaseDate = max_decrease['Date']
greatest_decreaseValue = max_decrease['Change']
print(f"Greatest Decrease in Profits: {greatest_decreaseDate} (${greatest_decreaseValue})")

