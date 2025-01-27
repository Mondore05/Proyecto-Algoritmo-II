class Producto:
    def __init__(self, codigo, nombre, precio, stack):
        # Inicializa un nuevo producto con los atributos dados
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stack = stack

class Papeleria:
    def __init__(self):
        # Inicializa la lista de productos y el contador de productos
        self.productos = []
        self.cont = 0

    def ingresar_producto(self):
        # Pide al usuario la cantidad de productos a ingresar
        print("Ingrese la cantidad de productos a guardar")
        num_productos = int(input())
        
        for _ in range(num_productos):
            # Solicita el nombre del producto
            print("Ingrese el nombre del producto")
            nombre = input()

            # Solicita y valida el precio del producto
            print("Ingrese el precio")
            precio = float(input())
            while precio < 0:
                print("Error en precio")
                precio = float(input())

            # Solicita el código del producto
            print("Ingrese código")
            codigo = input()

            # Solicita y valida la cantidad en stock del producto
            print("Ingrese cantidad en stock")
            stack = int(input())
            while stack < 1:
                print("Datos inválidos")
                stack = int(input())

            # Crea y agrega el nuevo producto a la lista
            nuevo_producto = Producto(codigo, nombre, precio, stack)
            self.productos.append(nuevo_producto)
            self.cont += 1
            print("Producto agregado exitosamente")

        print("Volviendo al menú")

    def busqueda(self, x):
        # Busca un producto por nombre y devuelve su posición en la lista
        posicion = -1
        for i, producto in enumerate(self.productos):
            if producto.nombre == x:
                posicion = i
                break

        if posicion == -1:
            print("Producto no encontrado")
        else:
            print("Producto encontrado")
            print(f"Su posición es: {posicion}")
        return posicion

    def edicion(self, buscar):
        # Edita un producto existente
        posicion = self.busqueda(buscar)
        if posicion == -1:
            print("Producto no encontrado")
            return

        producto = self.productos[posicion]
        print(f"Producto encontrado: {producto.nombre}, {producto.codigo}, {producto.precio}, {producto.stack}")
        
        # Solicita los nuevos datos del producto
        print("Ingrese el nombre del nuevo producto")
        producto.nombre = input()
        
        print("Ingrese existencias")
        producto.stack = int(input())
        while producto.stack < 1:
            print("Ingrese una cantidad válida")
            producto.stack = int(input())

        print("Ingrese precio")
        producto.precio = float(input())
        while producto.precio < 1:
            print("Ingrese un precio válido")
            producto.precio = float(input())

        print("Ingrese código")
        producto.codigo = input()

    def listado_productos(self):
        # Muestra todos los productos en la lista
        for i, producto in enumerate(self.productos, start=1):
            print(f"Producto número: {i}")
            print(f"Nombre: {producto.nombre}")
            print(f"Precio: {producto.precio}")
            print(f"Codigo: {producto.codigo}")
            print(f"Cantidad: {producto.stack}")

    def menu(self):
        # Muestra el menú y gestiona las opciones seleccionadas por el usuario
        while True:
            print("Bienvenido, ¿qué operación desea realizar?")
            print("1: Ingresar Producto")
            print("2: Buscar Producto")
            print("3: Editar Producto")
            print("4: Mostrar todos los productos")
            print("5: Salir")
            opc1 = int(input())

            while opc1 < 1 or opc1 > 5:
                print("Lo siento, intente de nuevo")
                opc1 = int(input())

            if opc1 == 1:
                self.ingresar_producto()
            elif opc1 == 2:
                print("Ingrese el nombre del producto a buscar")
                nombre = input()
                self.busqueda(nombre)
            elif opc1 == 3:
                print("Ingrese el nombre del producto a editar")
                nombre = input()
                self.edicion(nombre)
            elif opc1 == 4:
                self.listado_productos()
            elif opc1 == 5:
                print("Gracias por usar nuestros servicios")
                break


papeleria = Papeleria()
papeleria.menu()