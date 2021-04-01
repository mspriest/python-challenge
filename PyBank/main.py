import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")
counter = 0
net_profit = 0

# Open and read csv
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
    print(f"{csv_header}")

    # Loop through rows
    for row in csvreader:
       counter += 1
       # print(counter)
       net_profit = net_profit + int(row[1])
       #print(net_profit)
       avg_change = net_profit + 1 / months

    
    months = counter
    print (net_profit)
    print(avg_change)