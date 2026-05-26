class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self, food):
        self.weight -= food
        return self.weight

    def info(self):
        print(f"{self.name}, {self.age} years, {self.weight} kg")


class Cat(Animal):
    def __init__(self, name, age, weight, breed):
        super().__init__(name, age, weight)
        self.breed = breed

    def bark(self):
        print("MEOW!")