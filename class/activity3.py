class Parrot:
    species = 'bird'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
blu = Parrot('blu', 3)
woo = Parrot("woo", 5)

print("blu is a ", blu.species)
print("woo is a ", woo.species)
print(f"{blu.name} is {blu.age} years old ")
print(f"{woo.name} is {woo.age} years old ")