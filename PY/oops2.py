class Animal:
    def speak(self):
        print("some animals sound")

class Cat(Animal):
    def speak(self):
        print("Meow!") 

a = Cat()
a.speak() 
b = Animal()
b.speak()
