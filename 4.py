nombres = []

continuar = True

while continuar:
    nombre = input("Ingresa un nombre (FIN para terminar): ").strip()

    if nombre == "FIN":
        continuar = False
    elif nombre == "":
        print("Entrada vacia, intenta de nuevo")
    else:
        nombres.append(nombre)

print(f"\nTotal de nombres ingresados: {len(nombres)}")

if len(nombres) == 0:
    print("No se ingresaron nombres")
elif len(nombres) != len(set(nombres)):
    print("Hay nombres repetidos")  # ← Agrega esta línea
else:
    print("No hay nombres repetidos")

