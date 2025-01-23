class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def talk(self):
        print("bark")


class Cat:
    def talk(self):
        print("meow")


cat = Cat()
cat.talk()

doggo = Dog()
doggo.walk()
doggo.talk()
