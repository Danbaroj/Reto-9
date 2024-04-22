#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

def num_par(*args):

    #Bucle que itera sobre cada número pasado como argumento
    
    for num in args:

        numero_inicial = 1000
        print("Los siguientes números pares son menores al número natural dado:")
        
        #Bucle que itera hasta que el número inicial sea mayor que 2

        while numero_inicial > 2:

            numero_inicial -= 2
            if numero_inicial > num:
                continue
            print(numero_inicial)

        print("Fin del listado")

if __name__ == "__main__":

    numero = int(input("Ingrese un número natural mayor o igual a 2: "))
    num_par(numero)


#Nota del autor: Me di cuenta que a la hora de hacerlo para el reto 7, lo puse mal, esta asi: int(input("Ingrese un numero naturar menor o igual a 2: "))
