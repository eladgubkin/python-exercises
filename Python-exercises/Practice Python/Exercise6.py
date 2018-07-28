import random

x = random.randint(1500, 2701)
for y in range(1500, 2701):
    if y % 5 == 0 and y % 7 == 0:
        print(y)



#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).