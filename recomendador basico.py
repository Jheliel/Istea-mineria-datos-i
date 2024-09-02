import random

class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Puntuación: {self.puntuacion}'


# Lista para almacenar los objetos de la clase Libro
lista_libros = [
    Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5),
    Libro("1984", "George Orwell", "Ciencia Ficción", 4.3),
    Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7),
    Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2),
    Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4),
    Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6),
    Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8),
    Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4),
    Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)
]

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
        # Recomendar un libro con puntuación más alta
        genero_interes = input("¿Qué genero te apetece leer? ")
        libros_en_genero = [libro for libro in lista_libros if libro.genero.lower() == genero_interes.lower()]
        
        if libros_en_genero:
            libro_recomendado = max(libros_en_genero, key=lambda libro: libro.puntuacion)
            print(f"Te puedo recomendar este libro '{libro_recomendado.titulo}' la puntuación de este libro es de {libro_recomendado.puntuacion}.")
        else:
            print(f"No encontramos libros en el género indicado '{genero_interes}'.")

    elif opcion == '4':
        # agreuge una opción para recomendar un libro al azar de la lista
        libro_aleatorio = random.choice(lista_libros)
        print(f"¡Aquí tienes una recomendación al azar!\n{libro_aleatorio}")
        # Salir de la aplicación
    elif opcion == '5':
        print("¡No te olvides de tomar Agüita!, que tengas un excelente día!.")
        break

    else:
        print("La opción elegida no es valida. Por favor, opta por una opción del 1 al 5.")