from logica import generar_password, evaluar_password


def main():
    password = generar_password(14)

    print("Contraseña generada:", password)
    print("Nivel de seguridad:", evaluar_password(password))


if __name__ == "__main__":
    main()