def total_calc(bill_amount, tip_perc):
    total_cost = bill_amount+tip_perc
    total_bill = round(total_cost, 2)
    print("Your Total Bill is: ", total_bill)
    
print(total_calc(250, 10))