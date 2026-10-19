expenses = [100, 250, 80, 300, 150]

def total_expense():
    total = 0
    for expense in expenses:
        total += expense

    return total
    
    
result = total_expense()

print("Total expenses:", result)


def count_expenses(): 
    count = 0

    for expense in expenses:
      count += 1

    return count

count = count_expenses()
print("Number of expenses:", count)


def average_expense():
    total = total_expense()
    count = count_expenses()

    average = total / count

    return average  
average = average_expense()

print("Average expense:", average)


print("========================")
print("     EXPENSE SUMMARY")
print("========================")

print("Total expenses:", total_expense())
print("Number of expenses:", count_expenses())
print("Average expense:", average_expense())

print("========================")
