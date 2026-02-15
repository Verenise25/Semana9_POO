# ============================================
# SERVICIO: InventarioServicio
# Gestiona las operaciones del inventario
# ============================================

from modelos.producto import Producto


class InventarioServicio:

    def __init__(self):
        self.productos = []

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
            print("Producto eliminado correctamente")

        except ValueError:
            print("Debe ingresar un ID valido")