import sys

approved_users = ["david", "sarah", "michael"]
blocked_users = ["kevin", "james"]


def check_access(username, age, has_badge):
    if username in blocked_users:
        return "Access denied: this user is blocked."
    else:
        if username not in approved_users:
            return "Access denied: username is not approved."
            
        elif age < 18:
            return "Access denied: you must be at least 18."

        elif has_badge != "y":
            return "Access denied: badge required."
        else:
            return "Access granted. Welcome, " + username.capitalize()



while True:
    attempt = 0
    while attempt < 3:
        username = input("Enter your name: ").lower()
        if username in blocked_users:
            print("Access denied: this user is blocked.")
            continue
        elif username in approved_users:
            break
            
        else:
            attempt += 1
            print("Username is not approved.")
            print(f"You have {3 - attempt} left")
    if attempt == 3:
        print("ACCESS DENIED: Too many failed attempts.")
        sys.exit()

    age = int(input("Enter your age: "))
    has_badge = input("Do you have a badge(y/n): ").lower()
    print()
    print(check_access(username,age,has_badge))
    print()
    check = input("Check another person? ")

    if check.lower() == "y":
        continue
    else:
        print("Thank you for your services!")
        break


    

    
    
    
        



                
            
    

         












