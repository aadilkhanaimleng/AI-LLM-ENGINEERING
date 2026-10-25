class Expense:

    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category


expense1 = Expense("Food", 250, "Personal")

print(expense1.title, expense1.amount, expense1.category)