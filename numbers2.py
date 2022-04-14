number = input("Enter a number, and I'll tell you if it can be divided by 10. ")
number = int(number)

if number % 10 == 0:
    print("\nIt can.")
else:
    print("\It can't. You're a looser")
