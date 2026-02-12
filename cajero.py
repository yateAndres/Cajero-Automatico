# AUTENTICACION
def login():
    pass


# CONSULTA DE SALDO
def consultar_saldo():
    pass


# TRANSACCIONES
def retirar():
    pass

def depositar():
    pass


def main():
    pass

#  mostrar_historial
def  mostrar_historial():
    pass


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
            mostrar_historial()   # TU MODULO
        elif opcion == "5":
            print("Gracias por usar el cajero")
            break
        else:
            print("Opción inválida")


# ================== MAIN ==================

def main():
    usuario = login()
    if usuario:
        menu(usuario)


main()