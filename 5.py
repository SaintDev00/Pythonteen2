usuario_correcto = "admin"
password_correcta = "1234"


intentos = 0
max_intentos = 3
acceso_exitoso = False


while intentos < max_intentos and not acceso_exitoso:
    print(f"\nIntento {intentos + 1} de {max_intentos}")
    
  
    usuario = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()
    
    
    if usuario == "" and password == "":
        print(" Ambos campos están vacíos")
        # NO incrementa intentos
    
   
    elif usuario == usuario_correcto and password == password_correcta:
        print("✓ Acceso exitoso")
        acceso_exitoso = True
        intentos += 1
    
  
    elif usuario != usuario_correcto and password == password_correcta:
        print("✗ Usuario incorrecto")
        intentos += 1
    
    elif usuario == usuario_correcto and password != password_correcta:
        print("✗ Contraseña incorrecta")
        intentos += 1
    
    else: 
        print("✗ Usuario y contraseña incorrectos")
        intentos += 1


if intentos == max_intentos and not acceso_exitoso:
    print("\n Acceso bloqueado. Máximo de intentos alcanzado.")
