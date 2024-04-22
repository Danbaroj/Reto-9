if __name__ == "__main__":

    c = float(input("¿De cuanto es el prestamo?: "))
    i = float(input("¿De cuanto es el porcentaje del interes?: "))
    n = float(input("¿Por cuantos meses: "))

    interes_compuesto = lambda c, i, n : c * ((1+(i/100))**n) #Función anonima para calcular el interes compuesto.
    valor_int_comp = interes_compuesto(c,i,n) #Da valor a la variable "valor_int_comp" utilzando la función anonima.

    print("El interes compuesto es de " + str(valor_int_comp))  