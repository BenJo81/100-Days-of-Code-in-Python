print("Welcome to Python Pizza Deliveries!")
bill = 0

size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill += 15
    print("Small pizza, $15")
elif size == "M":
    bill += 20
    print("Medium pizza, 20")
else:
    bill += 25
    print("Large pizza, $25")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
        print("Pepperoni, +$2")
    else:
        bill += 3
        print("Pepperoni, +$3")

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    print("Extra cheese, +1")
    bill += 1

print(f"You final bill is: ${bill}")



