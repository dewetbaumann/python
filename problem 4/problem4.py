from os import system as console
console('color 0b && cls')

mes = input('ingrese el mes: ').lower()

if mes == 'abril' or mes == 'junio' or mes == 'septiembre'or mes == 'noviembre':
    print ('El mes trae 30 dias')

elif mes == 'enero' or mes == 'marzo' or mes == 'mayo' or mes == 'julio' or mes == 'agosto' or mes == 'octubre' or mes == 'diciembre':
    print ('El mes trae 31 dias')

elif mes == 'febrero':
    print ('El mes trae 28 o 29 dias, todo un misterio la verdad esto de los 100tificos')

else:
    print('verifica la escritura del mes')
