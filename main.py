from membresia import Gratis, Basica, Familiar, SinConexion, Pro

def main():
    correo = input("Ingrese su correo electrónico: ")
    tarjeta = input("Ingrese su número de tarjeta: ")

    usuario = Gratis(correo, tarjeta)

    while True:
        print("\nOpciones disponibles:")
        print("1. Cambiar suscripción")
        print("2. Mostrar información de suscripción")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            print("\nSuscripciones disponibles:")
            print("1. Básica")
            print("2. Familiar")
            print("3. Sin Conexión")
            print("4. Pro")
            nueva_suscripcion = input("Ingrese el número de la nueva suscripción: ")

            if nueva_suscripcion.isdigit() and 1 <= int(nueva_suscripcion) <= 4:
                nueva_membresia = usuario.cambiar_suscripcion(int(nueva_suscripcion))
                if nueva_membresia:
                    print("Suscripción cambiada con éxito.")
                    usuario = nueva_membresia
                else:
                    print("No se puede cambiar la suscripción.")
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        elif opcion == "2":
            print("\nInformación de suscripción:")
            print(f"Correo electrónico: {usuario.correo_suscriptor}")
            print(f"Número de tarjeta: {usuario.numero_tarjeta}")
            print(f"Costo de la membresía: ${usuario.costo}")
            print(f"Cantidad máxima de dispositivos: {usuario.cantidad_max_dispositivos}")
            if hasattr(usuario, 'dias_regalo'):
                print(f"Días de regalo: {usuario.dias_regalo}")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
