price= int(input("Enter the price of the product: "))
quantity=int(input("enter the quantity of the product: "))
discount = int(input("enter the discount percentage: ")) 

subtotal = price*quantity
discountamount = subtotal* (discount/100)
total = subtotal - discountamount
print("subtotal is : " , subtotal)
print("discount amount is : " , discountamount)
print("total amount is : " , total)