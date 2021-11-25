#### Paint Can Calculator ####
# module import
import math
# function to calculate the number of cans required to paint
def paint_calc(height, width, cover):
    area = height * width
    can_required = area / cover
    print(f'The number of cans required are {math.ceil(can_required)}')

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)