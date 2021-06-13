from os import system as console
console('color 0b && cls')


def weightValidation():
    while (True):
        try:
            stay = int(input('Cuantos anios va a estar en la luna: '))
            earthWeight = float(input('Ingrese su peso terrestre: '))
            break

        except: 
            print('1 -> Error: El anio solo puede ser un entero y el peso un racional\n2 -> Error: Presione una tecla para volver a empezar')
            console('pause > null && cls')

    weightCalc(earthWeight,stay)

def weightCalc(earthWeight,stay):
    console('cls')
    weight = 0
    for i in range(stay):
        weight +=1
        print (f'anio {i+1} -> Su peso lunar es de {((earthWeight+weight)*.165):.1f}')

weightValidation()