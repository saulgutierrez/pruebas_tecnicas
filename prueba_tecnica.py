# Estructura por defecto de un objeto tarea
tarea = {
            'id': None,
            'titulo': None, 
            'descripcion': None, 
            'estado': "Pendiente"
        }

# Lista de tareas
tareas = []

# Manejo del id de cada tarea
global contador
contador = 1

def agregar_tarea():
    global contador
    tarea["id"] = contador
    tarea["titulo"] = input("Agregue un titulo: ")
    respuesta = input("¿Desea agregar una descripcion? (S/N): ")
    if respuesta == "s":
        tarea["descripcion"] = input("Agregue una descripcion: ")
        tareas.append(tarea.copy())
        contador = contador + 1
    elif respuesta == "S":
        tarea["descripcion"] = input("Agregue una descripcion: ")
        tareas.append(tarea.copy())
        contador = contador + 1
    else:
        # Se agrega la tarea a la lista con el operador append y se actualiza el id
        tareas.append(tarea.copy())
        contador = contador + 1


def listar_tareas():
    print(tareas)

def marcar_completada():
    tarea_completada = input("Ingrese el id de la tarea completada: ")
    tarea_completada_int = int(tarea_completada)
    for item in tareas:
        # Si se encuentra el indice dado, se actualiza el campo estado
        if item["id"] == tarea_completada_int:
            item["estado"] = "Completada"
        else:
            print("El indice ingresado no existe")

def eliminar_tarea():
    tarea_eliminar = input("Ingrese el id de la tarea a eliminar: ")
    tarea_eliminar_int = int(tarea_eliminar)
    # Si se encuentra el indice dado, se realiza la operacion pop sobre la lista, para eliminar el objeto
    if tarea_eliminar_int <= len(tareas):
        tareas.pop(tarea_eliminar_int - 1)
    else:
        print("El indice ingresado no existe")

# Menu principal
def menu():
    print("Sistema de gestion de tareas pendientes")
    print("1. Agregar tarea")
    print("2. Listar todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar una tarea")
    opcion = input("Seleccione: ")

    if opcion == "1":
        agregar_tarea()
        menu()
    elif opcion == "2":
        listar_tareas()
        menu()
    elif opcion == "3":
        marcar_completada()
        menu()
    elif opcion == "4":
        eliminar_tarea()
        menu()
    else:
        print("Ingrese una opcion correcta")
        opcion = None
        menu()

if "__main__":
    menu()