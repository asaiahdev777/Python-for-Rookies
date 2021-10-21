class Person:

    # This method is called a constructor. It is called when a class is created.
    def __init__(self, first_name, last_name, age, country):
        # Creating the first_name property (a variable part of a class definition)
        self.first_name = first_name
        # Creating the last_name property
        self.last_name = last_name
        # Creating the age property
        self.age = age
        # Creating the country property
        self.country = country

    # Methods always have the keyword self before any other arguments
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def introduce_person(self):
        print(f'Hi! My name is {self.get_full_name()}. I am {self.age} and I hail from {self.country}')

    def immigrate(self, new_country):
        # You can use both '' and "" to define a string
        print(f"See, I am from {self.country}. I am moving to {new_country}.")
        self.country = new_country
        print("I'll reveal my new identity")
        self.introduce_person()


colombianMan = Person(age=10, country="Colombia", first_name="Carlos", last_name="Merinda")
# To call a method on an object, type the object/variable name, dot, then the method# name 
colombianMan.introduce_person()

print()

chineseMan = Person(first_name="Li", last_name="Feng", age=23, country="China")
chineseMan.immigrate("South Korea")

print()

frenchWoman = Person(first_name="Marie", last_name="St. Louis", age=23, country="France")
frenchWoman.introduce_person()
frenchWoman.age = frenchWoman.age + 15  # Age is a property of the Person class
frenchWoman.introduce_person()

print()

# Look at this (interesting, hmmn?)
frenchWoman.age = colombianMan.age + chineseMan.age + frenchWoman.age
frenchWoman.country = "Cuba"
frenchWoman.introduce_person()
