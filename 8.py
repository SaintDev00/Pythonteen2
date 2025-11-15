afirmativas = 0
negativas = 0

while True:
   
    edad = int(input("Edad (0 o negativo para terminar): "))
    
    if edad <= 0:
        break
    
    
    while True:
        respuesta = input("¿Te gusta programar? (si/no): ").lower().strip()
        
        if respuesta == "si":
            afirmativas += 1
            break  
        elif respuesta == "no":
            negativas += 1
            break
        else:
            print("Respuesta inválida. Por favor responde 'si' o 'no'")
          

#
print(f"\n Resultados:")
print(f"Respuestas afirmativas: {afirmativas}")
print(f"Respuestas negativas: {negativas}")
print(f"Total de participantes: {afirmativas + negativas}")
