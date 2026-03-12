# from utils.operations import sum
from utils.operations import sum
import datetime as dt
import os

# Esto es un comentario

# Number

number1 = 10
number2 = 25.5

# print(number1 + number2)

# None

database = None 
# print(type(database))


# List
names = ["Deimian", "Juana"]
# print(type(names))


# Object

class Car():
    def __init__(self, color):
        self.color = color
    
my_car = Car("red")
# print(my_car.color)


# Diccionarios
human = {
    "name":"Juanita",
    "pets": ["Gat", "Dog"]
}
# print(human)


# Tuples -- inmutables
pets = ("Bird", "Dog", "Mouse")
# print(pets)


# Set 
fruits1 = {"Pera", "Mango", "Manzana", "Pera"}
fruits2 = {"Fresa", "Mango", "Manzana", "Pera"}
# print(fruits1.union(fruits2))

# String
name = "Deimian"
# print(name)


# print(sum(10, 5))
nowdate = dt.datetime.now()
delta = dt.timedelta(days=5)
# print(f"Esta es la fecha despues de 5 días {nowdate + delta}")
exists = os.path.exists("learn.json")
# print(f"Existe un modulo learn.json {exists}")


PI = 3.141615
URL_BASE = "https://deimian.com"

snack_case = "prueba"
class Human():
    pass














































