# TODO: it's a playground, let's write some code (no unit tests to run here)

radius = 5
from math import pi 
perimeter = 2*radius *pi

print(radius)
print(perimeter)


area = pi*(radius*radius)
print(area)

print(round(area))


# String Interpolation
str = f'{area} is the area'
print(str)

type('Le Wagon')
type(None)


# Exponent 
print(2**5)

# more math
import math
print(math.floor(3.2))
print(math.ceil(3.2))
print(math.factorial(5))

import datetime
today = datetime.date.today()
print(today)

day=datetime.date.fromisoformat('2020-03-16')
print(day.month)
print(day.strftime("%A %B %d, %Y"))


# Functions
## from slides
def vote(age):
    if age<18:
        return "You can not vote"
    else:
        return "You can vote"

print(vote(24))
print(vote(15))

def is_even(number):
    return number%2==0
print(f'4 is even: {is_even(4)}')
print(f'3 is even: {is_even(3)}')

def greet(first_name, last_name):
    full_name=f"{first_name.capitalize()} {last_name.upper()}"
    return f"Hello, {full_name}"
print(greet("ringo","starr"))
#full_name #error expected due to scope

def circle_math(radius):
    perimeter=2*pi*radius
    area=pi*radius*radius
    return [perimeter, area]
values = circle_math(5)
print(f"Radius=5 => Perimeter={round(values[0], 1)}, Area={round(values[1], 1)}")

values = circle_math(6)
print(f"Radius=6 => Perimeter={round(values[0], 1)}, Area={round(values[1], 1)}")

def open(hour):
    if (hour >= 9 and hour < 12) or (hour >= 14 and hour < 19):
        return "The store is open!"
    else:
        return "Sorry it's closed."
 
print(open(10))