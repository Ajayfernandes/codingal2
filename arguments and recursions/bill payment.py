def bill_amount(bill, tip_amount):
    total = (bill * 0.01) * (100 + tip_amount)
    print(f"the total cost is " , total)
bill = int(input("what is the amount to be paid? : "))
tip_amount = int(input("what is the percentage of tip u want to pay? : "))

bill_amount(bill, tip_amount)

    
