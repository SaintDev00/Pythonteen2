luces_encendidas = False
calefaccion_activa = False


es_de_noche = input("¿Es de noche? (si/no): ").lower() == "si"
temperatura = float(input("Temperatura actual (°C): "))


while True:
    print("\n=== PANEL DE CONTROL DOMÉSTICO ===")
    print("1. Encender/Apagar luces")
    print("2. Activar/Desactivar calefacción")
    print("3. Ver estado")
    print("4. Salir")
    
    opcion = input("\nSelecciona una opción: ")
    
    match opcion:
        case "1":
           
            if not luces_encendidas:  
                if es_de_noche:
                    luces_encendidas = True
                    print("✓ Luces encendidas")
                else:
                    print("✗ No se pueden encender las luces: Es de día")
            else: 
                luces_encendidas = False
                
                if calefaccion_activa:
                    calefaccion_activa = False
                    print(" Calefacción apagada automáticamente")
                print(" Luces apagadas")
        
        case "2":
          
            if not calefaccion_activa:  # 
                if not luces_encendidas:
                    print(" No se puede activar: Las luces deben estar encendidas")
                elif temperatura >= 18:
                    print(f" No se puede activar: Temperatura actual ({temperatura}°C) debe ser menor a 18°C")
                else:
                    calefaccion_activa = True
                    print(" Calefacción activada")
            else: 
                calefaccion_activa = False
                print(" Calefacción desactivada")
        
        case "3":
          
            print("\n--- ESTADO ACTUAL ---")
            print(f"Hora: {'Noche' if es_de_noche else 'Día'}")
            print(f"Temperatura: {temperatura}°C")
            print(f"Luces: {'Encendidas' if luces_encendidas else 'Apagadas'}")
            print(f"Calefacción: {'Activa' if calefaccion_activa else 'Inactiva'}")
        
        case "4":
            print("Saliendo del sistema...")
            break
        
        case _:
            print(" Opción inválida")

print("Sistema apagado")
