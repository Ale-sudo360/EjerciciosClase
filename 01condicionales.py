import math

def volumen_esfera(radio):
    """Calcula el volumen de una esfera dado su radio."""
    return (4/3) * math.pi * radio**3

def volumen_cilindro(radio, altura):
    """Calcula el volumen de un cilindro dado su radio y altura."""
    return math.pi * radio**2 * altura

# Ejemplo de uso
if __name__ == "__main__":
    radio_esfera = float(input("Introduce el radio de la esfera: "))
    print(f"El volumen de la esfera es: {volumen_esfera(radio_esfera):.2f}")

    radio_cilindro = float(input("Introduce el radio del cilindro: "))
    altura_cilindro = float(input("Introduce la altura del cilindro: "))
    print(f"El volumen del cilindro es: {volumen_cilindro(radio_cilindro, altura_cilindro):.2f}")