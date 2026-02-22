# Inventario App

Sistema de gestión de inventario desarrollado en Python.  
Permite agregar, listar, buscar, actualizar y eliminar productos.  

## Funcionalidades

- Guardar productos en un archivo `inventario.txt` para mantener persistencia.  
- Cargar productos automáticamente al iniciar el sistema.  
- Manejo de errores básicos de archivos (`FileNotFoundError`, `PermissionError`).  
- Interfaz de usuario simple en consola con menú interactivo.

## Cómo usar

1. Ejecutar el archivo principal: `python main.py`  
2. Elegir opciones del menú:  
   - 1 → Agregar producto  
   - 2 → Listar productos  
   - 3 → Buscar producto  
   - 4 → Actualizar producto  
   - 5 → Eliminar producto  
   - 0 → Salir
3. Todos los cambios se guardan automáticamente en `inventario.txt`.
