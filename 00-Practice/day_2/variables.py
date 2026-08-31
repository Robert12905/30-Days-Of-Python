#!/usr/bin/env python3

print("Day 2: 30 Days of python programming")

first_name="Robert"
last_name="Benstine"

full_name=(first_name + " " + last_name)

country="USA"
city="Fort Myers"
age=21

year=2026

is_married = False

is_true = True

is_lightOn = True

car="charger" ; make = "dodge" ; carYear = 2006 # ALSO READABLE AS: car, make, carYear = "charger", "dodge", 2006

print(

    type(first_name) ,
    type(last_name) ,
    type(full_name) ,
    type(country) ,
    type(city) ,
    type(age) ,
    type(year) , 
    type(is_married) ,
    type(is_true) ,
    type(is_lightOn) ,
    type(car) ,
    type(make) , 
    type(carYear) ,

    sep="\n"

)

print(

        first_name , "is",
        len(first_name),
        "characters long",
        sep=" "
)

name1=len(first_name)
name2=len(last_name)

print(
    "is", first_name, "longer than", last_name, "?:" ,
    name1 > name2,
    sep=" ",
    end="\n"
)

num1=5
num2=2
total=0
diff=0
product=0
division=0
remainder=0
exp=0
floor_div=0

total = num1+num2
print(total,"\n")

diff = num2-num1 
print(diff, "\n")

product = num1*num2
print(product, "\n")

division = num1/num2
print(division, "\n")

remainder = num2%num1
print(remainder, "\n")

exp = num1**num2
print(exp, "\n")

floor_div = num1//num2
print(floor_div, "\n")


area_of_circle=0
pi=3.141592
radius=30
area_of_circle=pi*radius**2,
print("the area of a circle with radius 30:", area_of_circle, sep=" ", end="\n")


userRadius=float(input("input your own radius to calculate: "))

area_of_circle=pi*userRadius**2

print("the area of a circle with radius", userRadius, "is", area_of_circle, sep=" ", end="\n")

# Dictionary

userData={
        
        "userName1": input("what is your first name? "),
        "userName2": input("what is your last name? "),
        "userCountry": input("what is your country? "),
        "userAge": int(input("how old are you? ")),

    }

print(userData["userName1"], userData["userName2"], "age:", userData["userAge"], "from:", userData["userCountry"], ",Welcome!",
sep=" "
)
