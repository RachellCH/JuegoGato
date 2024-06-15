def contar_letras_y_espacios(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            letras = sum(c.isalpha() for c in contenido)
            espacios = sum(c.isspace() for c in contenido)
            return letras, espacios
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return None, None

def generar_resumen(nombre_archivo_entrada, nombre_archivo_salida):
    letras, espacios = contar_letras_y_espacios(nombre_archivo_entrada)
    if letras is not None and espacios is not None:
        with open(nombre_archivo_salida, 'w') as archivo_salida:
            archivo_salida.write(f"Cantidad de letras: {letras}\n")
            archivo_salida.write(f"Cantidad de espacios: {espacios}\n")

if __name__ == "__main__":
    archivo_entrada = input("Ingrese el nombre del archivo de entrada (.txt): ")
    archivo_salida = input("Ingrese el nombre del archivo de salida para el resumen (.txt): ")

    generar_resumen(archivo_entrada, archivo_salida)
    print("Resumen generado con éxito.")
