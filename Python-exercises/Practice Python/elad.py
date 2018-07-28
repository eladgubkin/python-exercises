import random

x = random.randint(1, 100)
print(x)
y = int(input("what do you think is the number?"))

if y == x:
    print("GREAT SUCCESS")
else: 
    z = int(input("You can try 2 more times."))
    if z == x:
        print("GREAT SUCCESS")
    else:
        a = int(input("You have another chance."))
        if a == x:
            print("GREAT SUCCESS")
        else:
            print("You failed!@!@!")
            print("The randon number was", x)
  
