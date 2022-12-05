class Animal:
    def __init__(self, name, sound="Grrrr"):
        self.name = name
        self.sound = sound

    def make_noise(self):
        print("{} says, {}".format(self.name, self.sound))

    def say_hi(self):
        print(f"{self.name} says, Hi!")


class Cat(Animal):
    # Define it's own __init__ method and call parent __init__ method
    # This allows it to enjoy both worlds
    def __init__(self, name):
        super().__init__(name, "Meow!")

    def rolls(self):
        print(f"{self.name} rolls over. Awww")


class Dog(Animal):
    def action(self):
        print(f"{self.name} wags tail. Awww")


class Hybrid(Dog, Cat):
    def action(self):
        super().action()
        # Cat.rolls(self.name)


pet_cat = Cat("Ginger")
pet_cat.make_noise()
pet_cat.say_hi()
print("-- " * 3)

hybrid = Hybrid("Frank")
hybrid.action()
hybrid.rolls()