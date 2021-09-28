a = int(input())
b = int(input())
c = int(input())
print(4 * (a + b + c))  # edge length
half_surface = (a * b + b * c + c * a)
print(2 * half_surface)  # surface area
print(a * b * c)  # volume
