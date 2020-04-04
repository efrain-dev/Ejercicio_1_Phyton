def ejercicio1():
    numeroUno = int(input("Introduce el numero"))
    print("El numero es uno "+str(numeroUno))


def ejercicio2():

    numeroUno= int(input("Introduce el primer numero"))
    numeroDos= int(input("Introduce el segundo numero"))
    resultado=numeroDos*numeroUno

    print("El numero es"+str(resultado))

def ejercicio3():
    num1=0
    num2=0
    resultado=0
    num1 = int(input("Ingrese un numero"))
    num2 = int(input("Ingrese un numero"))
    if num2 >= num1:
     resultado=num1
    else:
     resultado=num2
     print("el numero mayor es"+str(num2))

def ejercicio4():

    num1 = float(input("Ingrese un numero"))
    num2 = float(input("Ingrese el numero 2 "))
    num3 = float(input("Ingrese el numero 3 "))
    if num1 > num2:
        if num1 > num3:
            if num2 > num3:
                print("El valor mayor es: ", num1)
    elif num2 > num1:
        if num2 > num3:
            if num1 > num3:
                print("El valor mayor es: ", num2)

    elif num3 > num2:
        if num3 > num1:
            if num2 > num1:
                print("El valor mayor es: ", num3)

def ejercicio6():
    resultadoSuma=0
    resultadoProducto=1
    for x in range(0, 50):
        num1 = int(input("El numero"))
        resultadoSuma=resultadoSuma+num1
        resultadoProducto=resultadoProducto*num1

    print("La suma es ", str(resultadoSuma))
    print("El producto es ", str(resultadoProducto))

def ejercicio7():
    num1 = 0
    resultado =0
    while not num1 < 0 :
        resultado = resultado+num1
        num1 = int(input("Ingrese un numero x"))


    print("La suma total es" + str(resultado))

def ejercicio8():

    numeroUno= int(input("Introduce el primer numero"))
    numeroDos= int(input("Introduce el segundo numero"))
    resultado=0
    for x in range(0, numeroDos):
        resultado=resultado + numeroUno

        print(resultado)

def ejercicio10():
    num1=1
    num2=1
    i = ord('d')
    while not i == 102:

        num2 = int(input("Ingrese un numero"))
        i = ord(input("Presione f para salir"))
        print(num2)
        num1 = num1 * num2
    print(num1)

def ejercicio11():
    num1=0
    i = ord('d')
    while not i == 102:

        num2 = int(input("Ingrese un numero"))
        i = ord(input("Presione f para salir"))
        if num2 >= num1:
            num1=num2
        print("hola")
    else:
        num2=num1

    print("el numero mayor es"+str(num2))

def ejercicio15():
        contador = 0
        a = 0
        b = 1
        c = 0
        N = int(input("INGRESE LA CANTIDAD QUE DESEA VER"))

        while contador < N:
            a = b
            b = c
            c = a + b
            print(c)
            contador = contador + 1

def sumapar():
    num1=0
    num2=0
    i = ord('d')
    while not i == 102:

        num2 = int(input("Ingrese un numero"))
        i = ord(input("Presione f para salir"))
        if num2%2 ==0:
            num1= num1 + num2
        print(num1)
    print("La suima es"+str(num1))

