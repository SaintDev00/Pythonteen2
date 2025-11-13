while True: 
    try: 
        edad = int(input("Tell me how old are you"))
        
        while True:
            Trabaja = input("Tell me if your work")
            if edad>60 and Trabaja == "no":
                print("You are a old man")
                break
            
            elif edad>60 and Trabaja == "si":
                print("No determinado")
                break
            else:
                print ("Incorrecto")
              
        
        if edad>25 and Trabaja == "no":
            print("No determinado") 
            break
        
        elif edad >25 and Trabaja == "si":
            print("You are a active adult")
            break
        else:
              print("Incorrecto")
        
        while True:
        
            if edad >18 and edad<=25:
                N_escolar=input("You studied? yes/no : ").lower ()
                
                if N_escolar == "yes":
                        print("You are a university student")  
                        break
                
                elif N_escolar == "no":
                        print("You arent university student")
                        break
                else:
                      print("Wrong answer..choose yes or no")
                      
        while True:
              
                if edad >6 and edad<=17:
                        N_escolar=input("You studied? yes/no : ").lower()

                if N_escolar == "yes":
                        print ("tu eres un estudiante escolar")
                        break
                
                elif N_escolar == "no":
                        print ("tu no eres un estudiante escolar")
                        break
                else:
                      print("Wrong answer..choose yes or no") 

        while True:
              
                if edad <6:
                        print("You are a kid")
                else:
                    print("You need have more years of six")

    except ValueError:
          print("Try with a  whole number")
            
      
            

            
    
            





   