# Calcular numero total de palabras
def total_palabras():
    global frase
    i = 0 # Iterador
    j = 1 # Contador de palabras
    if len(frase) == 0:
        print("No es posible leer entradas vacias")
        return
    
    # Quitamos los signos de puntuacion del texto
    frase_sin_puntuacion = frase.replace(".", "")
    frase_sin_puntuacion = frase.replace(",", "")
    frase_sin_puntuacion = frase.replace("¿", "")
    frase_sin_puntuacion = frase.replace("?", "")
    frase_sin_puntuacion = frase.replace("¡", "")
    frase_sin_puntuacion = frase.replace("!", "")

    for i in frase_sin_puntuacion:
        # Cada que encontramos un espacio en blanco, significa que una palabra ha terminado, por lo que podemos incrementar el contador
        if (i == " "):
            j = j + 1
    print("Total de palabras: ", j)

# Calcular numero total de caracteres, excluyendo espacios
def total_caracteres():
    global frase
    i = 0 # Iterador
    k = 0 # Contador de caracteres

    if len(frase) == 0:
        return

    for i in frase:
        # Usando continue, omitimos el caracter espacio dentro del bucle, para contar unicamente los caracteres
        if (i == " "):
            continue
        k = k + 1
    print("Total de caracteres, sin espacios: ", k)

# Numero total de oraciones
def total_oraciones():
    i = 0 # Iterador
    l = 0 # Contador de oraciones
    global frase

    if len(frase) == 0:
        return
    
    for i in frase:
        # Buscamos por los simbolos que delimitan el fin de una oracion, para aumentar el contador
        if (i == "." or i == "!" or i == "?"):
            l = l + 1
    print("Total de oraciones: ", l)

def palabra_mas_larga():
    i = 0 # Iterador
    j = 1 # Contador letras
    contador_letras = []
    global frase

    if len(frase) == 0:
        return
    
    # Quitamos los signos de puntuacion del texto
    frase_sin_puntuacion = frase.replace(".", "").replace(",", "").replace("¿", "").replace("?", "").replace("¡", "").replace("!", "")

    for i in frase_sin_puntuacion:
        # Buscamos la cantidad de letras de cada palabra, verificando si existe un espacio, para delimitar la longitud
        # La almacenamos dentro de un arreglo, e iteramos por cada letra de la oracion
        if (i == " "):
            frase_split = frase_sin_puntuacion.split(" ")
            contador_letras.append(j - 1)
            j = 0
        else:
            contador_letras.append(j)
        j = j + 1

    # Una vez que tenemos la cantidad de letras de cada palabra, buscamos la cantidad mayor, y la almacenamos.
    # Es decir, en el arreglo original, se vera algo como esto = [1, 2, 3, 4, 1, 2, 3], representando el orden de cada letra en cada palabra
    # Cuando el contador se reinicia, quiere decir que se esta contando la primera letra de una nueva palabra. El objetivo 
    # es buscar el numero mayor en el arreglo, lo que representa la longitad de la palabra mas larga
    mayor = 0
    for k in contador_letras:
        if (k >= mayor):
            mayor = k

    # Cuando tenemos la longitud de la palabra mas larga, comparamos esa longitud, con la longitud de cada palabra de la frase
    # Cuando estos valores coinciden, significa que hemos encontrado la palabra más larga. Mostramos en consola.
    for i in frase_split:
        if (len(i) == mayor):
            print("Palabra mas larga: ",i)

def palabra_mas_corta():
    i = 0 # Iterador
    menor = 9999999999999999 # Limite maximo, se utiliza para evaluar las longitudes
    global frase

    if len(frase) == 0:
        return
    
    # Quitamos los signos de puntuacion del texto
    frase_sin_puntuacion = frase.replace(".", "").replace(",", "").replace("¿", "").replace("?", "").replace("¡", "").replace("!", "")
    
    # Dividimos cada palabra de la oracion en cadenas individuales, para evaluarlas de una mejor manera
    for i in frase_sin_puntuacion:
        if (i == " "):
            frase_split = frase_sin_puntuacion.split(" ")
    
    # Recorremos cada palabra, y medimos su longitud. Si la comparamos con un valor alto, y vamos paulatinamente disminuyendo su valor,
    # nos encontraremos con el valor mas bajo de longitudes en una palabra
    for i in frase_split:
        if (len(i) <= menor):
            menor = len(i)

    # Una vez que tenemos el valor mas bajo del conjunto de palabras, buscamos a que palabra pertenece, y la mostramos en pantalla.
    for i in frase_split:
        if (len(i) == menor):
            print("Palabra mas corta: ",i)


if "__main__":
    frase = input("Ingrese una frase o parrafo: ")
    total_palabras()
    total_caracteres()
    total_oraciones()
    palabra_mas_larga()
    palabra_mas_corta()