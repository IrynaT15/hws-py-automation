def find_radially_opposite_position(n, f_number):
    if f_number < n/2:
        number = f_number + n//2
    else:
        number = f_number - n//2
    return number


print(find_radially_opposite_position(10, 6))
print(find_radially_opposite_position(10, 2))
print(find_radially_opposite_position(10, 4))
print(find_radially_opposite_position(12, 1))
