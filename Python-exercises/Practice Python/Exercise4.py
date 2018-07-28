num = int(input("Please enter a number to divide: "))

x = range(2, num+1)

divisorList = []

for number in x:
    if num % number == 0:
         divisorList.append(number)
print(divisorList)
