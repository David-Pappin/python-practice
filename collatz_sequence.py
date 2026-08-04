
def collatz(number):
    
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

check = True
while check:
    num = int(input("Enter a number: "))
    if num >= 1:
         check = False
    else:
         print("Number cant be less than 0")
         
    

while num > 1:
        num = collatz(num)
        print(num)
   
    






        
    
    
     
