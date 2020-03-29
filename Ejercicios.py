
def producto():

    numeroUno= int(input("Introduce el primer numero"))
    numeroDos= int(input("Introduce el segundo numero"))
    resultado=0
    for x in range(0, numeroDos):
        resultado=resultado + numeroUno

        print(resultado)

producto()
def productoraro():
    num1=1
    num2=1
    i = ord('d')
    while not i == 102:

        num2 = int(input("Ingrese un numero"))
        i = ord(input("Presione f para salir"))
        print(num2)
        num1 = num1 * num2
    print(num1)
productoraro()
def mayor():
    num1=0
    num2=0
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
mayor()
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
sumapar()

def factorial(num):

    factorial = 1

    if num < 0:
        print("Lo siento el factorial no existe porque es un numero negatico")
    elif num == 0:
        print("El fatorial de 0 es 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("El factorial del numero", num, "es", factorial)

factorial(int(input("Ingrese el numero")))

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

sumaprimo()

def fibonacci():
    contador=0
    a=0
    b=1
    c=0
    N= int(input("INGRESE LA CANTIDAD QUE DESEA VER"))

    while contador < N:
        a=b
        b=c
        c=a+b
        print(c)
        contador=contador+1
fibonacci()
