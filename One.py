edad=int(input("Cual es tu edad?"))

if edad < 0 or edad >120:
    print("Edad no valida")

else:
    if edad < 6:
        print("Infante")



    elif edad >= 6 and edad <=17:
        estudia=input("¿Estudia?si/no:").lower()
        if estudia == "si":
            print("estudiante escolar")
        else:
            print("No determinado")

    elif edad >= 18 and edad <= 25:
        estudia=input("¿Estudia en la universidad? si/no").lower()
        if estudia == "si":
            print("Estudiante universitario")
        else:
            print("No determinado")

    elif edad > 60:
        jubilado=input("trabajas?si/no").lower()
        if jubilado == "no":
            print("Eres un adulto mayor y jubilado")
        else:
            print("No determinado")


    elif edad > 25:
        Activo=input("Trabajas? si/no").lower()
        if Activo == "si":
            print("Eres un adulto activo")
        else:
            print("No determinado")
    
    else:
        print("No determinado")


   
