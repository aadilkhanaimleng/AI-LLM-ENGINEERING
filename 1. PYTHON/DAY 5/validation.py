#normal conditon
#age = 20

#if age >= 18:
   # print("Valid")


#validation utility condition
def check_age(age):
    if age >= 18:
        return "Valid"
    else:
        return "Invalid"
        
        
     
print(check_age(15))
print(check_age(25))