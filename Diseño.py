Cartelera = {}

while True:
    print(f"Bienvenido")
    print("1. Registrar Película")
    print("2. Editar Película")
    print("3. Eliminar Película")
    print("4. Buscar Película")
    print("5. Salir")

    opcion = int(input("Ingrese una opción"))

    if opcion == "1":
        Codigo = input("Ingrese el código de la película")
        if Codigo in Cartelera:
            print("Este código de la película ya existe")
        else:
            Titulo = input("Ingrese el nombre de la película: ")
            Genero = input("Ingrese el genero de la película: ")
            Duracion = input("Ingrese la duración de la película (Minutos): ")
            Clasificacion = input("Ingrese la clasificacion (Ej: PG-13): ")
            Cartelera[Codigo] = {
                "Titulo": Titulo,
                "Genero": Genero,
                "Duracion": Duracion,
                "Clasificacion": Clasificacion
            }
            print(f'Película "{Titulo}" agregada con código "{Codigo}".')
    elif opcion == "2":
        Codigo = input("Ingrese el código para editar la película: ")
        if Codigo in Cartelera:
            print("Datos actuales: ", Cartelera[Codigo])
            Titulo = input("Ingrese el nuevo nombre: ")
            Genero = input("Ingrese el nuevo genero: ")
            Duracion = input("Ingrese la nueva duración (Minutos): ")
            Clasificacion = input("Ingrese la clasificación (Ej: PG-13): ")
            Cartelera[Codigo] = {
                "Titulo": Titulo,
                "Genero": Genero,
                "Duracion": Duracion,
                "Clasificacion": Clasificacion
            }
            print(f'Película con código "{Codigo}" actualizada.')
        else:
            print("Codigo de la película no existe")
    elif opcion == "3":
        Codigo = input("Ingrese la película que desea eliminar: ")
        if Codigo in Cartelera:
            Titulo = Cartelera[Codigo]["Titulo"]
            del Cartelera[Codigo]
            print(f'Película "{Titulo}" eliminada de la cartelera.')
        else:
            print("El código de la película no encontrado")

    elif opcion == "4":
        print("Cartelera")
        if not Cartelera:
            print("No hay película registrada.")
        else:
            for Codigo, Datos in Cartelera.items():
                print(f"Codigo: {Codigo}")
                for clave, valor in Datos.items():
                    print(f"{clave}: {valor}")
    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Intente de nuevo.")
