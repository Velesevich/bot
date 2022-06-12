class Person:
    def __init__(self, name):
        self.name = name
    def run(self):
        print(f"{self.name} бегает")

Person("Наталья").run()