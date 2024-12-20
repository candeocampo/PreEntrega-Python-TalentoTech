
# Importar la base de datos
import sqlite3

# Color
# Style.BRIGHTY es ideal para título
# Style.DIM se usa para mensajes secundarios
from colorama import init, Fore, Style
init(autoreset=True) #Inicilizado colorama

# Funcion: Crear tabla
def crear_tabla_productos():
    conexion = sqlite3.connect("base_de_datos.db")
    cursor = conexion.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Productos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT UNIQUE NOT NULL,
               descripcion TEXT NOT NULL,
               stock INTEGER NOT NULL,
               precio REAL NOT NULL,
               categoria TEXT NOT NULL)''')
    conexion.commit()
    conexion.close()
crear_tabla_productos()


## Función: Agregar productos
def agregar_producto(nombre,descripcion,stock,precio,categoria):
    datos = [nombre, descripcion, stock, precio, categoria]
    conexion = sqlite3.connect("base_de_dato.db")
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO Productos (nombre, descripcion, stock, precio, categoria) VALUES (?,?,?,?,?)", datos)
    conexion.commit()
    print(Fore.LIGHTMAGENTA_EX + f"Producto{nombre} registrado con éxito!")
    conexion.close()            

# Función: Mostrar producto
def mostrar_productos(productos = 0, producto_unico = False):
    if productos == 0:
        conexion = sqlite3.connect("base_de_datos.db")
        cursor = sqlite3.cursor()
        cursor.execute("SELECT * FROM Productos") # Seleccionamos la tabla
        resultados = cursor.fetchall()
        for registro in resultados:
            print("ID:", registro[0],
                  "Nombre:", registro[1],
                  "Descripcion:", registro[2],
                  "Stock:",registro[3],
                  "Precio:", registro[4],
                  "Categoria:", registro[5])
        conexion.close()
    else:
        if producto_unico:
            print("ID:", registro[0],
                  "Nombre:", registro[1],
                  "Descripcion:", registro[2],
                  "Stock:",registro[3],
                  "Precio:", registro[4],
                  "Categoria:", registro[5])
        else:
            for registro in productos:
                print("ID:", registro[0],
                  "Nombre:", registro[1],
                  "Descripcion:", registro[2],
                  "Stock:",registro[3],
                  "Precio:", registro[4],
                  "Categoria:", registro[5])





# Función: Buscar Producto
def buscar_producto():
    nombre = input("Ingrese nombre del producto: ").capitalize()
    conexion = sqlite3.connect("base_de_datos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Productos WHERE nombre = ?",(nombre,))

    resultados = cursor.fetchone()
    if resultados != None:
        mostrar_productos(resultados,True)
    else:
        print("Registro de producto no encontrado.")
    conexion.close()

# Funcion: Mostrar Menu Iteractivo
def mostrar_menu():
    print(" ___________________________________________")
    print("|        Menú de Gestión de Productos       |")
    print("|-------------------------------------------|")
    print("| 1. Agregar Producto.                      |")
    print("| 2. Consulta de Datos de Productos.        |")
    print("| 3. Modificar la Cantidad de Stock.        |")
    print("| 4. Dar de Baja.                           |")
    print("| 5. Listado Completo de Productos.         |")
    print("| 6. Lista de Productos con Cantidad Baja.  |")
    print("| 7. Salir.                                 |")
    print(" ___________________________________________")

def main():
    menu = True
    while menu:
        mostrar_menu()
        opcion = input("Ingrese opcion: ")
        ## Opcion 1: Registrar Producto
        if opcion == "1":
            nombre = input("Ingrese Nombre del Producto: ").capitalize()
            descripcion = input("Descripcion: ").capitalize()            
            stock = 0
            while stock <= 0:
                try:
                    stock = int(input("Cantidad de Stock: "))
                    if stock <=0:
                        print(estilo_aviso + "Por favor, ingrese un numero mayor que 0.")
                except ValueError:
                    print(estilo_aviso + "Ingrese un numero")
                    stock = 0
            precio = 0
            while precio <= 0:
                try:
                    precio = int(input("Precio del Producto: "))
                    if precio <=0:
                        print(estilo_aviso + "Por favor, ingrese un numero mayor que 0.")
                except ValueError:
                    print(estilo_aviso + "Ingrese un numero")
                    precio = 0
            categoria = input("Ingrese la Categoria del Producto: ").capitalize()
            agregar_producto(nombre, descripcion, stock, precio, categoria)
            print("Productos agregados exitosamente!\n")
        ## Opcion 2: mostrar productos
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            reporte_bajo_stock()
        elif opcion == "6":
            buscar_producto_por_nombre()
        elif opcion == "7":
            menu = False
        else:
            print(estilo_alerta +"¡Error! Por favor, ingrese una opcion válida.\n")  





# Funciones a convocar:
# agregar_producto("Prueba2", "Bebida para hidratarse", 10, 10.50, "Bebida")
# mostrar_productos()
# actualizar_producto()
# eliminar_producto()
# reporte_bajo_stock()
# reporte_bajo_stock()
# buscar_producto_por_nombre()
main()
