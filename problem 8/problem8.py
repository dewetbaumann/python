from os import system as console
console('color 0b && cls')

def inputPrice():
    major , major2, minor, average, add, loops = 0,0,0,0,0,0
    while True:
        try:
            price = float(input('Ingrese el precio: $'))
            if price == 0: break
            
            else:
                if minor == 0 and major == 0: 
                    minor, major = price,price
                    add += price
                    loops += 1
                    if price > major: major = price
                    elif price < minor: minor = price
                    elif price > 1000: major2 += 1
                
                else:
                    add += price
                    loops += 1
                    if price > major: major = price
                    elif price < minor: minor = price
                    if price > 1000: 
                        major2 += 1
                        print(major2)
        except: 
            print('El precio solo puede ser un racional')
            console('pause > null && cls')
      
    try:
        average = (add/loops)
        return major,major2,minor,average

    except: print('Warning: No se ingresaron precios')

try: 
    major,major2,minor,average = inputPrice()
    console('color 0c && cls')
    print (f'\n-> El cafe de mayor precio es: ${major}')
    print (f'-> El cafe de menor precio es: ${minor}')
    print (f'-> El precio promedio de los cafes es: ${average:.1f}')
    print (f'-> Cafes con un precio de mas de $1.000 son: {major2}\t')

except: print('Cuando tenga los precios vuelva por favor...')
