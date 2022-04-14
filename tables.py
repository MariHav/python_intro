visitor = input("How many guests should come? ")
visitor = int(visitor)

if visitor > 8:
    print("\nSorry, you'll need to wait for 30 minutes so that we make your table"
    + " ready.")
else:
    print("\nYour table is ready. Please follow the waiter.")