students = ["Aadil", "Rahul", "Aman", "Rohit", "Karan"]
marks = [85, 32, 76, 91, 45] 
def check_result(marks):
    if marks >= 40:
        return "pass"
    else:
        return "fail"

    
print(check_result(85))
print(check_result(32))