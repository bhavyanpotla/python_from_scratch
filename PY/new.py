class ABC:
    count = 0    

    def __init__(self, name, sec):
        self.name = name
        self.sec = sec
        ABC.count += 1
        print(f"Object count: {ABC.count}")

    def display(self):
        print(f"Name: {self.name}, Section: {self.sec}")


 
a1 = ABC("Alice", "A")
a2 = ABC("Bob", "B")
a3 = ABC("Charlie", "C")

a1.display()
a2.display()
a3.display()