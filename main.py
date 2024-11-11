from usuarios import *
from chats import *
from mensajes import *
from contactos import *

def menu():
    print("\n--- Menú Principal ---")
    print("1. Crear Usuario")
    print("2. Listar Usuarios")
    print("3. Actualizar Usuario")
    print("4. Eliminar Usuario")
    print("5. Crear Chat")
    print("6. Listar Chats")
    print("7. Crear Mensaje")
    print("8. Listar Mensajes")
    print("9. Agregar Contacto")
    print("10. Listar Contactos")
    print("0. Salir")

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            actualizar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            crear_chat()
        elif opcion == "6":
            listar_chats()
        elif opcion == "7":
            crear_mensaje()
        elif opcion == "8":
            listar_mensajes()
        elif opcion == "9":
            agregar_contacto()
        elif opcion == "10":
            listar_contactos()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
