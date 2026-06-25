from Archivo import crear_archivo
from Inventario import *

# Crear archivo CSV al iniciar el programa
crear_archivo()

# MENÚ PRINCIPAL

while True:

    print("\n====================================")
    print("   SISTEMA DE INVENTARIO TEXTIL")
    print("        TEXTILERÍA MENDOZA")
    print("====================================")
    print("1. Registrar material")
    print("2. Buscar material")
    print("3. Actualizar stock")
    print("4. Verificar stock mínimo")
    print("5. Registrar salida de material para confección")
    print("6. Registrar ingreso")
    print("7. Generar reporte")
    print("8. Ordenar inventario")
    print("9. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":

        registrar_material()

    elif opcion == "2":

        buscar_material()

    elif opcion == "3":

        actualizar_stock()

    elif opcion == "4":

        verificar_stock_minimo()

    elif opcion == "5":

        registrar_salida_de_material_para_confeccion()

    elif opcion == "6":

        registrar_ingreso()

    elif opcion == "7":

        generar_reporte()

    elif opcion == "8":

        ordenar_inventario()

    elif opcion == "9":

        print("\nGracias por utilizar el sistema.")
        break

    else:

        print("\nOpción inválida. Intente nuevamente.")