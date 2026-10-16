

print("soda:- Rs.300/=")
print("water:- Rs.230/=")
print("milk:- Rs.540/=")

total = 0
for i in range(0,3):
    
    userinput1 = input("enter item name: ")
    
    userinput2 = int(input("price: "))
    
    total += userinput2
    
    print("current total: ",total)
    print()                
print("Final Bill: ",total)    
    
    
    
    
       