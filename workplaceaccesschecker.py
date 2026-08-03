
approved_users = ["david", "sarah", "michael"]
blocked_users = ["kevin", "james"]
granted_count = 0
denied_count = 0 


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
            denied_count += 1
            continue
        elif username in approved_users:
            break
            
        else:
            attempt += 1
            print("Username is not approved.")
            print(f"You have {3 - attempt} left")

      
    if attempt == 3:
        denied_count += 1
        print("ACCESS DENIED: Too many failed attempts.")
        break
    
    age = int(input("Enter your age: "))
    has_badge = input("Do you have a badge(y/n): ").lower()

    if age < 18 or has_badge.lower() != "n":
        denied_count += 1
    else:
        granted_count += 1
    print()
    print(check_access(username,age,has_badge))
    print()
    check = input("Check another person? ")

    if check.lower() == "y":
        continue
    else:
        print("Thank you for your services!")
        break

print(f"""Access summary: 
      Granted: {granted_count}
      Denied: {denied_count}""")


    

    
    
    
        



                
            
    

         












