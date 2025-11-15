num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Tercer número: "))


if num1 > 0 and num2 > 0 and num3 > 0:
    print("Los tres son positivos")
else:
    print("No todos son positivos")


if num1 < 0 or num2 < 0 or num3 < 0:
    print("Al menos uno es negativo")
else:
    print("Ninguno es negativo")

cantidad_ceros = 0
if num1 == 0:
    cantidad_ceros += 1
if num2 == 0:
    cantidad_ceros += 1
if num3 == 0:
    cantidad_ceros += 1

if cantidad_ceros == 1:
    print("Exactamente uno es cero")
else:
    print("No hay exactamente uno en cero")
