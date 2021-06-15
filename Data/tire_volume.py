import math
def place_value(number):
    return ('{:,}'.format(number))



w = float(input('Enter the width of the tire in mm (ex 205):\n> '))
a = float(input('Enter the aspect ratio of the tire (ex 60):\n> '))
d = float(input('Enter the diameter of the wheel in inches (ex 15):\n> '))

volume = (w*a + 2540*d) * math.pi * w**2 * a / (10000000)

print(f'The approximate volume is {place_value(round(volume,1))} cubic cm')


from datetime import datetime
current_day = datetime.now()
current_day = current_day.date()
with open('volumes.txt', 'a') as dimens_file:
    print(f'{current_day}, {w}, {a}, {d}, {volume:.2f}')


