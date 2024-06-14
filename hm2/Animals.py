class Animal:
    def __init__(self, name):
        self.name = name
        
    def reply(self):
        return self.speak()

class Mammal(Animal):
    pass

class Cat(Mammal):
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        string_name = self.name + ' says Meow!'
        return string_name

class Dog(Mammal):
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        string_name = self.name + 'says Roof!'
        return string_name

class Primate(Mammal):
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        string_name = self.name + 'says puppyCat'
        return string_name

class ComputerScientist(Primate):
    def __init__(self, name):
        self.name = name 
