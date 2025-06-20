def leer_archivo(texto):
    # Manejo de errores en la apertura del fichero
    try:
        f = open("usuarios.csv", encoding="utf-8")
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
    # Obtenemos la edad mas pequeña
    pos_mas_joven = 0
    mas_joven = float('inf')
    for i in edades:
        if i < mas_joven:
            mas_joven = i

    # Buscamos el nombre del usuario al que corresponde
    for i in texto:
        pos_mas_joven += 1
        if (i == str(mas_joven)):
            nombre_mas_joven = pos_mas_joven - 2
    print("Usuario mas joven: ", texto[nombre_mas_joven], "(",mas_joven,") años")

    # Usuario mas viejo
    # Obtenemos la edad mas alta
    pos_mas_viejo = 0
    mas_viejo = -float('inf')
    for i in edades:
        if i > mas_viejo:
            mas_viejo = i

    # Buscamos el nombre del usuario al que corresponde
    for i in texto:
        pos_mas_viejo += 1
        if (i == str(mas_viejo)):
            nombre_mas_viejo = pos_mas_viejo - 2
    print("Usuario mas viejo: ", texto[nombre_mas_viejo], "(",mas_viejo,") años")

    # Numero de usuarios por ciudad
    # Almacenamos las ciudades
    # Se pueden identificar porque cada una de estas contiene un salto de linea al final
    ciudades = []
    for i in texto:
        if "\n" in i:
            ciudades.append(i)

    # Contar cuantas veces se repite cada ciudad
    # Eliminamos los duplicados
    ciudades_unicas = []
    for i in ciudades:
        if i not in ciudades_unicas:
            ciudades_unicas.append(i)

    print("Usuarios por ciudad: ")
    usuarios_mayor = 0
    usuarios_por_ciudad = []
    for i in ciudades_unicas:
        repeticiones_ciudad = []
        contador = 0
        for j in ciudades:
            # Quitamos los saltos de linea para mostrar cada registro en su propia linea
            j = str(j).rstrip()
            i = str(i).rstrip()
            # Comparamos los elementos en el bucle, para aumentar el contador en caso de que sean iguales
            if i == j:
                repeticiones_ciudad.append(i)
                contador += 1
        # Mostramos los resultados en consola
        print("- ", end ="")
        print(i, end="")
        usuarios_por_ciudad.append(i)
        print(": ", end="")
        print(len(repeticiones_ciudad))
        usuarios_por_ciudad.append(len(repeticiones_ciudad))
        if (usuarios_mayor < len(repeticiones_ciudad)):
            usuarios_mayor = len(repeticiones_ciudad)

    # Mostrar ciudad con mas usuarios
    pos_ciudad_mas_usuarios = 0
    for i in usuarios_por_ciudad:
        pos_ciudad_mas_usuarios += 1
        if i == usuarios_mayor:
            nombre_ciudad_mas_usuarios = pos_ciudad_mas_usuarios - 2
            print("Ciudad con mas usuarios: ", usuarios_por_ciudad[nombre_ciudad_mas_usuarios])
    
    resultados = [
                    "Total de usuarios: ", cantidad_usuarios, "\n",
                    "Edad promedio: ", promedio, "\n",
                    "Usuario mas joven: ", texto[nombre_mas_joven], "(",mas_joven,")"," años", "\n",
                    "Usuario mas viejo: ", texto[nombre_mas_viejo], "(",mas_viejo,")"," años", "\n",
                    "Usuarios por ciudad: ", usuarios_por_ciudad, "\n",
                    "Ciudad con mas usuarios: ", usuarios_por_ciudad[nombre_ciudad_mas_usuarios]
                ]
    return resultados

# Salvamos los resultados en un fichero de texto
def guardar_resultados(resultados):
    resultados_string = ''.join(str(x) for x in resultados)
    # Manejo de error al abrir el archivo. Se abre en modo escritura
    try:
        f = open("resultados_prueba2.txt", "w", encoding="utf-8")
    except OSError:
        print("No es posible abrir el archivo")
    with f:
        f.write(resultados_string)
    f.close()
    return

if __name__ =="__main__":
    texto = []
    datos = leer_archivo(texto)
    resultados = calcular_estadisticas(texto)
    resultados_save = guardar_resultados(resultados)
    print(resultados_save)