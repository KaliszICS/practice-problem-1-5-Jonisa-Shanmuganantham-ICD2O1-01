'''
    Lesson: Typecasting and documentation
    Author: Jonisa Shanmuganantham
    Date Created: Sept 23, 2024
    Date Last Modified: Sept 23, 2024
'''
def q1():
  integer = input("Input an integer: ")
  integer = (int(integer))
  integer = integer + 3
  print(integer)

def q2():
  number = input("Input a number: ")
  number = (str(number) + "4")
  number = (float(number))
  number = (number + 2)
  print(number)

def q3():
  radius = input("Input a radius: ")
  radius = (float(radius))
  area = (radius *  radius * 3.14)
  print(area)

def q4():
  number = input("Input a number: ")
  number = (float(number))
  number = (number * 12)
  number = (int(number))
  print(number)

def q5():
  integer = input("Input an integer: ")
  integer = (int(integer))
  integer = (integer + 5)
  print(f"Your number + 5 is {integer}")
'''
q1()
q2()
q3()
q4()
q5()
'''