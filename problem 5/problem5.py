from os import system as console
console('cls')
console('color 0b')

def degreeValidation():
    try: 
        quadrant = int(input('Ingrese el angulo como un entero: '))
        quadrantOutput(quadrant)
    except: 
        print('Error: El angulo debe ser un entero...')

def quadrantOutput(quadrant):
    if quadrant == 0 or quadrant == 360: print('Eje X+')
    elif quadrant == 180: print('Eje X-')
    elif quadrant == 90: print('Eje Y+')
    elif quadrant == 270: print('Eje Y-')
    elif quadrant > 0 and quadrant < 90: print('Estas en el cuadrante: I')
    elif quadrant > 90 and quadrant < 180: print('Estas en el cuadrante: II')
    elif quadrant > 180 and quadrant < 270: print('Estas en el cuadrante: III')
    elif quadrant > 270 and quadrant < 360: print('Estas en el cuadrante: IV')

degreeValidation()