def rectangle_area(width, length):
    return width * length


input_width = int(input())
input_length = int(input())
calculated_area = rectangle_area(input_width, input_length)
print(calculated_area)