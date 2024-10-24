import math

# Уровень 1
def cube_properties(gran_surface_area):
    # Найдем длину ребра
    edge_length = math.sqrt(gran_surface_area)
    
    # Найдем объем куба
    volume = edge_length ** 3
    
    # Найдем площадь поверхности куба
    surface_area = 6 * edge_length ** 2
    
    return edge_length, volume, surface_area

# Пример использования:
gran_surface_area = 25  # площадь грани куба
edge_length, volume, surface_area = cube_properties(gran_surface_area)

print(f"Длина ребра: {edge_length}")
print(f"Объем куба: {volume}")
print(f"Площадь поверхности: {surface_area}")

# Уровень 2
def check_repeated_digits(number):
    # Преобразуем число в строку и создаем множество цифр
    digits = set(str(number))
    
    # Если длина множества меньше 4, то есть повторяющиеся цифры
    return 1 if len(digits) < 4 else 0

# Пример использования:
number = 1223  # четырехзначное число
result = check_repeated_digits(number)

print(f"Результат: {result}")
