# AUTENTICACION
def login():
    # Usuario de prueba
    usuario = {
        "nombre": "Nicole",
        "saldo": 1000.0
    }
    return usuario


# CONSULTA DE SALDO
def consultar_saldo(usuario):
    """
    Muestra el saldo actual del usuario en pantalla.
    """
    print("\n" + "="*30)
    print(f"TITULAR: {usuario['nombre']}")
    print(f"SALDO DISPONIBLE: ${usuario['saldo']:.2f}")
    print("="*30)


# TRANSACCIONES
def retirar(usuario):
    pass


def depositar(usuario):
    pass


# mostrar historial
def mostrar_historial():
    pass


# menu
def menu(usuario):

    while True:

        print("\n===== CAJERO AUTOMATICO =====")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Ver historial")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_saldo(usuario)

        elif opcion == "2":
            retirar(usuario)

        elif opcion == "3":
            depositar(usuario)

        elif opcion == "4":
            mostrar_historial()

        elif opcion == "5":
            print("Gracias por usar el cajero")
            break

        else:
            print("Opción inválida")


# ================= MAIN =================

def main():

    usuario = login()

    if usuario:
        menu(usuario)


if _s_name__ == "__main__":
    main()
