total_sum = 0
for number in range(1000):
    if number % 3 == 0 or number % 5 == 0:
        total_sum = total_sum + number
print(total_sum)

total_sum_1 = 0
for number_1 in range(1000):
    if number_1 % 2 == 0 or number_1 % 4 == 0:
        total_sum_1 = total_sum_1 + number_1
print(total_sum_1)


total_sum_2 = 0
for number_2 in range(400000):
    if number_2 % 2 == 0 or number_2 % 4 == 0:
        total_sum_2 = total_sum_2 + number_2
print(total_sum_2)
