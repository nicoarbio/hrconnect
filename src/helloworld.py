from hrconnect.menu.Menu import Menu
from src.hrconnect.users.model.User import User


class HelloWorld:
    def __init__(self):
        print("1 HelloWorld class created")
        pass

    def print_hello(self):
        return print("2 Hello, World!")


    @staticmethod
    def static_method():
        print("3 Este es un método estático")


# Crear una instancia de la clase HelloWorld
hello = HelloWorld()

# Llamar al método print_hello para imprimir el mensaje
hello.print_hello()

HelloWorld.static_method()

# Ejemplo de uso
usuario = User("usuario@example.com", "contraseña123", "2024-03-18 15:30:00", False, 12345)
print(usuario)
# print(usuario.email)
print(usuario.get_email())

menu = Menu()
menu.start()

# numero = input("Ingrese un número (ingrese 'q' para volver al menú principal): ")
# try:
#     numero = int(numero)
#     print(f"Número ingresado: {numero}")
# except ValueError:
#     print("Por favor, ingrese un número válido.")
