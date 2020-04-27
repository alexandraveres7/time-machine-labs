class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tricks = []

    def bark(self):
        print('Woof woof')

    def add_tricks(self, trick):
        self.tricks.append(trick)

    def age_in_human_years(self):
        hy = [15, 24, 28, 32, 36, 42, 47, 51, 56, 60]
        dy = self.age
        print(hy.pop(dy+1))


my_dog = Dog("Berta", 5)
my_dog.bark()
my_dog.age_in_human_years()
my_dog.add_tricks('roll over')
my_dog.add_tricks('play dead')
print(my_dog.tricks)

