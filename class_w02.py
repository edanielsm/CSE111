import math

items = int(input('Enter the number of items:\n > '))
boxes_items = int(input('Enter the number of items per boxes:\n > '))

number_boxes = math.ceil(items / boxes_items)

print(f'For {items} items, packing {boxes_items} items in each box, you will need {number_boxes} boxes.')

