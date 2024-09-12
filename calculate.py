def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

length = 10
width = 5

area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

print("Area:", area)
print("Perimeter:", perimeter)
