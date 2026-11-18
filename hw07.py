#1 კომენტარების სახით ჩამთვალეთ ყველა შედარებითი ოპერატორები და გააკეთეთ 5-5 ნაგალითი თითოეულზე.

# შედარებითი ოპერატორები Python-ში:
# 1. == (უდრის)
# 2. != (არ უდრის)
# 3. > (მეტია) 
# 4. < (ნაკლებია)
# 5. >= (მეტია ან ტოლია)

1.
print(11 == 11) 
print(5 == 10)
print(3 == 3)
print(7 == 8)
print(15 == 15)

print("NEXT TASK BELOW")

2.
print(11 != 10)
print(5 != 5)
print(6 != 7)
print(1221 != 1441)
print(158 != 158)

print("NEXT TASK BELOW")

3. 
print(35 > 41)
print(4672 > 4671)
print(1 > 0)
print(69 > 67)
print(5847184 > 53343)

print("NEXT TASK BELOW")

4.
print(14 < 18)
print(173 < 33)
print(817 < 1320)
print(553 < 765)
print(670 < 671)

print("NEXT TASK BELOW")

5.
print(63 >= 123)
print(1432 >= 1342)
print(8765 >= 8765)
print(167 >= 999)
print(872 >= 765)

#2 კომენტარების სახით ახსენით რა არის logical operators, ჩამოწერეთ თითოეული და განმარტეთ რომელი რა დროს რა შედეგს გვიბრუნებს.

# 1. and / და - ეს ოპერატორი გამოიყენება მაშინ, როდესაც ორივე პირობა უნდა იყოს მართალი, რომ საბოლოო შედეგი მართალი იყოს.
# 2. or / ან - ეს ოპერატორი გამოიყენება მაშინ როდესაც ერთი პირობა მაინც უნდა იყოს მართალი, რომ საბოლოო შედეგი მართალი იყოს.

#3 გააკეთეთ 3-3 მაგალითი logical operator-ებზე.

print(5 > 3 and 5 < 10)  
print(5 > 3 and 5 > 10)
print(5 < 3 and 5 < 10)

print(5 > 3 or 5 < 10)
print(5 > 3 or 5 > 10)
print(5 < 3 or 5 < 10)

#4 მომხმარებელს შემოატანინეთ რიცხვი, შეინახეთ იგი ცვლადში და შეადარეთ იგი მეტია თუ არა თქვენს მიერ წინასწარ გამზადებულ რიცხვზე.
user_input = int(input("please enter a number: "))
user_number = int(user_input)
my_number = 10
print("my number is 10.")
print("is your number greater than my number?")
print("your number is:", user_number)
print(user_number > my_number)

#5 მომხმარებელს შემოატანინეთ სახელი, შეინახეთ იგი ცვლადში და მკაცრად შეამოწმეთ უდრის თუ არა იგი თქვენს სახელს.
user_name = input("please enter your name: ")
my_name = "john"
print("my name is john.")
print("do we have the same name?")
print("your name is:", user_name)
print(user_name == my_name)

#6 მომხმარებელს შემოატანინეთ თავისი ასაკი, შეინახეთ იგი ცვლადში და შეამოწმეთ მეტია თუ არა იგი 18.
user_age = int(input("please enter your age to enter this website: "))
print("are you over 18?")
print(user_age > 18)