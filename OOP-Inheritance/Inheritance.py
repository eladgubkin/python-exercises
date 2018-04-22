class Person(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def say(self):
        print 'Hi :)'

    def __str__(self):
        return 'Person {} is {} years old'.format(self.__name, self.__age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


class Student(Person):

    def __init__(self, name, age, average_score):
        super(Student, self).__init__(name, age)
        self.__average_scores = average_score

    def get_average_score(self):
        return self.__average_scores

    def say(self):
        print 'Good morning Teacher!'


def main():
    person = Person('Jack', 16)
    student = Student('James', 19, 85)
    print person
    print student.say()


if __name__ == '__main__':
    main()
