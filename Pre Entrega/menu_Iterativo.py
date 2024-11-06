
print("Bienvenido!")
local=str(input("Ingrese nombre de su local: "))

condicion = True

productos=[] #Lista de productos

while condicion:
    print(f"\nInventario de: {local}")
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

    # solicitar la opcion deseada al usuario
    opcion = int(input("Ingrese opcion:"))

    if opcion == 1:
        n = 0 
        cantidad=int(input("¿Cuantos productos desea agregar?: "))
        while n < cantidad:
            # solicitar datos del producto
            prod=str(input("Nombre del Producto: "))
            stock=int(input("Cantidad de Stock: "))
            
            producto={"Nombre": prod, "Stock": stock}
            productos.append(producto)
            n +=1

        print("Productos agregados exitosamente!\n")

    elif opcion == 2:
        print("Proximamente disponible..")
    elif opcion == 3:
        print("Proximamente disponible..")
    elif opcion == 4:
        print("Proximamente disponible..")
    elif opcion == 5:
        print("PRODUCTO   |  STOCK")
        i = 0

        while i < len(productos):
            producto = productos[i]
            print(f"\b{producto['Nombre']}    |   {producto['Stock']}") 
            i +=1

    elif opcion == 6:
        print("Proximamente disponible..")
    elif opcion == 7:
        print("Salida exitosa!")
        condicion = False
    else:
        print("¡Error! Por favor, ingrese una opcion válida.")