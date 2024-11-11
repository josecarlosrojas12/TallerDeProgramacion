from db import conectar

def agregar_contacto():
    id_usuario = input("Ingrese el ID del usuario: ")
    id_contacto_usuario = input("Ingrese el ID del contacto: ")

    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO Contactos (id_usuario, id_contacto_usuario) VALUES (%s, %s)"
    datos = (id_usuario, id_contacto_usuario)
    cursor.execute(query, datos)
    conexion.commit()
    print("Contacto agregado con éxito.")
    conexion.close()

def listar_contactos():
    id_usuario = input("Ingrese el ID del usuario para listar sus contactos: ")

    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM Contactos WHERE id_usuario=%s"
    cursor.execute(query, (id_usuario,))
    contactos = cursor.fetchall()
    for contacto in contactos:
        print(contacto)
    conexion.close()
