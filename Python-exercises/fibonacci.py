# REAL FIBONACCI

def fibonacci(a, b):
    print(a + b)

    if a + b < 1000:
        fibonacci(b, a + b)


print(0)
print(1)

fibonacci(0, 1)



# ELAD NOOBY FIBONACCI

a = 1
b = 1
a_b = a + b
print(a)
print(b)
while True:
    print(a_b)
    a = b
    b = a_b
    a_b = b + a
    if a_b > 10000:
        break
