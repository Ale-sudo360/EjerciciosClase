def Edad(aa,an):
    e=aa-an
    print(f"Tienes {e} años.")
    print("Adivinamos tu edad solo sabiendo el año de nacimiento")
    an=int(input("En que año nacistes: "))
    Edad(2025,an)
