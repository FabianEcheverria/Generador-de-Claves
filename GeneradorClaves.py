import string, random
import os

def Main():
    os.system('cls') #Limpia la consola
    print("+++++++Bienbenido al Generado de Contraseñas++++++")
    
    def Ok(n):
        try:
            n = int(n)
        except:
            n = Ok(input("Caracter no valido, intente de nuevo!: "))
        return n
            
    while True:
        mayus = Ok(input("Cantidad minima de mayusculas: "))
        minus = Ok(input("Cantidad minima de minusculas: "))
        numero = Ok(input("Cantidad minima de numeros: "))

        longitud = mayus + minus + numero
        caract = string.ascii_letters+string.digits+string.punctuation
        
        contraseña = (" ").join(random.choice(caract) for i in range(longitud))
        if (sum(c.islower() for c in contraseña) >= minus 
            and sum(c.isupper() for c in contraseña) >= mayus
            and sum(c.isdigit() for c in contraseña) >= numero):
            break
    
        print("Su contraseña es: ", contraseña)
            
        continuar = Ok(input("1) Generar nueva contraseña: \n2) Terminar: "))
        if continuar != 1:
            break
        else:
            continue
    

    
Main()