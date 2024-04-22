def potencia(n, x):

    # Verifica si el exponente es igual a 0, en cuyo caso devuelve 1
    
    if x == 0:
        return 1
    else: 

        return n ** x
    
if __name__ == "__main__":
    
    n = int(input("Ingrese el número que será la base: "))
    x = int(input("Ingrese su exponente: "))
    
    poten = potencia(n, x)# Calcula la potencia utilizando la función potencia() y los números ingresados por el usuario
    
    print("El número " + str(n) + " elevado al exponente " + str(x) + " es igual a " + str(poten))
