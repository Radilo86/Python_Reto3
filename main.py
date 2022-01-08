"""
Ejercicio 3
    Enunciado: Crea una función que calcule los números primos entre 1 y N,
    siendo N el parámetro que recibe la función.
Objetivo:
    - Uso de bucles anidados
    - El uso de colecciones
"""
# Radilo86

def numPrimo(num):
    check = True

    while num > 1:
        for a in range(2, num):
            if num % a == 0:
                check = False

        if check:
            print("Es primo: " + str(num))

        num = num - 1
        check = True


if __name__ == "__main__":
    print("COMPROBACION DE Nº PRIMOS")
    numero = int(input("Inserta el numero maximo a comprobar: \n"))
    numPrimo(numero)
