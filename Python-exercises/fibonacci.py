def fibonacci(a, b):
    print(a + b)

    if a + b < 1000:
        fibonacci(b, a + b)


fibonacci(0, 1)
