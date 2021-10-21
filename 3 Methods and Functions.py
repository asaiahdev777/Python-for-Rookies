# Methods/functions are blocks of code that do something
# They can take input called arguments (not always) and can output something in return (not always).
# Take a look:


def print_my_full_name(first_name, last_name):
    print(f"My full name is {first_name} {last_name}")


def print_my_age():
    print("My age is 16")


# To call a method/function, we write the function name, and pass the arguments inside the parentheses
print_my_full_name("Asaiah", "Toutouyoutte")
# We can also directly name the arguments like this:
print_my_full_name(last_name="Toutouyoutte", first_name="Asaiah")
# Or like this
print_my_full_name(first_name="Asaiah", last_name="Toutouyoutte")
# No arguments to pass
print_my_age()
print()  # Just adding a linebreak


# If there's a default value for an argument, you don't need to pass a value
def print_my_full_name_and_age(first_name="John", last_name="Doe", age=30):
    print(f"My name is {first_name} {last_name} and I am {age} years old")


print_my_full_name_and_age()  # Outputs: My name is John Doe and I am 30 years old
print_my_full_name_and_age(age=35)  # Outputs: My name is John Doe and I am 35 years old
print_my_full_name_and_age(last_name="Doug")  # Outputs: My name is John Doug and I am 35 years old
print_my_full_name_and_age(last_name="Donald", age=75)  # Outputs: My name is John Donald and I am 75 years old
print()  # Just adding a linebreak


# If there's a default value for an argument, you don't need to pass a value
# Arguments without a default must go BEFORE those that do have a default value
def print_my_full_name_age_country(age, country, first_name="John", last_name="Doe"):
    print(f"My name is {first_name} {last_name} and I am {age} years old. I am from {country}.")


# Outputs: My name is Asaiah Toutouyoutte and I am 17 years old. I am from Canada.
print_my_full_name_age_country(17, "Canada", "Asaiah", "Toutouyoutte")
# Outputs: My name is John Doe and I am 17 years old. I am from India.
print_my_full_name_age_country(age=17, country="India")
# Outputs: My name is Colton Dixon and I am 17 years old. I am from India.
print_my_full_name_age_country(age=23, first_name="Colton", country="the USA", last_name="Dixon")
