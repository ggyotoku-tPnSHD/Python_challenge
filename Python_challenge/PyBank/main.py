import os
import csv
from numpy import average

output_file = os.path.join("..", "Analysis", "Bank_results.txt")
csvpath = os.path.join("..", "Resource", "budget_data.csv")

profit_loss = []
month_index = []
profit_change = []
greatest_increase_index = 0
greatest_decrease_index = 0

with open(csvpath) as csvfile:
    """The script returns the statistics of the budget data."""
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # cast row 2 as an integer
    for row in csvreader:
        if row != csv_header:
            profit_loss.append(int(row[1]))
            month_index.append(row[0])

    for count in range(len(profit_loss)):
        if count < 85:
            profit_change.append(profit_loss[count] - profit_loss[count+1])

    average_change = average(profit_change)
    greatest_increase = max(profit_change)
    greatest_decrease = min(profit_change)

    for i, e in enumerate(profit_change):
        if e == greatest_increase:
            greatest_increase_index += i+1
        elif e == greatest_decrease:
            greatest_decrease_index += i+1

print("```\nFinancial Analysis")
print('----------------------------------')
print(f'Total Months: {len(profit_loss)} ')
print(f'Total: $ {sum(profit_loss)} ')
print(f'Average Change: $ {round(average_change,2)}')
print(
    f'Greatest Increase in Profits: {month_index[greatest_increase_index]} $ {greatest_increase} ')
print(
    f'Greatest Decrease in Profits: {month_index[greatest_decrease_index]} $ {greatest_decrease} ')
print("```")

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["```\nFinancial Analysis"])
    writer.writerow(['----------------------------------'])
    writer.writerow([f'Total Months: {len(profit_loss)} '])
    writer.writerow([f'Total: $ {sum(profit_loss)} '])
    writer.writerow([f'Average Change: $ {round(average_change,2)}'])
    writer.writerow([
        f'Greatest Increase in Profits: {month_index[greatest_increase_index]} $ {greatest_increase} '])
    writer.writerow([
        f'Greatest Decrease in Profits: {month_index[greatest_decrease_index]} $ {greatest_decrease} '])
    writer.writerow(["```"])
