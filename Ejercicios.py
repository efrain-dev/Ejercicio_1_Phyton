
def producto():

    numeroUno= int(input("Introduce el primer numero"))
    numeroDos= int(input("Introduce el segundo numero"))
    resultado=0
    for x in range(0, numeroDos):
        resultado=resultado + numeroUno

        print(resultado)


def productoraro():
    num1=0
    num2=0
    i = ord('d')
    while not i == 102:

        num2 = int(input("Ingrese un numero"))
        i = ord(input("Presione f para salir"))
        print(num2)
        num1 = num1 * num2
    print(num1)

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