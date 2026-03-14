# Ejercicio 4 - Palindromo:
# Descripción:
# Crea una función llamada es_palindromo que reciba una cadena de texto
# y determine si es un palíndromo (una palabra o frase que se lee igual
# de izquierda a derecha que de derecha a izquierda, ignorando espacios,
# mayúsculas y minúsculas). La función debe devolver True si es un palíndromo
# y False en caso contrario.
# Ejemplo:

# Entrada: "Anita lava la tina"
# Salida esperada: True
# Entrada: "Python"
# Salida esperada: False


def es_palindromo(texto):
    texto_limpio = texto.replace(" ", "").lower()
    texto_invertido = texto_limpio[::-1]

    return texto_limpio == texto_invertido


def main():
    frase = input("Ingresa una frase: ")
    
    if es_palindromo(frase):
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()
