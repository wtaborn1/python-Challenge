print("Hello World")
import csv
#import os
#csvpath = os.path.join("..")
profit_loss = []
date = []
line_num = 0
with open ("budget_data.csv") as budget_data:
    for line in budget_data:
        if line_num != 0:
            split_line = line.split(",")
            split_line[1] = split_line[1].strip("\n")
            split_line[1] = int(split_line[1])
            profit_loss.append(split_line[1])

            date.append(split_line[0])
        line_num = line_num +1
  #  print("profit_loss", profit_loss)
   # print("date:", date)
num_months = len (date)
print ("total months {0}".format(num_months))
total_dollars = sum (profit_loss)
print ("Total: $" + str(total_dollars))
#average change in profit and losses
differce_sum = 0
prev_amount = profit_loss [0]
for dollar_amount in profit_loss:
    the_difference = dollar_amount -prev_amount
    differce_sum = the_difference + differce_sum
    prev_amount = dollar_amount
average_change = differce_sum/(num_months-1)

print("Average Change:${0}".format (average_change))

# Trying to capture the greatest amount difference
most_profitable = 0
prev_amount = profit_loss[0]
for dollar_amount in profit_loss:
    the_difference = dollar_amount - prev_amount
   # print("different amount",the_difference)
    if the_difference >= most_profitable:
        most_profitable = the_difference
    prev_amount = dollar_amount
print("Greatest increase in profits:${0} ".format(most_profitable))
# Capturing the least amount
least_profitable = 1000000
prev_amount = profit_loss[0]
for dollar_amount in profit_loss:
    the_difference = dollar_amount-prev_amount
    if the_difference <= least_profitable:
        least_profitable = the_difference
    prev_amount = dollar_amount
print("Greatest decrease in profits:${0}".format(least_profitable))

#Writing files and outputs
with open ("financial_output.txt", "w") as financial_ouput:
    financial_ouput.write("total months {0}\n".format(num_months))
    financial_ouput.write("Total:${0}\n".format(total_dollars))
    financial_ouput.write("Average Change:${0}\n".format (average_change))
    financial_ouput.write("Greatest increase in profits:${0}\n".format(most_profitable))
    financial_ouput.write("Greatest decrease in profits:${0}\n".format(least_profitable))



