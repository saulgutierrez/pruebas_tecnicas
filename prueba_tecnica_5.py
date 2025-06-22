class Usuario:
    def __init__(self, id, nombre, edad, email):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.email = email

class UsuarioManager:
    def __init__(self):
        self.usuarios = self.cargar_usuarios()

    def cargar_usuarios(self):
        return
    
    def guardar_usuarios(self):
        return
    
    def agregar_usuario(self, nombre, edad, email):
        return
    
    def listar_usuarios(self):
        return
    
    def buscar_por_id(self, id):
        return
    
    def actualizar_usuario(self, id, nuevo_email=None, nueva_edad=None):
        return
    
    def eliminar_usuario(self, id):
        return
    
if __name__ == "main":
    print("Hello")