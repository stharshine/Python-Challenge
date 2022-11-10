import csv

# Files to Load
file_to_load = "PyBank/Resources/budget_data.csv"
file_to_output = "PyBank/Resources/budget_analysis.txt"


total_months = 0
total_revenue = 0
prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]  #i am sure there are better ways but this is what i gathered from my coursemates
greatest_decrease = ["", 9999]


revenue_changes = [] #made it into an empty list as


with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:


        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row["Date"]


        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]

        revenue_changes.append(int(row["Profit/Losses"]))

    revenue_avg = sum(revenue_changes) / len(revenue_changes)
    
    
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(float(sum(revenue_changes) / len(revenue_changes)))) # i am not sure sorry
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
#sorry i dont know how to put it into text file