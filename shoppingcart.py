
cart = []

while True:
    

    print("""menu 
        1. add item and price (1)
        2. update item and price  (2)
        3. take an item out (3)
        4. view cart (4)
        5. exit (press "q" to exit)""")
    
    user_input = input(">")
    
    if user_input == "1":
        while True:
            item = input("Enter the item you want to add to the list(q to quite): ")

            if item == "q":
                break
            else:
                price = float(input("Enter the price of the item: "))

                cart.append([item,price])


    if user_input == "2":
        pass

    if user_input == "3":
        dele = input("Enter item you want to take out: ")
        for i in cart:
            if dele == i[0]:
                print("Item found and deleted")
                cart.remove(i)
                break
        else:
            print("Item not found")
                


            


    if user_input == "4":
        total = 0
        for i in cart:
            print(f"{i[0]} - ${i[1]}")
        for price in cart:
            total += price[1]
        print(f"Your total is ${total:.2f}")

    if user_input == "q":
        break




    

   
