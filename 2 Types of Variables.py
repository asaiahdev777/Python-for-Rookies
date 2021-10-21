myString = "This is a string value"  # holds text
print("String: $myString")

myCharacter = 'A'  # holds a single character
print("Character: $myCharacter")

myInt = 1000  # holds a whole number
print("Int: $myInt")

myFloat = 1.4  # holds a decimal number
print("Double: $myDouble")

myBooleanTrue = True  # a Boolean holds a true/false value
print("Boolean (true): $myBooleanTrue")

myBooleanFalse = False  # a Boolean holds a true/false value
print("Boolean (false): $myBooleanFalse")

# Lists can hold any kind of variable. Have a look:
myListOfStrings = ["Hi,", "everyone.", "Welcome", "to", "Kotlin"]  # a list that holds strings
print(f"List of strings: {myListOfStrings}")

myListOfIntegers = [1, 2, 4, 5, 10000, 345, 12]  # a list that holds integers
print(f"List of integers: {myListOfIntegers}")

print()  # prints empty line

# It is also possible to explicitly state the variable type
# However, usually this is unnecessary, because the compiler can usually tell what kind of variable it is
myCountry: str = "Canada"
print(myCountry)

numberOfHoursInDay: int = 24
print(numberOfHoursInDay)

# None means nothing/null
myNullName = None
print(myNullName)

myNullName = "Henry Ford"
print(myNullName)
