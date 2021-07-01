# 1. Declare a function called username that takes one argument as a string and return the name
#
# def username(name):
#     return name
#
# print(username("Saim"))
#
# 2. Declare a list with numbers 1 - 5 and iterate through the list and display the list
#
# list = [1, 2, 3, 4, 5]
#
# for i in list:
#     print(i)
#
# 3. Create, AND, &&, &, ==  Which one returns a boolean? ==
#
# 4. What is the difference between a list and a tuple?
# A list [] is mutable whereas a tuple () is immutable
#
# 5. Can we add an element to a list? Yes
# Can we add an element to a tuple? No
# Can the element of a tuple be different types? Yes
#
# 6. Create a dictionary with key value pairs firstname and lastname
# dict = {"firstname": "Saim", "lastname": "Rafiq"}
#
# 7. Add course to the dictionary
# dict = {"firstname": "Saim", "lastname": "Rafiq"}
# dict["Course"] = "DevOps"
# print(dict)
# print(dict["lastname"])
#
# # 8. Create a class called student, initialise the class and create an object of that class
#
# class Student:
#
#     def __init__(self):
#         pass
#
# name = Student()
#
# # 9. Create two functions that takes two arguments each. Func1 = add values and Func2 = Subtract values
# #      Return the addition and subtraction
#
# def add_value(num1, num2):
#     return num1 + num2
#
# def subtract_value(num1, num2):
#     return num1 - num2
#
# print(add_value(4, 2))
# print(subtract_value(5, 2))

# 10. Declare a dictionary with 3 shopping items and write a function to return the total

# shopping_list = {"egss": 1.20, "milk": 2.30, "bread": 1.00}
#
# def total_value(dict):
#     list = dict.values()
#     total = sum(list)
#     return f" The total value is £{total}"
#
# print(total_value(shopping_list))

# 11. Prompt the user to enter an integer, declare a function that checks in the number is odd or even.
# display back to the user with the message "the number you have chosen is odd or even"
#
# num = input("PLease input an integer")
#
# def odd_check(num):
#     if num % 2 == 0:
#         print("Your number is even")
#     else:
#         print("Your number is odd")

# 12 select the correct syntax - 1 -super.__init(). 2- super()__init(). 3 super().__init(). 4 - super().__init__()
# super().__init__() (4)

# Declare a tuple with three values of my choice iterate through the tuple and display the value
#
# my_tuple = ("this", 2, "tuple")
#
# for i in my_tuple:
#     print(i)

# 13 Create a class called student, 1 method called "student_data() returns "student_name"
# class called DevopsStudent which inherits the student class and prints the name
#
# class Student:
#     def student_data(self):
#         return "Saim"
#
# class DevopsStudent(Student):
#     def __init__(self):
#         super().__init__()
#
# ds = DevopsStudent()
# print(ds.student_data())

# 14. Declare a variable called city, declare a method that takes city as an argument, value of city is london. Method checks if the value is london and returns true or false
#
#
# def citycheck(cityname):
#     if cityname == "London":
#         return True
#     else:
#         return False
#
# print(citycheck("London"))
