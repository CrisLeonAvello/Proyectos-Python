def operaciones(opcion, a, b):
    lista_operaciones = {
        'suma': lambda x, y: x + y,
        'resta': lambda x, y: x - y,  # Corregido
        'multiplicacion': lambda x, y: x * y,  # Corregido
        'division': lambda x, y: x / y if y != 0 else "error de operación, no existe la división de 0",
    }

    operacion = lista_operaciones.get(opcion, lambda x, y: "operación no válida")
    return operacion(a, b)

def main():
    print("--------------------------------------------------------")
    print('Bienvenido a mi primera calculadora en consola de python')
    print('Por favor, selecciona una de las siguientes opciones: ')
    print('1) suma')
    print('2) resta')
    print('3) multiplicación')
    print('4) división')
    print('5) salir')
    print("--------------------------------------------------------")

    operaciones_dict = {
        '1': 'suma',
        '2': 'resta',
        '3': 'multiplicacion',
        '4': 'division',
        '5': 'salir',
    }

    while True:
        opcion = input("Ingresa una de las opciones en pantalla: ")
        
        if opcion == '5':
            print("Hasta luego")
            break
        
        if opcion in operaciones_dict:
            a = float(input("Ingresa el primer valor: "))
            b = float(input("Ingresa el segundo valor: "))
            
            operacion = operaciones_dict.get(opcion)
            resultado = operaciones(operacion, a, b)
            print("Resultado:", resultado)
        else:
            print("Opción no válida, por favor escoge una de las que aparece en pantalla.")

if __name__ == "__main__":
    main()
