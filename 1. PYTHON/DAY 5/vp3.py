def check_withdrawal(amount, balance):
    if amount > 0 and amount <= balance:
        return "Approved"
    else:
        return "Declined"


print(check_withdrawal(500, 2000))
