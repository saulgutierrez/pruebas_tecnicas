def leer_archivo(texto):
    # Manejo de errores en la apertura del fichero
    try:
        f = open("usuarios.csv")
    except OSError:
        print("No es posible abrir el archivo")
    with f:
        # Leemos cada linea del fichero
        for linea in f:
            # Ignoramos la linea de encabezado
            # Como el encabezado incluye solo letras en minuscula, (el resto de lineas no) consultamos si la linea
            # esta en minuscula, en cuyo caso, la ignoramos en el bucle de lectura
            if linea.islower():
                continue
            # Dividimos cada campo del archivo, por su delimitador, y lo copiamos dentro de un arreglo usando un
            # bucle, de esta manera, podemos copiar todo el contenido del archivo de forma separada, independientemente
            # de la cantidad de columnas, es decir, de forma dinamica
            palabras = linea.split(",")
            for i in palabras:
                texto.append(i)
    return texto

def calcular_estadisticas(texto):
    # Total de usuarios
    cantidad_usuarios = 0
    # Contamos los usuarios basandonos en el salto de linea del documento.
    # Cada salto de linea indica que estamos evaluando a un usuario diferente
    for i in texto:
        if "\n" in i:
            cantidad_usuarios += 1
    # Agregamos un ultimo usuario al conteo final, puesto que el ultimo registro no incluye salto de linea
    cantidad_usuarios += 1
    print("Cantidad de usuarios: ", cantidad_usuarios)

    # Edad promedio de todos los usuarios
    edades = [] # Almacenamos las edades de los usuarios
    # Recorremos cada campo del texto, hasta encontrar un valor que pueda ser convertido a entero, que corresponde a la edad.
    # En tal caso, lo almacenamos
    for i in texto:
        try:
            i = int(i)
            edades.append(i)
        except Exception as e:
            continue
    promedio = 0.0
    suma = 0
    for i in edades:
        suma = suma + i
    promedio = suma/cantidad_usuarios
    print("Edad promedio", promedio)

    # Usuario mas joven
    pos_edades = 0
    pos_edad = 0
    fila = 0
    mas_joven = float('inf')
    for i in edades:
        pos_edades += 1
        if i < mas_joven:
            mas_joven = i
            pos_edad = pos_edades

    mas_joven_datos = []
    for i in texto:
        if "\n" in i:
            fila = fila + 1
            if fila == pos_edad:
                mas_joven_datos.append(i)

    print("Usuario mas joven: ", mas_joven, "Pocision: ", pos_edad)

    # Usuario mas viejo
    mas_viejo = -float('inf')
    for i in edades:
        if i > mas_viejo:
            mas_viejo = i
    print("Usuario mas viejo", mas_viejo)

    # Numero de usuarios por ciudad
    
    # Ciudad con mas usuarios

def guardar_resultados():
    return

if __name__ =="__main__":
    texto = []
    datos = leer_archivo(texto)
    resultados = calcular_estadisticas(texto)