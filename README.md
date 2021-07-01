### 1. Declare a function called username that takes one argument as a string and return the name
````
def username(name):
    return name

print(username("Saim"))
````
### 2. Declare a list with numbers 1 to 5, iterate through the list and display the list
````
list = [1, 2, 3, 4, 5]

for i in list:
    print(i)
````
### 3. Create, AND, &&, &, ==  Which one returns a boolean? 
````
==
````
### 4. What is the difference between a list and a tuple?
````
A list [] is mutable whereas a tuple () is immutable. Both are ordered.
````
### 5. List and Tuple properties
````
Can we add an element to a list? Yes
Can we add an element to a tuple? No
Can the element of a tuple be different types? Yes
````
### 6. Create a dictionary with key value pairs firstname and lastname
````
dict = {"firstname": "Saim", "lastname": "Rafiq"}
````
### 7. Add course to the dictionary
````
dict = {"firstname": "Saim", "lastname": "Rafiq"}
dict["Course"] = "DevOps"
print(dict)
print(dict["lastname"])
````
### 8. Create a class called student, initialise the class and create an object of that class
````
class Student:

    def __init__(self):
        pass

name = Student()
````
### 9. Create two functions that takes two arguments each. Func1 = add_values and Func2 = Subtract_values. Return the addition and subtraction
```
def add_values(num1, num2):
    return num1 + num2

def subtract_values(num1, num2):
    return num1 - num2

print(add_values(4, 2))
print(subtract_values(5, 2))
```