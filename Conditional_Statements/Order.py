# ordering system
# suppose to order baryani if order is more than 300 then dilevery is free other wise cost of 30

Order_Amount = int(input('Please Enter your Order Amount : '))

Result = "Dilevery Free" if Order_Amount >=300 else "You Cost 30 Dilevery Charges"

print(Result)