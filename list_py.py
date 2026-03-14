names = [
    "Alejandro García", "Sofía Rodríguez", "Diego Martínez", "Lucía Fernández",
    "Mateo López", "Isabella González", "Sebastián Pérez", "Valentina Sánchez",
    "Nicolsá Romero", "Camila Torres", "Julián Suárez", "Mariana Castro",
    "Santiago Vargas", "Daniela Mendoza", "Leonardo Ortiz", "Elena Silva",
    "Andrés Morales", "Victoria Ramos", "Gabriel Delgado", "Martina Herrera", "Deimian Vásquez"
]
# index = length - 1

# print(names[len(names)-1]) 
# print(names[1]) 


my_empty_list = []  # Lista vacia
my_list = ["Apple", "Orange", "Donkey"]  # La única forma de declarar una lista
my_tuple = ("Apple", "Orange", "Donkey")  # Esto no es una lista, es una versión más limitada llamada "Tupla"
my_set = {"Apple", "Orange", "Donkey", "apple"}  # Esto no es una lista, es una versión más limitada llamada "set" (conjunto).


# print("Esto es una lista: ",my_list.index("Orange"))
# print("Esto es una Tupla: ",my_tuple.count("Orange"))
# print("Esto es un set: ",my_set)

names[3] = "Juan Salazar"
# print(names[len(names) - 1])
# print(names[2:6:2])
# print(names)

names.append("Maxwell Hernandez")
names.insert(0, "Carlos Silva")
names.insert(4, "Carlos Silva")
item_removed = names.pop()

# names.remove("Carlos Silva")
# print(names)
# del names[0:10]
# print("--" * 30)
# print(names)

y_url = "https://www.youtube.com/watch?v=YlUKcNNmywk&list=RDYlUKcNNmywk&start_radio=1"
y_url = y_url.split("/") 
# del y_url[0:3]
# print("".join(y_url))


# for item in names:
#     print(f"Hola ¿qué tal {item}?")

# for num in range(0, 100):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

count = 0

# while count < len(names):
#     print(names[count])
#     count = count + 1

list_aux = []
for index in range(len(names)):
    list_aux.append(f"{names[index]}-{index}")

# list comprehemsions
# result = [f"{names[index]}-{index}" for index in range(len(names))]
# print(result)



# for index in range(1, 51):
#     if index % 2 == 0:
#         cuadrados.append(index)

pares = [index for index in range(1, 51) if index % 2 == 0]
# print(pares)


cuadrados = [index**2 for index in range(1, 26) if index % 2 == 0]
# print(cuadrados)



# map
# filtrado

# def upper_name(name):
#     return name.upper()

upper_result = list(map(lambda item: item.upper(), names))
# print(upper_result)



filter_result = list(filter(lambda item : "m" in item.lower(), names))
print(filter_result)