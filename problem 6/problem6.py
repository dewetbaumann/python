from os import system as console
console('color 0b')

def sexValidation():
    while (True):    
        try:
            sex = int(input('\nOpcion: '))
            if sex == 1 or sex == 2: return sex
            else: print ('El sexo solo puede ser 1 o 2')

        except: print ('El sexo solo puede ser un entero (1 o 2)')

def sexCounter():
    male = 0
    female = 0
    
    for i in range(6):
        console('cls')
        print(f'Ingrese el sexo del empleado N {i+1}:\n\t1 -> Varon\n\t2 -> Mujer')
        sex = sexValidation()
        if sex == 1: male += 1
        elif sex == 2: female +=1
        else: print('Sexo desconocido')

    console('cls')
    print(f'# Hay {male} empleados varones \n# Hay {female} empleados mujeres')

sexCounter()