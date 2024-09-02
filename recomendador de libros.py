import csv
import random


class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Puntuación: {self.puntuacion}'


lista_libros = []

with open('Libros.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)  
    for fila in lector_csv:
        titulo, autor, genero, puntuacion = fila
        puntuacion = float(puntuacion)
        libro = Libro(titulo, autor, genero, puntuacion)
        lista_libros.append(libro)
    
while True:
    print("\n¿Qué deseas hacer?")
    print("1. Agregar un nuevo libro")
    print("2. Buscar libros por género")
    print("3. Recomendar un libro")
    print("4. Sugerir un libro al azar")
    print("5. Salir")

    opcion = input("Ingresa el número de opción: ")

    if opcion == '1':
        # Agregar un libro
        titulo = input("Ingresa el título del libro: ")
        autor = input("¿Quién es el autor? ")
        genero = input("¿De qué género es? ")
        puntuacion = float(input("¿Qué puntuación le das (del 0 al 5)? "))
        libro = Libro(titulo, autor, genero, puntuacion)
        lista_libros.append(libro)
        print(f"¡Genial! El libro '{titulo}' ha sido agregado.")
           
        with open('Libros.csv', 'a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow([titulo, autor, genero, puntuacion])

    elif opcion == '2':
        # Buscar libros por género
        genero_buscar = input("¿Qué género te interesa? ")
        libros_en_genero = [libro.titulo for libro in lista_libros if libro.genero.lower() == genero_buscar.lower()]
        
        if libros_en_genero:
            print(f"Libros disponibles en el género que elegiste '{genero_buscar}':")
            for titulo in libros_en_genero:
                print(titulo)
        else:
            print(f"No encontramos libros en el género que nos indicas '{genero_buscar}'.")

    elif opcion == '3':
        # Recomendar un libro
        genero_interes = input("¿Qué genero te apetece leer? ")
        libros_en_genero = [libro for libro in lista_libros if libro.genero.lower() == genero_interes.lower()]
        
        if libros_en_genero:
            libro_recomendado = max(libros_en_genero, key=lambda libro: libro.puntuacion)
            print(f"Te puedo recomendar este libro '{libro_recomendado.titulo}' la puntuación de este libro es de {libro_recomendado.puntuacion}.")
        else:
            print(f"No encontramos libros en el género indicado '{genero_interes}'.")

    elif opcion == '4':
        # agreuge una opcion para recomendar un libro al azar
        libro_aleatorio = random.choice(lista_libros)
        print(f"¡Aquí tienes una recomendación al azar!\n{libro_aleatorio}")

    elif opcion == '5':
        print("¡No te olvides de tomar Agüita!, que tengas un excelente día!.")
        break

    else:
        print("La opción elegida no es valida. Por favor, opta por una opción del 1 al 5.")