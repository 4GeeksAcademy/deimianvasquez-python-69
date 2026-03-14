def sum(*args):
    total = 0

    for item in args:
        if type(item) == int or type(item) == float:
            total = total + item
    return total
    # Todo lo que pase aquí no se lee

# print(sum(5, 9, 6, "m", 2.5))

def saludar(**kwargs):


    return f"Hola ¿qué tal {kwargs.get("name", "Nombre")} {kwargs["lastname"]}?"


# print(saludar(name="Deimian", lastname="Vásquez"))


sumar_two = lambda num1, num2: num1+num2
word_upper = lambda word : word.upper()

print(sumar_two(5,9)) 
print(word_upper("demian"))
print(sum(sum(58,60), sumar_two(96, 87)))