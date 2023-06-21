from math import ceil

def paint_calc(height,width,cover):
    return ceil((height * width) / cover)

test_h = int(input('Height of wall: '))
test_w = int(input('Width of wall: '))
coverage = 5
num_of_cans = paint_calc(height=test_h, width=test_w, cover=coverage)

print(f'You will need {num_of_cans} cans of paint.')