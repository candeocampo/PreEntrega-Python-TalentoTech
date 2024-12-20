import sqlite3 # Importo modulo de sqlite3.
from colorama import init, Fore, Style, Back

init(autoreset=True) # Inicializo el colorama.

# Crear la tabla de productos
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
           categoria TEXT NOT NULL
        )''')
    conexion.commit()
    conexion.close()
crear_tabla_productos()

# Abstracción para validar numeros positivos.
def validar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print(Style.BRIGHT + Fore.BLUE + "Por favor, ingrese un número mayor que 0.")
        except ValueError:
            print(Style.BRIGHT + Fore.BLUE + "Ingrese un número válido.")

# Opcion 1: Agregar un producto
def agregar_producto(nombre, descripcion, stock, precio, categoria):
    datos = [nombre, descripcion, stock, precio, categoria]
    conexion = sqlite3.connect("base_de_datos.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO Productos (nombre, descripcion, stock, precio, categoria) VALUES (?, ?, ?, ?, ?)", datos)
        conexion.commit()
        print(Style.BRIGHT + Fore.GREEN + f"Producto '{nombre}' registrado con éxito!")
    except sqlite3.IntegrityError:
        print(Fore.RED + "Error: Ya existe un producto con ese nombre.")
    finally:
        conexion.close()

# Opcion 2: Mostrar productos
def mostrar_productos(productos=None, producto_unico=False):
    if productos is None:
        conexion = sqlite3.connect("base_de_datos.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Productos")
        resultados = cursor.fetchall()
        conexion.close()
    else:
        resultados = productos if not producto_unico else [productos]

    if resultados:
        for registro in resultados:
            print(f"ID: {registro[0]}, Nombre: {registro[1]}, Descripción: {registro[2]}, Stock: {registro[3]}, Precio: {registro[4]}, Categoría: {registro[5]}")
    else:
        print(Fore.RED + "No se encontraron productos.")

# Opcion 3: Buscar producto por ID
def buscar_producto():
    id_producto = validar_numero("Ingrese número de ID del Producto: ")
    conexion = sqlite3.connect("base_de_datos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Productos WHERE id = ?", (id_producto,))
    resultado = cursor.fetchone()
    conexion.close()
    if resultado:
        mostrar_productos(resultado, True)
    else:
        print(Fore.RED + "Producto no encontrado.")

# Opcion 4: Actualizar producto
def actualizar_producto():
    mostrar_productos()
    id_producto = validar_numero("Ingrese el ID del producto que desea modificar: ")
    nombre = input("Ingrese el nuevo nombre del Producto: ").capitalize()
    descripcion = input("Descripción: ").capitalize()
    stock = validar_numero("Ingrese cantidad de Stock: ")
    precio = validar_numero("Precio: ")
    categoria = input("Categoría: ").capitalize()

    conexion = sqlite3.connect("base_de_datos.db")
    cursor = conexion.cursor()
    cursor.execute('''UPDATE Productos SET nombre = ?, descripcion = ?, stock = ?, precio = ?, categoria = ? WHERE id = ?''',
                   (nombre, descripcion, stock, precio, categoria, id_producto))
    conexion.commit()
    conexion.close()
    print(Style.BRIGHT + Fore.GREEN + "Producto actualizado con éxito!")
    mostrar_productos()

# Opcion 5: Eliminar producto
def eliminar_producto():
    mostrar_productos()
    id_producto = validar_numero("Ingrese ID del Producto que desea eliminar: ")
    conexion = sqlite3.connect("base_de_datos.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Productos WHERE id = ?", (id_producto,))
    if cursor.rowcount > 0:
        print(Style.BRIGHT + Fore.GREEN + "Producto eliminado exitosamente.")
    else:
        print(Fore.RED + "Error: Producto no encontrado.")
    conexion.commit()
    conexion.close()

# Opcion 6: Mostrar productos con bajo stock
def productos_de_bajo_stock():
    valor_bajo = validar_numero("Ingrese la cantidad mínima de stock: ")
    conexion = sqlite3.connect("base_de_datos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Productos WHERE stock <= ?", (valor_bajo,))
    resultados = cursor.fetchall()
    conexion.close()
    if resultados:
        mostrar_productos(resultados)
    else:
        print(Fore.RED + "No hay productos con stock bajo.")

# Menú principal
def mostrar_menu():
    print(Style.BRIGHT + Fore.GREEN +             " ___________________________________________")
    print(Back.WHITE + Style.BRIGHT + Fore.GREEN +"|        Menú de Gestión de Productos       |")
    print(Style.BRIGHT + Fore.CYAN  +             "|-------------------------------------------|")
    print(Style.BRIGHT + Fore.CYAN  +             "| 1. Agregar Producto.                      |")
    print(Style.BRIGHT + Fore.CYAN  +             "| 2. Buscar Producto.                       |")
    print(Style.BRIGHT + Fore.CYAN  +             "| 3. Actualizar Producto.                   |")
    print(Style.BRIGHT + Fore.CYAN  +             "| 4. Eliminar Producto.                     |")
    print(Style.BRIGHT + Fore.CYAN  +             "| 5. Mostrar Productos.                     |")
    print(Style.BRIGHT + Fore.CYAN  +             "| 6. Productos con Bajo Stock.              |")
    print(Style.BRIGHT + Fore.RED   +             "| 7. Salir.                                 |")
    print(Style.BRIGHT + Fore.CYAN  +             " ___________________________________________")

def main():
    while True:
        mostrar_menu()
        opcion = input(Style.BRIGHT + Fore.CYAN + "Ingrese opción: ")
        if opcion == "1":
            nombre = input("Ingrese Nombre del Producto: ").capitalize()
            descripcion = input("Descripción: ").capitalize()
            stock = validar_numero("Cantidad de Stock: ")
            precio = validar_numero("Precio del Producto: ")
            categoria = input("Categoría del Producto: ").capitalize()
            agregar_producto(nombre, descripcion, stock, precio, categoria)
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            mostrar_productos()
        elif opcion == "6":
            productos_de_bajo_stock()
        elif opcion == "7":
            print(Style.BRIGHT + Fore.GREEN + "Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print(Fore.RED + "¡Error! Por favor, ingrese una opción válida.")

main()