
menu = {
    "pizza": 3.50,
    "burger": 5.00,
    "popcorn": 6.00,
    "nachos": 4.00,
    "soda": 1.50,
    "water": 1.00
}

cart = []
total = 0

print("------------------MENU--------------------")
for k,v in menu.items():
    print(f"{k:10}: ${v:.2f}")
print("----------------------------------")

while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------------------YOUR ORDER--------------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")


