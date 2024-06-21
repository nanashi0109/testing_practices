from math import sqrt


def input_number(massage: str) -> float:
    number = input(massage)
    default_number = 1
    try:
        number = float(number)
        return number
    except ValueError:
        print(f"Невозможно преобразовать в число! Будет возвращено значение по умолчанию: {default_number}")
        return  default_number


# Task_1
def quadratic_equation() -> None:
    print("Введите коэффициенты a, b и c для уравнения ax^2 + bx + c = 0")
    a = input_number("Коэффициент a: ")
    b = input_number("Коэффициент b: ")
    c = input_number("Коэффициент c: ")

    if (a == 0) or (b == 0):
        print("Коэффициенты равну нулю! Это не является квадратным уравнением")
        return

    discriminant = calculate_discriminant(a, b, c)

    calculate_roots(a, b, discriminant)


def calculate_discriminant(a: float, b: float, c: float) -> float:
    return b*b - 4*a*c


def calculate_roots(a: float, b: float, discriminant: float):
    if discriminant > 0:
        root1 = (-b + sqrt(discriminant)) / (2 * a)
        root2 = (-b - sqrt(discriminant)) / (2 * a)
        print(f"Корни уравнения: {root1}, {root2}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"Корень уравнения: {root}")
    else:
        print("У уравнения нет действительных корней")


# Task_2
def triangle_area() -> None:
    print("Введите длины сторон треугольника a, b и c:")
    a = input_number("Сторона a: ")
    b = input_number("Сторона b: ")
    c = input_number("Сторона c: ")

    if (a < 0) or (b < 0) or (c < 0):
        print("Длинны сторон не могут быть меньше нуля ")
        return

    if (a + b <= c) or (a + c <= b) or (b+c <= a):
        print("Треугольник с такими сторонами не существует")
        return

    half_perimetr = calculate_half_perimetr(a, b, c)

    area = calculate_area(a, b, c, half_perimetr)

    print(f"Площадь треугольника {area}")


def calculate_half_perimetr(a: float, b: float, c: float):
    return (a + b + c) / 2


def calculate_area(a: float, b: float, c: float, half_perimetr: float) -> float:
    area = sqrt(half_perimetr * (half_perimetr - a) * (half_perimetr - b) * (half_perimetr - c))

    return area


# Task_3
def temperature_conversion():
    print("Выберите опцию: ")
    print("1. Конвертировать Цельсий в Фаренгейт")
    print("2. Конвертировать Фаренгейт в Цельсий")
    choice = input_number("Ваш выбор: ")

    if choice == 1:
        convert_to_fahrenheit()
    elif choice == 2:
        convert_to_celsius()
    else:
        print("Неправильный выбор")


def convert_to_fahrenheit():
    celsius = input_number("Введите температуру в градусах Цельсия: ")
    fahrenheit = (celsius * (9.0 / 5.0)) + 32
    print(f"Температура в градусах Фаренгейта: {fahrenheit}")


def convert_to_celsius():
    fahrenheit = input_number("Введите температуру в градусах Фаренгейта: ")
    celsius = (fahrenheit - 32) * (5.0 / 9.0)
    print(f"Температура в градусах Цельсия: {celsius}")


class Program:
    @staticmethod
    def main():
        quadratic_equation()
        # triangle_area()
        # temperature_conversion()


Program.main()
