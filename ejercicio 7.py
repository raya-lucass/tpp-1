import math
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area
radios = [2, 3.5, 5]
for r in radios:
    area = calcular_area_circulo(r)
    print(f"El área del círculo con radio {r} es: {area:.2f}")
