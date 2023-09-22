

def area_triangle(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
    else:
        s = "Треугольник не существует."
    return s


def area_circle(r):
    if r <= 0:
        return "Радиус меньше, либо равен нулю. Круга не существует."
    s = 3.14 * r ** 2
    return s


def is_right_triangle(a, b, c):
    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) \
            or (b ** 2 + c ** 2 == a ** 2):
        return "Треугольник является прямоугольным."
    return "Треугольник не является прямоугольным"
