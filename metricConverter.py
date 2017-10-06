''' This is a metric converter.
It converts quantities from metres to millimeters
centimetres, kilometres, inches, feets, miles, and
yard.

'''
from decimal import Decimal as D
mm = 'millimeters'
cm = 'centimeters'
km = 'kilometers'
inch = 'inches'
ft = 'feets'
mile = 'miles'
yd = 'yards'
Dans = 0
print('''mm = millimeters
cm = centimeters
km = kilometers
inch = inches
ft = feets
mile = miles
yd = yards ''')
Dx = input('enter value: ')
conv = input( 'enter unit of conversion:')
if conv == mm :
    Dans = Dx/1000
    print('the answer is ' + Dans + 'mm')
elif conv == cm :
    Dans = Dx/100
    print('the answer is ' + Dans + 'cm')
elif conv == km :
    Dans = Dx * 1000
    print('the answer is ' + Dans + 'km')
elif conv == inch :
    Dans = Dx * 39.37
    print('the answer is ' + Dans + 'inches')
elif conv == ft :
    Dans = Dx * 3.28
    print('the answer is ' + Dans + 'ft')
elif conv == mile :
    Dans = Dx * 0.00621
    print('the answer is ' + Dans + 'miles')
elif conv == yd :
    Dans = Dx * 1.094
    print('the answer is ' + Dans + 'yards')
else:
    print(' you have entered an invalid unit of conversion')




