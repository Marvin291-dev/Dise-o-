Registrar = {}
while True:
    print(f"Bienvenido")
    print("1. Registrar Cinepolis")
    print("2. Editar")
    print("3. Eliminar")
    print("4. Buscar")
    print("5. Salir")

    opcion = int(input("Ingrese una opción"))
    if opcion == "1":
        Cantidad = int(input("Ingrese la cantidad de Persona"))
        for i in range(Cantidad):
            print(f"\Cinepolis {i + 1}")
            Codigo = int(input("Ingrese el codigo de la persona"))
            Nombre = input("Ingrese el nombre")
            Apellido = input("Ingrese el apellido")
            Edad = int(input("Ingrese la edad de la persona 15/06/2009"))
