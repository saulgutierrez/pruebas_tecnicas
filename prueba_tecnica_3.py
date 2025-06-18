def leer_archivo(enteros):
    # Manejo de errores en la apertura del fichero
    try:
        f = open("numeros.txt")
    except OSError:
        print("No es posible abrir el archivo")
    with f:
        # Leemos cada linea del fichero
        for linea in f.readlines():
            if (f.readlines() == ""): # Manejo de error, linea vacia
                print("Hay lineas vacias en el archivo")
                return
            # Establecemos el delimitador de linea
            palabras = linea.split("\n")
            # Convertimos cada cadena de texto a valor entero y lo agregamos a la lista
            # Asi nos aseguramos de no encontrar el error en el que los valores no son numericos
            temp = int(palabras[0])
            enteros.append(temp)
    return enteros


def procesar_estadisticas(enteros):
    # Total de numeros leidos
    cantidad_numeros = 0
    for i in enteros:
        cantidad_numeros = cantidad_numeros + 1
    print("Total de numeros: ", cantidad_numeros)

    # Promedio
    promedio = 0.0
    suma = 0
    for i in enteros:
        suma += i
    promedio = suma / cantidad_numeros
    print("Promedio: ", promedio)

    # Encontrar el valor maximo
    mayor = 0
    for i in enteros:
        if (i >= mayor):
            mayor = i
    print("Maximo: ", mayor)

    # Encontrar el valor minimo
    menor = 9999999999999999
    for i in enteros:
        if (i <= menor):
            menor = i
    print("Minimo: ", menor)

    # Encontrar la cantidad de valores positivos
    positivos = 0
    for i in enteros:
        if (i > 0):
            positivos += 1
    print("Positivos: ", positivos)

    # Encontrar la cantidad de valores negativos
    negativos = 0
    for i in enteros:
        if (i < 0):
            negativos += 1
    print("Negativos: ", negativos)

    # Encontrar la cantidad de ceros
    ceros = 0
    for i in enteros:
        if (i == 0):
            ceros += 1
    print("Ceros: ", ceros)

    # Encontrar el numero mas frecuente
    n = len(enteros)
    repeticiones = 0
    mas_frecuente = 0

    for i in range(n):
        count = 0
        for j in range(n):
            if enteros[i] == enteros[j]:
                count += 1

        if count > repeticiones or (count == repeticiones and enteros[i] > mas_frecuente):
            repeticiones = count
            mas_frecuente = enteros[i]
    print("El valor mas frecuente es: ", mas_frecuente, "(",repeticiones,") veces")

    # Devolvemos un array con los resultados de todos los calculos, para guardarlo en el archivo
    resultados = [
                    "Total de numeros: ", cantidad_numeros,
                    "Promedio: ", promedio,
                    "Maximo: ", mayor,
                    "Minimo: ", menor,
                    "Positivos: ", positivos,
                    "Negativos: ", negativos,
                    "Ceros: ", ceros,
                    "Numero mas frecuente: ", mas_frecuente, ", (", repeticiones, ") veces"
                ]
    return resultados

def guardar_resultado(resultados):
    # Convertimos a cadena cada elemento de la lista, y lo unimos en una sola con la funcion join,
    # para poder escribirlo en el archivo
    resultados_string = '\n'.join(str(x) for x in resultados)
    # Manejo de error al abrir el archivo. Se abre en modo escritura
    try:
        f = open("resultados.txt", "w")
    except OSError:
        print("No es posible abrir el archivo")
    with f:
        f.write(resultados_string)
    f.close()


if __name__ =="__main__":
    enteros = []
    datos = leer_archivo(enteros)
    resultados = procesar_estadisticas(enteros)
    guardar_resultado(resultados)