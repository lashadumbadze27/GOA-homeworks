# მომხმარებელს შემოაყვანინე სამი რიცხვი, ხოლო პროგრამამ დაბეჭდოს მათი საშუალო არითმეტიკული.
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
num3 = float(input("Please enter the third number: "))
average = (num1 + num2 + num3) / 3
print("The average of the three numbers is:", average)

# მომხამრებელს შემოაყვანინე ორი რიცხვი და დაბეჭდე მათი ჯამი.
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
result = num1 + num2
print("The sum of the two numbers is:", result)

# დაბეჭდე შენი ოჯახის წევრების სახელები
dad_name = input("Please enter your father's name: ")
mum_name = input("Please enter your mother's name: ")
sister_name = input("Please enter your sister's name: ")
print("My father's name is " + dad_name + " and my mother's name is " + mum_name + " and my sister's name is " + sister_name)

#  მომხმრებელს შემოაყვანინე ქვეყანა, ქალაქი, ქუჩა, რაიონი, შენობა და სართული და დაბეჭდე სრული მისამართი.
country = input("Please enter the name of the country you currently are located in: ")
city = input("Please enter the name of the city you currently are located in: ")
street = input("Please enter the name of the street you currently are located on: ")
district = input("Please enter the name of the district you currently are located in: ")
building = input("Please enter the name of the building you currently are located in: ")
floor = input("Please enter the floor number you currently are located on: ")
print("Your full address is" + " " + country + ", " + city + ", " + street + ", " + building + ", Floor" + " " + floor + ", " + district)

# მომხმარებელს შემოაყვანინე მათი ასაკი
age = int(input("Please enter your age: "))
print("Your age is: " + str(age))