
# =====================================
# SISTEMA DE LOGIN EN PYTHON
# Autora: Raquel Klepache
# =====================================

usuarios = {
    "admin": "1234",
    "raquel": "python2026"
}


def registrar_usuario():
    print("\n===== REGISTRO DE USUARIO =====")

    usuario = input("Ingresa un nombre de usuario: ")

    if usuario in usuarios:
        print("El usuario ya existe.")
        return

    contraseña = input("Ingresa una contraseña: ")

    if len(contraseña) < 4:
        print("La contraseña debe tener al menos 4 caracteres.")
        return

    usuarios[usuario] = contraseña

    print("¡Usuario registrado correctamente!")


def iniciar_sesion():
    print("\n===== INICIAR SESIÓN =====")

    intentos = 3

    while intentos > 0:

        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")

        if usuario in usuarios and usuarios[usuario] == contraseña:
            print(f"\n¡Bienvenido/a, {usuario}!")
            return

        intentos -= 1

        print("Usuario o contraseña incorrectos.")
        print(f"Intentos restantes: {intentos}")

    print("\nAcceso bloqueado. Se agotaron los intentos.")


# PROGRAMA PRINCIPAL

while True:

    print("\n===== SISTEMA DE LOGIN =====")
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Salir")

    opcion = input("\nSelecciona una opción: ")

    match opcion:

        case "1":
            iniciar_sesion()

        case "2":
            registrar_usuario()

        case "3":
            print("¡Hasta pronto!")
            break

        case _:
            print("Opción incorrecta. Intenta nuevamente.")
