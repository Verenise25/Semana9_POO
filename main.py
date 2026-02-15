# ============================================
# SISTEMA PRINCIPAL
# Inventario App
# ============================================

from servicios.inventario_servicio import InventarioServicio


def mostrar_menu():
    print("""
=================================
       SISTEMA DE INVENTARIO
=================================
1. Agregar producto
2. Listar productos
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
0. Salir
=================================
""")


def main():

    servicio = InventarioServicio()

    while True:

        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                servicio.agregar_producto()

            elif opcion == 2:
                servicio.listar_productos()

            elif opcion == 3:
                nombre = input("Nombre a buscar: ")
                resultados = servicio.buscar_por_nombre(nombre)

                if resultados:
                    for producto in resultados:
                        print(producto)
                else:
                    print("No se encontraron coincidencias")

            elif opcion == 4:
                servicio.actualizar_producto()

            elif opcion == 5:
                servicio.eliminar_producto()

            elif opcion == 0:
                print("Saliendo del sistema...")
                break

            else:
                print("Opcion invalida")

        except ValueError:
            print("Debe ingresar un numero valido")


if __name__ == "__main__":
    main()