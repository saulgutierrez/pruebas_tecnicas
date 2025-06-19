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
            palabras = linea.split(",")
            temp = palabras[0]
            temp2 = palabras[1]
            temp3 = palabras[2] #.removesuffix("\n")
            texto.append(temp)
            texto.append(temp2)
            texto.append(temp3)
    return texto

def calcular_estadisticas(texto):
    # Total de usuarios
    cantidad_usuarios = 0
    # Contamos los usuarios basandonos en el salto de linea del documento.
    # Cada salto de linea indica que estamos evaluando a un usuario diferente
    for i in texto:
        if "\n" in i:
            cantidad_usuarios += 1
    # Agregamos un ultimo usuario al conteo final, puesto que el ultimo registro no incluye salta de linea
    cantidad_usuarios += 1
    print("Cantidad de usuarios: ", cantidad_usuarios)

    # Edad promedio de todos los usuarios
    # Exraemos los indices de las edades
    edades = [texto.pop(1), texto.pop(3), texto.pop(5), texto.pop(7), texto.pop(9), texto.pop(11)]
    edades_total = 0
    promedio = 0.0
    # Convertimos a valor entero
    edades_int = [int(x) for x in edades]

    for i in edades_int:
        edades_total += i
    promedio = edades_total / cantidad_usuarios
    print("Edad pronedio: ", promedio)

    # Usuario mas joven
    index = 1
    mas_joven = float("inf")
    for i in edades_int:
        if (i <= mas_joven):
            index += 1
            mas_joven = i
    print("Usuario mas joven: (",index, "nombre", mas_joven, "años)")

    # Usuario mas viejo
    
    # Numero de usuarios por ciudad
    
    # Ciudad con mas usuarios

    return texto

def guardar_resultados():
    return

if __name__ =="__main__":
    texto = []
    datos = leer_archivo(texto)
    resultados = calcular_estadisticas(texto)