from os import system as console

console('cls')
console('color 0b')

def inputHour():
    try:
        hour = int(input('Ingrese la hora (formato 24hs): '))
        if hour < 0:
            print ('La hora no puede ser negativa')
            return False
        
        elif hour > 24:
            print ('La hora no puede ser mayor a 24')
            return False

        else:
            console('cls')
            if hour >= 0 and hour < 5: print('Anda a dormir que te voy dar con la chancla') 
            elif hour >= 5 and hour < 12: print('Buenos dias, aunque no se que tienen de bueno levantarse temprano') 
            elif hour >= 12 and hour < 19: print('Buenas tardes, esta especial para una siesta no?') 
            else: print('Buenas noches, hora de mimir') 
                
    except: print('Error: La hora solo puede ser un entero mayor a 0 y menor a 24')

inputHour()