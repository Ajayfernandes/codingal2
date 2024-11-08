def tipping_system(bill, percentage):
    totalbill = (percentage / 100 * bill) + bill
    print("the totalbill is: ", totalbill)

tipping_system(100,10)
