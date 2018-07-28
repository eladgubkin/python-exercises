# Step 1: Retrieve math operation from the user
operation = input("Which math operation you wanna use?")

# Step 2: ask user whats the first number
first_number = int(input("What is the first number?"))

# Step 3: ask user whats the second number
second_number = int(input("What is the second number?"))

# Step 4: Print the final answer
if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    print(first_number / second_number)
else:
    print("The operation is incorrect")