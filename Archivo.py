import csv
import os

ARCHIVO = "inventario.csv"


# CREAR ARCHIVO SI NO EXISTE
def crear_archivo():

    if not os.path.exists(ARCHIVO):

        with open( ARCHIVO, "w", newline="", encoding="utf-8") as archivo:

            escritor = csv.writer(archivo)

            escritor.writerow([
                "Codigo",
                "Nombre",
                "Categoria",
                "Cantidad",
                "Unidad",
                "StockMinimo",
                "FechaIngreso",
                "Costo"
            ])


# LEER MATERIALES
def leer_materiales():

    materiales = []

    try:

        with open(
            ARCHIVO,"r", encoding="utf-8" ) as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:
                materiales.append(fila)

    except FileNotFoundError:

        print("No se encontró el archivo de inventario.")

    except Exception as e:

        print("Ocurrió un error al leer el archivo:", e)

    return materiales


# GUARDAR MATERIALES
def guardar_materiales(materiales):

    try:

        with open(
            ARCHIVO, "w", newline="", encoding="utf-8" ) as archivo:

            campos = [
                "Codigo",
                "Nombre",
                "Categoria",
                "Cantidad",
                "Unidad",
                "StockMinimo",
                "FechaIngreso",
                "Costo"
            ]

            escritor = csv.DictWriter(
                archivo,
                fieldnames=campos
            )

            escritor.writeheader()
            escritor.writerows(materiales)

    except Exception as e:

        print(
            "Ocurrió un error al guardar los datos:",
            e
        )