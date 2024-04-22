#Programa que muestre los números primos del 1 al 100. Nota: use funciones

def divisores(*args):

    #Bucle que itera sobre cada número pasado como argumento
    
    for num in args:
        divisor = 50

        
        print(f"Divisores de {num}:")
        
        #Bucle que itera desde 50 hasta 2 para encontrar los divisores del número

        while divisor > 1:
            
            # Verifica si el número es divisible por el divisor actual
            
            if num % divisor == 0:
                print(divisor)
            divisor -= 1

if __name__ == "__main__":
    numero = int(input("Ingrese un número de 2 a 50: "))
    
    # Llama a la función divisores() con el número ingresado como argumento
    
    divisores(numero)
