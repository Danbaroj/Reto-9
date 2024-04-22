## Reto-9

1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

  - Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

```python
if __name__ == "__main__":

    c = float(input("¿De cuanto es el prestamo?: "))
    i = float(input("¿De cuanto es el porcentaje del interes?: "))
    n = float(input("¿Por cuantos meses: "))

    interes_compuesto = lambda c, i, n : c * ((1+(i/100))**n) #Función anonima para calcular el interes compuesto.
    valor_int_comp = interes_compuesto(c,i,n) #Da valor a la variable "valor_int_comp" utilzando la función anonima.

    print("El interes compuesto es de " + str(valor_int_comp))   
```

  - Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
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
```

  - El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```python
if __name__ == "__main__":

    C = int(input("¿Cuantas personas hay contagiadas actualmente?: "))
    D = int(input("¿Cuantos días pasaran?: "))

    num_contagiados = lambda D, C :C * (2**D) #Función anonima que calcula el numero de contagiados
    cantidad_contagiados= num_contagiados(D,C)#Da valor a la variable "cantidad_contagiados" haaciendo uso de la función anonima
     
    print("La cantidad de personas que se contagiaran en " +str(D) + " dias, será de " + str(cantidad_contagiados))
```
2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

  - Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones

```python
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
```

  - Programa que muestre los números primos del 1 al 100. Nota: use funciones

```python
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
```
  - Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```python
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

```
3. Escriba una función recursiva para calcular la operación de la potencia.

```python
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
```
5. Crear cuenta en stackoverflow y adjuntar imagen en el repo

[![Stackoverflow.jpg](https://i.postimg.cc/Hx2zqRvR/Stackoverflow.jpg)](https://postimg.cc/njXq7RJG)

6. Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.

[![Linkedin.jpg](https://i.postimg.cc/rFS13vdJ/Linkedin.jpg)](https://postimg.cc/D8w4bpPJ)
