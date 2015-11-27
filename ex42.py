class Animal(object):
  def make_a_sound():
    print "About to make a sound"

# Dog is an Animal
class Dog(Animal):
  def __init__(self, name):
    # Dog has a name
    self.name = name

# Cat is an Animal
class Cat(Animal):
  def __init__(self, name):
    # Cat has a name
    self.name = name

# Person is object
class Person(object):
  def __init__(self, name):
    # Person has a name
    self.name = name
    # Person has a pet
    self.pet = None

# Employee is a Person
class Employee(Person):
  def __init__(self, name, salary):
    # Calling Person __init__ method to initialize name
    super(Employee, self).__init__(name)

    # Employee has a salary
    self.salary = salary

class Fish(object):
  pass

class Salmon(Fish):
  pass

class Halibut(Fish):
  pass

# rover is a Dog
rover = Dog("Rover")
# satan is a Cat
satan = Cat("Satan")

# mary is a Person
mary  = Person("Mary")
# mary has a pet satan
mary.pet = satan

frank = Employee("Frank", 120000)
frank.pet = rover

flipper = Fish()
crouse = Salmon()

harry = Halibut()
