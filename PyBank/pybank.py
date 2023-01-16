import os
import csv

#read csv file
with open ('budget_data.csv', 'r') as csv_file:
    csv_reader= csv.reader(csv_file)

    csv_header=next(csv_reader)

    profitloss = []
    months = []
    netchange = []

   #used loop to find and print the total number of months and the net total of Profit/Losses over the entire period
    for row in csv_reader:
        profitloss.append(int(row[1]))
        months.append(row[0])

    f=open("financial_analysis.txt", "w")
    print("Financial Analysis")
    print("Financial Analysis", file=f)
    print("--------------------------------")
    print("--------------------------------", file=f)

    print("Total Months:", len(profitloss))
    print("Total Months:", len(profitloss),file=f)
    print("Total Profit: $", sum(profitloss))
    print("Total Profit: $", sum(profitloss),file=f)


    #used loop to find change between each month and greatest increase and greatest decrease
    for x in range(1,len(profitloss)):
        netchange.append(profitloss[x] - profitloss[x-1])   
        avg_change = sum(netchange)/len(netchange)
        max_change = max(netchange)
        min_change = min(netchange)
        max_change_month=str(months[netchange.index(max_change)+1])
        min_change_month=str(months[netchange.index(min_change)+1])

    print("Avereage Revenue Change: $",round(avg_change, 2))
    print("Avereage Revenue Change: $",round(avg_change, 2),file=f)
    print("Greatest Increase in Revenue:",max_change_month,"($", max_change,")")
    print("Greatest Increase in Revenue:",max_change_month,"($", max_change,")",file=f)
    print("Greatest Increase in Revenue:",min_change_month,"($", min_change,")")
    print("Greatest Increase in Revenue:",min_change_month,"($", min_change,")",file=f)

 

  