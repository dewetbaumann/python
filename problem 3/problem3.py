from os import system as console

console('cls')
console('color 0b')

disapproved = 0
add = 0
aux = True

for i in range(6):
    if disapproved > 1:
        break
    else:
        while (aux):
            try:
                grade = float(input(f'Ingrese la nota del parcial({i+1}): '))
                if grade > 0 and grade < 6:
                    disapproved += 1
                    aux = False
                
                elif grade >= 6 and grade <= 10:
                    add += grade            
                    aux = False

                else:
                    print('La nota no puede ser menor a 0 y mayor a 10')

            except:
                print('Error: La nota sola puede ser un racional entre 0 y 10')

        aux = True

if disapproved == 0:
    average = add/6
    print (f'Promedio: {average:.2f}')

elif disapproved == 1:
    while (aux):
        try:
            grade = float(input(f'Ingrese la nota del parcial recuperatorio: '))
            
            if grade > 0 and grade < 7:
                print('Perdiste la materia por desaprobar 2 parciales')
            
            elif grade > 7 and grade <= 10:
                average = add/7
                print (f'Aprobado con un promedio de:{average:.2f}\ny con un parcial desaprobado!')
                
            aux = False

        except:
            print('Error: La nota sola puede ser un racional')
    
elif disapproved == 2:
    print('Perdiste la materia por desaprobar 2 parciales')

