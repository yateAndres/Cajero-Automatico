# AUTENTICACION

def modulo_seguridad():
    """
    Responsabilidad: Validar la identidad del usuario.
    Retorna: True si el PIN es correcto, False si se agotan los intentos.
    """
    pin_secreto = "1234"
    intentos_maximos = 3
    
    print("=== SISTEMA DE SEGURIDAD BANCARIA ===")
    
    for intento_actual in range(1, intentos_maximos + 1):
        pin_ingresado = input(f"Intento {intento_actual}/{intentos_maximos} - Ingrese su PIN: ")
        
        if pin_ingresado == pin_secreto:
            print("\n Verificación exitosa. Cargando sistema...")
            return True
        else:
            print("PIN incorrecto.")

    print("\nALERTA Demasiados intentos fallidos. Cuenta bloqueada.")
    return False

if __name__ == "__main__":
        if modulo_seguridad():
            print("Continuar al Menú Principal...")
        else:
            print("Saliendo del programa.")

# CONSULTA DE SALDO
def consultar_saldo():
    pass


# TRANSACCIONES
def retirar():
    pass

def depositar():
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


# ================== MAIN ==================
def main():
    usuario = login()
    if usuario:
        menu(usuario)


if __name__ == "__main__":
    main()