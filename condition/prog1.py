'''
# Price of a house is $1M.If buyer has good credit,
they need to put down 10% otherwise they need to put down 20%.
#Print the down payment.'''
houseprice = 1000000
credit = input("do you have good credit:(Y/N): ").upper()
if credit == "Y":
    downpayment = (houseprice * (10 / 100))
    print(f"Your down payment is {downpayment} $ ")
elif credit == "N":
    downpayment = (houseprice * (20 / 100))
    print(f"Your down payment is {downpayment} $")
else:
    print("user need to input wheather they have good credit or not as [Y/N]")