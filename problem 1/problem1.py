from os import system as console
from numpy import sqrt as raiz

console('color 0b')
console('cls')

def inputData():
    try:
        catAdyacente = float(input('Ingrese la distancia entre el pie de la escalera y la pared: '))
        hipotenusa = float(input('\t   '*3+'Ingrese la altura de la escalera: '))
        catOpuesto = raiz(hipotenusa**2 - catAdyacente**2)
        print ('-Respuesta-\n\t=> '+f'La altura de la piso a la escalera es: {catOpuesto:.1f}')
        console('pause > null')
        
        return False

    except:
        print ('Error: Solamente se pueden ingresar numeros reales, presione una tecla para reiniciar...')
        console('pause > null')
        
        return True

inputData()