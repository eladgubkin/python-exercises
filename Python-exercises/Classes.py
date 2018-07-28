import random


class CrazyPlane:

    def __init__(self):
        self.x = 0
        self.y = 0

    def update_position(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

    def get_position(self):
        print(self.x, self.y)


def main():
    plane1 = CrazyPlane()
    xpos, ypos = plane1.get_position()


print(main())



# class Employee:
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = ''.join([first, '.', last, '@company.com'])
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#
# emp_1 = Employee('Elad', 'Gubkin', 30000)
# emp_2 = Employee('Alon', 'Gubkin', 50000)
#
# # print emp_1.email
# # print emp_2.email
# print emp_2.fullname()
# # print emp_1.fullname()
# # print emp_2.fullname()