def metodo_cuadrados_medios(semilla, n):
    numeros_aleatorios = []
    x = semilla
    for _ in range(n):
        x_cuadrado = x ** 2
        x_str = str(x_cuadrado).zfill(8)  # Aseguramos 8 dígitos
        x = int(x_str[2:6])  # Tomamos los 4 dígitos del medio
        numeros_aleatorios.append(x / 10000)  # Normalizamos a [0, 1]
    return numeros_aleatorios

def metodo_productos_medios(semilla1, semilla2, n):
    numeros_aleatorios = []
    x = semilla1
    y = semilla2
    for _ in range(n):
        producto = x * y
        producto_str = str(producto).zfill(8)  # Aseguramos 8 dígitos
        y = int(producto_str[2:6])  # Tomamos los 4 dígitos del medio
        x = y  # Actualizamos la semilla
        numeros_aleatorios.append(y / 10000)  # Normalizamos a [0, 1]
    return numeros_aleatorios

def metodo_multiplicador_constante(semilla, multiplicador, n):
    numeros_aleatorios = []
    x = semilla
    for _ in range(n):
        x = (multiplicador * x) % 10000  # Realizamos la multiplicación y tomamos el módulo
        numeros_aleatorios.append(x / 10000)  # Normalizamos a [0, 1]
    return numeros_aleatorios

def metodo_congruencial_mixto(semilla, a, c, m, n):
    numeros_aleatorios = []
    x = semilla
    for _ in range(n):
        x = (a * x + c) % m  # Realizamos la operación congruencial
        numeros_aleatorios.append(x / m)  # Normalizamos a [0, 1]
    return numeros_aleatorios

def metodo_congruencial_multiplicativo(semilla, a, m, n):
    numeros_aleatorios = []
    x = semilla
    for _ in range(n):
        x = (a * x) % m  # Realizamos la operación congruencial
        numeros_aleatorios.append(x / m)  # Normalizamos a [0, 1]
    return numeros_aleatorios

def metodo_congruencial_aditivo(semilla, m, n):
    numeros_aleatorios = []
    x = semilla
    for _ in range(n):
        x = (x + semilla) % m  # Realizamos la operación congruencial
        numeros_aleatorios.append(x / m)  # Normalizamos a [0, 1]
    return numeros_aleatorios

def main():
    print("Selecciona un método de generación de números aleatorios:")
    print("1. Método de cuadrados medios")
    print("2. Método de productos medios")
    print("3. Método del multiplicador constante")
    print("4. Método congruencial mixto")
    print("5. Método congruencial multiplicativo")
    print("6. Método congruencial aditivo")

    opcion = int(input("Ingresa el número de tu opción: "))
    n = int(input("Ingresa la cantidad de números aleatorios a generar: "))

    if opcion == 1:
        semilla = int(input("Ingresa la semilla: "))
        print(metodo_cuadrados_medios(semilla, n))
    elif opcion == 2:
        semilla1 = int(input("Ingresa la primera semilla: "))
        semilla2 = int(input("Ingresa la segunda semilla: "))
        print(metodo_productos_medios(semilla1, semilla2, n))
    elif opcion == 3:
        semilla = int(input("Ingresa la semilla: "))
        multiplicador = int(input("Ingresa el multiplicador: "))
        print(metodo_multiplicador_constante(semilla, multiplicador, n))
    elif opcion == 4:
        semilla = int(input("Ingresa la semilla: "))
        a = int(input("Ingresa el coeficiente a: "))
        c = int(input("Ingresa la constante c: "))
        m = int(input("Ingresa el módulo m: "))
        print(metodo_congruencial_mixto(semilla, a, c, m, n))
    elif opcion == 5:
        semilla = int(input("Ingresa la semilla: "))
        a = int(input("Ingresa el coeficiente a: "))
        m = int(input("Ingresa el módulo m: "))
        print(metodo_congruencial_multiplicativo(semilla, a, m, n))
    elif opcion == 6:
        semilla = int(input("Ingresa la semilla: "))
        m = int(input("Ingresa el módulo m: "))
        print(metodo_congruencial_aditivo(semilla, m, n))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
