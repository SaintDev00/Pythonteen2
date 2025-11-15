lista_restringida= ["admin", "root", "test"]

usuario = input("Nombre de usuario: ") .lower()

codigo = int(input("Codigo numerico: ")) 

if usuario in lista_restringida:
    print("Acceso denegado : usuario restringido")

else:
    if codigo % 2== 0 or codigo %10 == 7:
        print("Acceso permitido")
    else:
        print("Acceso denegado: Codigo invalido")

