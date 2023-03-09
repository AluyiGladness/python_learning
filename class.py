# class Dog():

# # class objects attributes
#     species = "mammal"

#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name

# mydog = Dog("Labratador", "sammy")
# print(mydog.species)




# methods

# class Circle():

#     pi = 3.14

#     def __init__(self, radius=1):
#         self.radius = radius

#     def area(self):
#         return self.radius*self.radius*Circle.pi

#     def set_radius(self, new_r):
#         self.radius = new_r

# myc = Circle(2)
# myc.set_radius(4)
# print(myc.area())




# Inheritance

# class Animal():

#     def __init__(self):
#         print("Animal Class")

#     def whoAmI(self):
#         print("Animal")

#     def eat(self):
#         print("Eating")

# class Dog(Animal):

#     def __init__(self):
#         # Animal.__init__(self)        
#         print("Dog created")

#     def bark(self):
#         print("wolf")

#     def eat(self):
#         print("Dog eating")        



# # Special Methods

# class Book():
    
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):   #this is a special method
#         return "title: {}, Author: {}, pages: {}".format(self.title, self.author, self.pages)    

#     def __len__(self): #another special method
#         return self.pages


# b = Book("Pyhton", "Jose", 800)
# print(b)        