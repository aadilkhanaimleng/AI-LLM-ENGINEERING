#format of menu using while loop

while True:
    print("1. Add")
    print("2. View")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Add selected")

    elif choice == "2":
        print("View selected")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")