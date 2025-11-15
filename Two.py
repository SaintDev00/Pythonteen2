Edad=int(input("Cual es tu edad?"))

Licencia = input ("Tienes licencia vigente? si/no:").lower()

Vehiculo=input("Tienes vehiculo propio? si/no:").lower()

Prestamo = input("Tienes prestamo autorizado? si/no:").lower()

if Edad >= 18 and Licencia == "si" and (Vehiculo == "si" or Prestamo == "si"):
    print("Apto para participar")
else:
    print("No apto para participar")

