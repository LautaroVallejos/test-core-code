# Crea una estructura if/else dentro del bucle para que esta imprima "Hola" cuando el número sea 5
def main():
    print("Inicio del Programa")
    for num in range(101):
        print(num)
        if num == 5:
            print("Hola")
        else:
            pass

if __name__ == '__main__':
    main()