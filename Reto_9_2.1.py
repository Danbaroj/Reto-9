#Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones

def primo(numero):
    
    # Verifica si el número es menor o igual a 1, ya que los números primos deben ser mayores que 1
    
    if numero <= 1:
        return False
    
    divisor = 2
    
    #Bucle que itera hasta que el cuadrado del divisor sea menor o igual que el número
    
    while (divisor ** 2) <= numero:

        # Verifica si el número es divisible por el divisor actual
        
        if numero % divisor == 0:
            return False
        divisor += 1

    return True

def limite_primos(*args):

    #Bucle que itera sobre cada límite pasado como argumento
    
    for limite in args:
        print("Números primos del 1 al " + str(limite))
        num = 2

        #Bucle que itera desde 2 hasta el límite
        
        while num <= limite:
            
            # Verifica si el número es primo utilizando la función primo()
            
            if primo(num):
                print(num)
            num += 1
            print()

limite_primos(100)  # Limita los primos mostrados hasta 100
