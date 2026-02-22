from modelos.producto import Producto


class InventarioServicio:

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        with open("inventario.txt", "w") as archivo:
            for producto in self.productos:
                linea = f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n"
                archivo.write(linea)

    def cargar_desde_archivo(self):
        try:
            with open("inventario.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")

                    id_p = int(datos[0])
                    nombre = datos[1]
                    cantidad = int(datos[2])
                    precio = float(datos[3])

                    producto = Producto(id_p, nombre, cantidad, precio)
                    self.productos.append(producto)

        except FileNotFoundError:
            open("inventario.txt", "w").close()

        except PermissionError:
            print("No tienes permisos para leer el archivo.")

        except Exception as e:
            print("Error inesperado al cargar archivo:", e)

    # ----------- AGREGAR PRODUCTO -----------
    def agregar_producto(self):
        try:
            id_p = int(input("ID: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            if self.buscar_por_id(id_p):
                print("Ya existe un producto con ese ID")
                return

            nuevo = Producto(id_p, nombre, cantidad, precio)
            self.productos.append(nuevo)
            self.guardar_en_archivo()

            print("Producto agregado correctamente")

        except ValueError:
            print("Datos ingresados invalidos")

    # ----------- LISTAR PRODUCTOS -----------
    def listar_productos(self):
        if not self.productos:
            print("No hay productos registrados")
            return

        print("\nInventario:")
        for producto in self.productos:
            print(producto)

    # ----------- BUSCAR POR ID -----------
    def buscar_por_id(self, id_p):
        for producto in self.productos:
            if producto.get_id() == id_p:
                return producto
        return None

    # ----------- BUSCAR POR NOMBRE -----------
    def buscar_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    # ----------- ACTUALIZAR PRODUCTO -----------
    def actualizar_producto(self):
        try:
            id_p = int(input("ID del producto a actualizar: "))
            producto = self.buscar_por_id(id_p)

            if not producto:
                print("Producto no encontrado")
                return

            nuevo_nombre = input("Nuevo nombre: ")
            nueva_cantidad = int(input("Nueva cantidad: "))
            nuevo_precio = float(input("Nuevo precio: "))

            producto.set_nombre(nuevo_nombre)
            producto.set_cantidad(nueva_cantidad)
            producto.set_precio(nuevo_precio)

            self.guardar_en_archivo()

            print("Producto actualizado correctamente")

        except ValueError:
            print("Datos ingresados invalidos")

    # ----------- ELIMINAR PRODUCTO -----------
    def eliminar_producto(self):
        try:
            id_p = int(input("ID del producto a eliminar: "))
            producto = self.buscar_por_id(id_p)

            if not producto:
                print("Producto no encontrado")
                return

            self.productos.remove(producto)
            self.guardar_en_archivo()

            print("Producto eliminado correctamente")

        except ValueError:
            print("Debe ingresar un ID valido")