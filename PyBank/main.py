import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#initialize lists
months = []
profit = []

#open csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
    print(f"{csv_header}")

    # Loop through rows
    # Assign months & profit as a list
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))

    #find total number of months
    total_months = len(months)
    #check: print(total_months)

    #find net amount of profit/losses
    total_profit = sum(profit)
    #check: print(total_profit)

    #find average of profit/losses over the entire period
    total_change = [profit[i+1]-profit[i] for i in range(len(profit)-1)]
    average_change = sum(total_change)/len(total_change)
    #check: print(average_change)

    #find greatest increase in profits
    greatest_increase = max(total_change)
    greatest_increase_date_index = total_change.index(int(greatest_increase))
    greatest_increase_date = months[greatest_increase_date_index+1]
    #check: print(greatest_increase_date)

    #find greatest decrease in losses
    greatest_decrease = min(total_change)
    greatest_decrease_date_index = total_change.index(int(greatest_decrease))
    greatest_decrease_date = months[greatest_decrease_date_index+1]
    #check: print(greatest_decrease_date)

    #print all to summary table:
    print("*** Financial Analysis ***")
    print(f" Total Months: {total_months}")
    print(f" Net Total: ${total_profit}")
    print(f" Average Change: {average_change}")
    print(f" Greatest Increase in Profits: {greatest_increase_date},  ${greatest_increase}")
    print(f" Greatest Decrease in Losses: {greatest_decrease_date},  ${greatest_decrease}")

#print to text file
with open ("Financial_Analysis.text", "w") as text_file:
    text_file.write(f"*** Financial Analysis *** \n")
    text_file.write(f" Total Months: {total_months} \n")
    text_file.write(f" Net Total: ${total_profit} \n")
    text_file.write(f" Average Change: {average_change}\n")
    text_file.write(f" Greatest Increase in Profits: {greatest_increase_date},  ${greatest_increase}\n")
    text_file.write(f" Greatest Decrease in Losses: {greatest_decrease_date},  ${greatest_decrease}\n")

