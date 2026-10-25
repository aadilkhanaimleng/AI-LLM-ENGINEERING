
class product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

product1=product("apple",50000,4)
print(product1.name,product1.price,product1.quantity)
