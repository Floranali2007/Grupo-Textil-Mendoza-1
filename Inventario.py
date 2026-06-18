from datetime import datetime
from Archivo import leer_materiales, guardar_materiales


# REGISTRAR MATERIAL
def registrar_material():

    print("\n--- REGISTRAR MATERIAL ---")

    materiales = leer_materiales()

    codigo = input("Código: ").strip()

    if codigo == "":
        print("El código no puede estar vacío.")
        return

    for material in materiales:

        if material["Codigo"] == codigo:

            print("Ese código ya existe.")
            return

    nombre = input("Nombre: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    categoria = input("Categoría: ").strip()

    if categoria == "":
        print("La categoría no puede estar vacía.")
        return

    try:

        cantidad = float(
            input("Cantidad: ")
        )

        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
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

    unidad = input("Unidad: ").strip()

    if unidad == "":
        print("La unidad no puede estar vacía.")
        return

    fecha = datetime.now().strftime("%d/%m/%Y")

    nuevo = {

        "Codigo": codigo,
        "Nombre": nombre,
        "Categoria": categoria,
        "Cantidad": cantidad,
        "Unidad": unidad,
        "StockMinimo": stock_minimo,
        "FechaIngreso": fecha

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


# REGISTRAR CONSUMO
def registrar_consumo():

    print("\n--- REGISTRAR CONSUMO ---")

    nombre = input(
        "Nombre del material: "
    ).lower().strip()

    if nombre == "":
      print("Debe ingresar un nombre.")
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

                cantidad_actual = float(
                    material["Cantidad"]
                )

                if consumo > cantidad_actual:

                    print(
                        "No hay suficiente stock."
                    )
                    return

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

                material["Cantidad"] = (
                    float(material["Cantidad"])
                    + ingreso
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