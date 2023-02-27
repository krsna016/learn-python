# Creating the dog class:
class Dog():
    # This is called 'docstring' tell the uses what the class and function does:
    """Creating a 'dog' class"""
    
    # Difining the __init__ method (constructor) to pass the attributes for the class:
    # name and age are the parameter for (constructor) __init__ method or called the attributes of the class i.e name and age, here:
    def __init__(self,name,age):
        """Initialize 'name' and 'age' attribute"""
        # Attributes for the class:
        self.dog_name = name
        self.dog_age = age

    # Creating the instance method or method of the class:
    def sit_dog(self):
        """Simulate a dog to sit in response"""
        print(f"Kindly make the dog named {self.dog_name.title()}, sit.")
    
    # Creating the instance method or method of the class:
    def roll_over(self):
        """Simulate a dog to roll in response"""
        print(f"Kindly make the dog named {self.dog_name} to roll.")

# Creating instance from the class by calling class with the required argument, the init method will return the instance and get saved in my_dog:
my_dog = Dog("Dog_1",4)
your_dog = Dog("Dog_2",2)
# Printing the attribute value using the dot notation:
print(f"My dog name is : {my_dog.dog_name}\nIt's age is : {my_dog.dog_age}")
# Using the dot notation to call a method:
my_dog.sit_dog()
my_dog.roll_over()
your_dog.sit_dog()
your_dog.roll_over()