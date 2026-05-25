import random
import string


def generar_password(longitud=12):
    caracteres = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password


def evaluar_password(password):
    puntuacion = 0

    if len(password) >= 12:
        puntuacion += 1

    if any(c.islower() for c in password):
        puntuacion += 1

    if any(c.isupper() for c in password):
        puntuacion += 1

    if any(c.isdigit() for c in password):
        puntuacion += 1

    if any(c in string.punctuation for c in password):
        puntuacion += 1

    niveles = {
        1: "Muy débil",
        2: "Débil",
        3: "Aceptable",
        4: "Fuerte",
        5: "Muy fuerte"
    }

    return niveles.get(puntuacion, "Muy débil")