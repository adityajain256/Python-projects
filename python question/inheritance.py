
# Create a class Animal with a method speak(). Create a child class Dog that inherits from Animal and overrides the speak() method to print "Woof!"

# class animal:
#         def speak(self):
#                 print("animal Sound")
                
# class dog(animal):
#         def speak(self):
#                 print("woof")
                
# animal = animal()

# animal.speak()
                
# dog = dog()

# dog.speak()
                
                
                
# Create a parent class Person with attributes name and age. Create a child class Employee that inherits from Person and adds an attribute employee_id. Use the super() function to initialize the name and age attributes in the Employee class.

# class person:
#         def __init__(self,name,age):
#                 self._name = name
#                 self._age = age
                
#         def show(self):
#                 print(f"name is {self._name} and age is {self._age}")
# class employee(person):
#         def __init__(self, name, age, EmployeeId):
#                 super().__init__(name, age)
#                 self.EmployeeId = EmployeeId
                
#         def show_empid(self):
#                 super().show()
#                 print(f"Emplyoee Id: {self.EmployeeId}")
        
#         # def EmployeeId(self,Ei):
#         #         self.EmpId = Ei
#         #         print(self.EmpId)

# p1 = person('aditya jain', 19)

# p1.show()

# p2 = employee('aditya jain', 19 , "Tca2459009")
# p2.show_empid()

# Create two parent classes, Flyer and Swimmer. Create a child class Duck that inherits from both Flyer and Swimmer. Implement methods in each parent class and demonstrate how the Duck class can access them.

# class flyer:
#         def fly(self):
#                 print("fly")                
                
        
# class swimmer:
                       
#         def show(self):
#                 print(f"water")
        
# class duck(flyer,swimmer):
        
#         def showD(self):
#                 print("queck...")
                
                
# a1 = flyer()
# a1.fly()

# a2 = swimmer()
# a2.show()

# a3 = duck()
# a3.showD()

# a3.fly()

# a3.show()