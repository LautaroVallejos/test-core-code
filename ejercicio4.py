""" 
    Escribe un programa que muestre por pantalla los números del 1 al 100 y que tenga en cuenta los siguientes casos especiales:

    1. Si el número es múltiplo de 3, mostrar por pantalla el número más la palabra "Fizz"
    2. Si el número es múltiplo de 5, mostrar por pantalla el número más la palabra "Buzz"
    3. Si el número es múltiplo de 3 y 5 a la vez, mostrar por pantalla el número más la palabra "FizzBuzz"
    4. Si no cumple ninguna de las anteriores, mostrar por pantalla solo el número
"""
def main():
    print("Inicio del Programa")
    for num in range(101):
        if num == 0:
            pass

        elif num % 3 == 0 and num % 5 == 0:
            print(str(num) + " FizzBuzz")

        elif num % 3 == 0:
            print(str(num) + " Fizz")
            
        elif num % 5 == 0:
            print(str(num) + " Buzz")

        else:
            print(str(num))


if __name__ == '__main__':
    main()