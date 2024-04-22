#Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y 
#H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo)
#cuando me da un billete de B pesos.

if __name__ == "__main__":

    P = int(input("Cuantos panes se mandaron a comprar: "))
    M = int(input("Cuantas bolsas de leche mandaron a comprar: "))
    H = int(input("Cuantos huevos mandaron a comprar: "))
    B = int(input("Cuanto dinero le dinero le dieron: "))

    vueltas = lambda P, M , H, B: B - ((P*300)+(M*3300)+(H*350)) #Función anonima que se encarga de calcular las vueltas
    dinero = vueltas(P, M, H, B) #Da valor a la variable "dinero" haciendo uso de la función anonima
    
    #Condicionales para conocer si se debe dinero o si le deben dar vueltas

    if dinero > 0:
        print ("Te deberian dar de vueltas " + str(dinero) + " pesos")
    else: 
        if dinero < 0:
            debo = abs(dinero)
            print ("Deberias " + str(debo) + " pesos")
