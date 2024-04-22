#El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer
#un programa que diga el número total de personas que se han contagiado cuando pasen D días
#a partir de hoy, si el número de contagiados actuales es C.

if __name__ == "__main__":

    C = int(input("¿Cuantas personas hay contagiadas actualmente?: "))
    D = int(input("¿Cuantos días pasaran?: "))

    num_contagiados = lambda D, C :C * (2**D) #Función anonima que calcula el numero de contagiados
    cantidad_contagiados= num_contagiados(D,C)#Da valor a la variable "cantidad_contagiados" haaciendo uso de la función anonima 
    
    print("La cantidad de personas que se contagiaran en " +str(D) + " dias, será de " + str(cantidad_contagiados))
