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
                "FechaIngreso"
            ])


# LEER MATERIALES
def leer_materiales():

    materiales = []

    with open(
        ARCHIVO,
        "r",
        encoding="utf-8"
    ) as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:
            materiales.append(fila)

    return materiales


# GUARDAR MATERIALES
def guardar_materiales(materiales):

    with open(
        ARCHIVO, "w", newline="", encoding="utf-8") as archivo:

        campos = [
            "Codigo",
            "Nombre",
            "Categoria",
            "Cantidad",
            "Unidad",
            "StockMinimo",
            "FechaIngreso"
        ]

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos
        )

        escritor.writeheader()
        escritor.writerows(materiales)