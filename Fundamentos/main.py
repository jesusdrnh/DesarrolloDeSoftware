# Archivo base que llama a los demás archivos

import os

# Lista de archivos a ejecutar
archivos = [
    "01_HolaMundo.py",
    "02_VariablesYTiposDeDatos.py",
    "03_Operadores.py",
    "04_EstructurasDeControl.py",
    "05_FuncionesYMetodos.py",
    "06_Arreglos.py",
    "07_CadenasDeConversion.py",
    "08_ClasesYObjetos.py"
]

# Ruta base
ruta_base = os.path.dirname(__file__)

# Ejecutar cada archivo
for archivo in archivos:
    print(f"\n--- Ejecutando {archivo} ---")
    ruta_completa = os.path.join(ruta_base, archivo)
    with open(ruta_completa, "r", encoding="utf-8") as f:  # Especificar la codificación
        codigo = f.read()
        exec(codigo)