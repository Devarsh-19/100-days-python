class Animal:
    
    def __init__(self):
        self.no_of_eyes = 2
        
    def breathe(self):
        print("Inhale, Exhale.")
        
        

class Cat(Animal):
    
    def __init__(self):
        super().__init__()
    
    def puurr(self):
        print("Meow") 
    
    
    def breathe(self):
        print("Again.")
        super().breathe()
        
        
obj = Cat()
obj.puurr()
obj.breathe()
print(obj.no_of_eyes)