from datetime import datetime
from Archivo import leer_materiales, guardar_materiales


# REGISTRAR MATERIAL
def registrar_material():

    print("\n--- REGISTRAR MATERIAL ---")

    materiales = leer_materiales()

    codigo = f"MAT{len(materiales)+1:03d}"
    print("Código generado:", codigo)
    nombre = input("Nombre: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return
    
    if not nombre.replace(" ", "").isalpha():

        print("Solo se permiten letras.")
        return
    for material in materiales:

        if material["Nombre"].lower() == nombre.lower():

             print("El material ya se encuentra registrado.")
             return
    print("\nCategorías disponibles:")
    print("1. Tela")
    print("2. Tinta")
    print("3. Vinil")
    print("4. Papel")
    print("5. Accesorio")

    opcion_categoria = input("Seleccione una categoría: ")

    if opcion_categoria == "1":
        categoria = "Tela"

    elif opcion_categoria == "2":
          categoria = "Tinta"

    elif opcion_categoria == "3":
         categoria = "Vinil"

    elif opcion_categoria == "4":
         categoria = "Papel"

    elif opcion_categoria == "5":
         categoria = "Accesorio"

    else:
     print("Categoría inválida.")
     return

    try:

        cantidad = float(
            input("Cantidad: ")
        )

        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return
        if cantidad > 300:
            print("La cantidad no puede ser mayor a 300.")
            return

        stock_minimo = float(
            input("Stock mínimo: ")
        )

        if stock_minimo < 0:
            print("El stock mínimo no puede ser negativo.")
            return

    except ValueError:

        print("Debe ingresar números.")
        return
    print("\nUnidades disponibles:")
    print("1. Metros")
    print("2. Kilogramos")
    print("3. Mililitros")
    print("4. Unidades")
    print("5. Litros")
    print("6. Rollos")

    opcion_unidad = input("Seleccione una unidad: ")

    if opcion_unidad == "1":
         unidad = "Metros"

    elif opcion_unidad == "2":
         unidad = "Kilogramos"

    elif opcion_unidad == "3":
         unidad = "Mililitros"

    elif opcion_unidad == "4":
         unidad = "Unidades"
    elif opcion_unidad == "5":
         unidad = "Litros"
    elif opcion_unidad == "6":
         unidad = "Rollos"

    else:
     print("Unidad inválida.")
     return

    fecha = datetime.now().strftime("%d/%m/%Y")

    nuevo = {

        "Codigo": codigo,
        "Nombre": nombre,
        "Categoria": categoria,
        "Cantidad": cantidad,
        "Unidad": unidad,
        "StockMinimo": stock_minimo,
        "FechaIngreso": fecha,
        "Costo": ""

    }

    materiales.append(nuevo)

    guardar_materiales(materiales)

    print("Material registrado correctamente.")

# BUSCAR MATERIAL
def buscar_material():

    print("\n--- BUSCAR MATERIAL ---")

    nombre_buscar = input(
        "Nombre del material: "
    ).lower().strip()

    if nombre_buscar == "":
        print("Debe ingresar un nombre.")
        return
    if not nombre_buscar.replace(" ", "").isalpha():
         print("Solo se permiten letras.")
         return

    materiales = leer_materiales()

    encontrado = False

    for material in materiales:

        if material["Nombre"].lower() == nombre_buscar:

            print("\nMaterial encontrado")

            print("Código:", material["Codigo"])
            print("Nombre:", material["Nombre"])
            print("Categoría:", material["Categoria"])
            print("Cantidad:", material["Cantidad"])
            print("Unidad:", material["Unidad"])
            print("Stock mínimo:", material["StockMinimo"])
            print("Fecha ingreso:", material["FechaIngreso"])

            encontrado = True

    if not encontrado:

        print("Material no encontrado.")


# ACTUALIZAR STOCK
def actualizar_stock():

    print("\n--- ACTUALIZAR STOCK ---")

    nombre = input(
        "Nombre del material: "
    ).lower().strip()
    if nombre == "":
        print("Debe ingresar un nombre.")
        return
    if not nombre.replace(" ", "").isalpha():
         print("Solo se permiten letras.")
         return

    materiales = leer_materiales()

    encontrado = False

    for material in materiales:

        if material["Nombre"].lower() == nombre:

            try:

                nueva_cantidad = float(
                    input("Nueva cantidad: ")
                )

                if nueva_cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    return
                if nueva_cantidad > 300:
                    print("La cantidad no puede ser mayor a 300.")
                    return

                material["Cantidad"] = nueva_cantidad

                encontrado = True

            except ValueError:

                print("Cantidad inválida.")
                return

    if encontrado:

        guardar_materiales(materiales)

        print("Stock actualizado correctamente.")

    else:

        print("Material no encontrado.")

# VERIFICAR STOCK MÍNIMO
def verificar_stock_minimo():

    print("\n--- STOCK MÍNIMO ---")

    materiales = leer_materiales()

    alerta = False

    for material in materiales:

        cantidad = float(
            material["Cantidad"]
        )

        minimo = float(
            material["StockMinimo"]
        )

        if cantidad == 0:

            alerta = True

            print(
                f"{material['Nombre']} SIN STOCK."
            )

        elif cantidad <= minimo:

            alerta = True

            print(
                f"{material['Nombre']} necesita reposición."
            )

    if not alerta:

        print(
            "No existen alertas de stock."
        )


# REGISTRAR SALIDA DE MATERIAL para confeccion
def registrar_salida_de_material_para_confeccion():

    print("\n--- REGISTRAR SALIDA PARA CONFECCIÓN ---")

    nombre = input(
        "Nombre del material: "
    ).lower().strip()

    if nombre == "":
         print("Debe ingresar un nombre.")
         return
    if not nombre.replace(" ", "").isalpha():
         print("Solo se permiten letras.")
         return
    materiales = leer_materiales()

    encontrado = False

    for material in materiales:

        if material["Nombre"].lower() == nombre:

            try:

                consumo = float(
                    input(
                        "Cantidad utilizada: "
                    )
                )

                if consumo <= 0:
                    print(
                        "La cantidad debe ser mayor a cero."
                    )
                    return
                if consumo > 300:
                     print("La cantidad utilizada no puede ser mayor a 300.")
                     return

                cantidad_actual = float(material["Cantidad"])

                if consumo > cantidad_actual:
                     print("No hay suficiente stock.")
                     return

                cantidad_actual = float(
                    material["Cantidad"]
                )

                material["Cantidad"] = (
                    cantidad_actual - consumo
                )

                encontrado = True

            except ValueError:

                print(
                    "Cantidad inválida."
                )
                return

    if encontrado:

        guardar_materiales(materiales)

        print(
            "Inventario actualizado tras confección."
        )

    else:

        print(
            "Material no encontrado."
        )

# REGISTRAR INGRESO
def registrar_ingreso():

    print("\n--- REGISTRAR INGRESO ---")

    nombre = input(
        "Nombre del material: "
    ).lower().strip()

    if nombre == "":
        print("Debe ingresar un nombre.")
        return

    if not nombre.replace(" ", "").isalpha():
        print("Solo se permiten letras.")
        return

    materiales = leer_materiales()

    encontrado = False

    for material in materiales:

        if material["Nombre"].lower() == nombre:

            try:

                ingreso = float(
                    input(
                        "Cantidad ingresada: "
                    )
                )

                if ingreso <= 0:
                    print(
                        "La cantidad debe ser mayor a cero."
                    )
                    return
                if ingreso > 300:
                    print("La cantidad ingresada no puede ser mayor a 300.")
                    return
                cantidad_actual = float(material["Cantidad"])

                if cantidad_actual + ingreso > 300:
                     print("El stock total no puede superar las 300 unidades.")
                     return

                costo = float(
                    input(
                        "Costo del ingreso: "
                    )
                )

                if costo < 0:
                    print(
                        "Costo inválido."
                    )
                    return
                if costo >1000:
                    print ("El costo no puede superar los 1000 soles.")
                    return
            except ValueError:
                print("Debe ingresar un valor numérico")
                return

            material["Cantidad"] = (
                    float(material["Cantidad"])
                    + ingreso
                )

            material["Costo"] = costo

            encontrado = True

    if encontrado:

        guardar_materiales(materiales)

        print(
            "Ingreso registrado correctamente."
        )

    else:

        print(
            "Material no encontrado."
        )

# GENERAR REPORTE
def generar_reporte():

    print("\n--- REPORTE DE INVENTARIO ---")

    materiales = leer_materiales()

    if len(materiales) == 0:

        print("No existen registros.")
        return

    for material in materiales:

        print("--------------------------------")
        print("Código:", material["Codigo"])
        print("Nombre:", material["Nombre"])
        print("Categoría:", material["Categoria"])
        print("Cantidad:", material["Cantidad"])
        print("Unidad:", material["Unidad"])
        print("Stock mínimo:", material["StockMinimo"])
        print("Fecha ingreso:", material["FechaIngreso"])


# ORDENAR INVENTARIO
def ordenar_inventario():

    print("\n--- INVENTARIO ORDENADO ---")

    materiales = leer_materiales()

    if len(materiales) == 0:

        print("No existen registros.")
        return

    materiales.sort(
        key=lambda x: float(
            x["Cantidad"]
        )
    )

    for material in materiales:

        print(
            material["Nombre"],
            "- Stock:",
            material["Cantidad"]
        )