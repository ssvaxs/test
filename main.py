class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1

    @property
    def age(self):
        return self.__name

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print('Incorrect age')

    @property
    def get_name(self):
        return self.__name

    def display_info(self):
        print("Name:", self.__name, ",\tage:", self.__age)


def main():
    tom = Person("Tom")
    tom.age = -10
    tom.age = 20
    tom.display_info()


if __name__ == '__main__':
    main()
