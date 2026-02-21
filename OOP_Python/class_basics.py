#Class name starts with capital letter.
class MercedezBenz:
    pass


print(MercedezBenz)
# Since it
print(type(MercedezBenz))

#it'll return all base classes  
print(str(MercedezBenz.__bases__))

#Class is a blueprint that represents type of a object
#Even the simples class has state and behavior
#Calling the class creates instance of a class.

class audi:
    door = 2
    wheel = 4


print(audi.__dict__)    

a1 = audi()
a2 = audi()

print(a1.wheel)
print(a2.door)

#We tradionally defined class state in body
#Class state is stored in mappingproxy object and retireved using __dict__
#class state is shared and accessed by all instances of a class

#We can add behaviour to a class by adding funcitons
#These functions are special and it'll have atleast one parameter
#This parameter by convention, it's caled self
#When functions are defined within body of the class, they bound to instance of that class.

class Hyundai:
    door = 6
    wheel = 4
    model = 3

    def drive(self):
        return f"i am driving hyundai and my instance is {self}"


h1 = Hyundai()
h2 = Hyundai()

print(h1.drive())
print(h2.drive())
print(h1.drive)