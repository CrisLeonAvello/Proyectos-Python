def operaciones(a, b, tipo):
    def sum(a, b):
        return a + b

    def rest(a, b):
        return a - b

    def div(a, b):
        if b == 0:
            return "NO existe división por 0"
        return a/b

    def multi(a, b):
        return a * b

def main():
    print("""Calculadora básica con python

        ----Escoge una de las opciones de operación---
          1) suma
          2) resta
          3) multiplicación
          4)división
        """)

    opcion = input("ingresa una de las opciones: ")

    a = int(input("ingrese el primer valor: "))
    b = int(input("ingrese el segundo valor: "))

    if opcion == "1":
        print("el resultado de la suma es", sum(a, b))
    elif opcion == "2":
        print("el resultado es de la resta es", rest(a, b))
    elif opcion == "3":
        print("el resultado de la multiplicación es", multi(a, b))
    elif opcion == "4":
        print("el resultado de la división es", div(a, b))

if __name__ == "__main__":
    main()