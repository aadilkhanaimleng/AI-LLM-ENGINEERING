class Lead:

    def __init__(self, name, email, status):
        self.name = name
        self.email = email
        self.status = status


lead1 = Lead("Rahul", "rahul@gmail.com", "New")

print(lead1.name, lead1.email, lead1.status)