def factorial1(num):

    factorial = 1

    if num < 0:
        print("Lo siento el factorial no existe porque es un numero negatico")
    elif num == 0:
        print("El fatorial de 0 es 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
    return factorial

def sumaprimo():
    num1=0
    num2=0
    for x in range(0, 50):
        num1 = int(input("El numero"))
        divisor = 2
        while num1>divisor:
             if num1%divisor==0:
              break
             elif num1%divisor != 0:
              divisor=divisor+1

             if num1==divisor:
              num2 = num2 + num1

    print("La suma es"+str(num2))



def ejecicior15():
    contador = 0
    a = 0
    b = 1
    c = 0
    N = int(input("INGRESE LA CANTIDAD QUE DESEA VER"))

    while contador < N:
        a = b
        b = c
        c = a + b
        print(c)
        contador = contador + 1

def ejercicio16():
    lista = []
    mayor = 0
    menor = 999999
    cont = 0
    while  cont==0 :
        valor = int(input("Digite un numero"))
        if (valor%2) == 0:
            lista.append(valor)
            cont = 0
        else:
            cont=1

    lista.append(0)
    lista2= lista
    if len(lista)>0 and len(lista2)>0:
        for x in range(len(lista) - 1):
            if lista[x] >= mayor:
                mayor = lista[x]
        for x in range(len(lista) - 1):
            if lista[x] <= menor:
                menor = lista2[x]
        print("El valor mayor ingresado es: ", mayor)
        print("El valor menor ingresado es: ", menor)

def ejercicio17():
    cant = int(input("Cuantas cantidades desea ingresar?"))
    cont=0
    total = 0
    while cont < cant:
        num1 = float(input("Ingrese un numero: "))
        cont = cont + 1
        if num1 % 2 == 0:
            total = total + num1
        else:
            total = total
    print("La suma de los pares es: ", total)

def ejercicio18():
    cant = int(input("Cuantas cantidades desea ingresar?"))
    lista=[]
    cont=0
    total = 0
    while cont < cant:
        num1 = int(input("Ingrese un numero: "))
        cont = cont + 1
        if num1 % 2 == 0:
            lista.append(num1)
    if cont <=10:
        print("La lista de los pares es: ", lista[0:cont])
    else:
        print("La lista de los pares es: ", lista[0:10])

def ejercicio19():
    cant = int(input("Cuantas cantidades desea ingresar?"))
    lista = []
    cont = 0
    cont2=0
    total = 0
    while cont < cant:
        num1 = int(input("Ingrese un numero: "))
        cont = cont + 1
        if num1 % 2 == 0:
            if cont <= 30:
                cont2 +=1
                lista.append(num1)
    lista.append(0)
    if cont2 <= 30:
        for x in range(cont2):
            total += lista[x]
        print("La suma de los pares es: ", total)
    else:
        for x in range(30):
            total += lista[x]
        print("La suma de los pares es: ", total)

def ejercicio20():
    num = int(input("Ingrese un numero: "))
    x=1
    factorial=1
    while x <= num:
        print(x)
        factorial = factorial*(x)
        x +=1
    print("El factorial de", num, "es:",factorial)

def ejercicio21():
    num = float(input("Ingrese un numero: "))
    x=1
    cont=0
    for x in range (1,int(num)+1):
        if (num % x ) == 0:
            cont += 1
    if cont == 2:
        print("El valor", num, "es primo")
    else:
        print("El valor", num, "no es primo")

def ejercicio22():
    lista= []
    total=0
    x=1
    for x in range(1,31):
        valor=float(input("Digite un numero"))
        lista.append(valor)
    lista.append(0)
    for x in range(1,31):
        cont=0
        for y in range(1, int(lista[x]) + 1):
            if (lista[x] % y) == 0:
                cont += 1
        if cont == 2:
            total= total+lista[x]
    print("La suma de los numeros primos es: ", total)

def ejercicio23():
    lista= []
    factlista=[]
    factorial=1
    total=0
    x=0
    y=1
    for x in range(1,6):
        valor=float(input("Digite un numero"))
        lista.append(valor)
    lista.append(0)
    for x in range(5):
        while y <= lista[x]:
            factorial = factorial*(y)
            y +=1
        factlista.append(factorial)
    for x in range(len(factlista)):
        total += factlista[x]
    print(total)

def factorial(num):
    factorial = 1
    if num < 0:
        print("Lo siento el factorial no existe porque es un numero negatico")
    elif num == 0:
        print("El fatorial de 0 es 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
    return factorial

def ejercicio24():
    num1 = int(input("Entre mas grande el numero mas preciso es el valor de euler"))
    euler=1
    for i in range(1, num1):
            euler = euler+ 1/factorial(i)

    print("Numero de euler es"+str(euler))

def ejerccico25():
    numero = int(input("Ingrese el numero"))
    i= int(input("Ingrese I"))
    resultado = factorial(numero)/(factorial(i)*factorial(numero-i))
    print("EL resultado es " +str(resultado))
ejercicio24()
ejerccico25()
