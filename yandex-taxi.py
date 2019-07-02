from random import randint, seed
"""
Задача Яндекс-такси

Дано поле MxN, по которому разбросаны целые числа.
[*][0][3][.][.]
[.][.][2][.][.]
[.][7][.][.][.]
[.][.][.][.][X]

Водитель двигается из левого верхнего угла
в правый нижний, совершая движения либо вниз,
либо вправо.

Перебрать все возможные маршруты и найти
маршрут с наибольшей суммой
"""

# ----- Конфиг ---------
MIN_INT = -999999
ROWS = 5  # M
COLS = 7  # N
# Флаги, обозначающие движения
FLAG_MOVE_RIGHT = 1
FLAG_MOVE_DOWN = 0
# ----------------------


def print_route_on_desk(route):
    """
    Выводит маршрут на доске графически:
    [*][ ][ ][ ][ ]
    [*][*][ ][ ][ ]
    [ ][ ][*][ ][ ]
    [ ][ ][*][*][*]
    TODO: допишите сюда код
    """
    pass


def generate_desk(M, N):
    """
    Заполняет доску случайными целыми числами
    Доска = список списков
    """
    desk = [[FLAG_MOVE_DOWN] * COLS] * ROWS
    for i in range(0, ROWS):
        for j in range(0, COLS):
            desk[i][j] = randint(0, 9)
    return desk


def print_route(route):
    """
    Выводит маршрут на экран
    TODO: почему нельзя в методе с таким именем выводить еще и сумму на маршруте?
    """
    print(route)


def is_valid(route) -> bool:
    """
    Проверка корректности маршрута (что не вышли за край)
    """
    sum_down = 0
    sum_right = 0
    for i in route:
        if i == FLAG_MOVE_RIGHT:
            sum_right += 1
        if i == FLAG_MOVE_DOWN:
            sum_down += 1
    return sum_down == (ROWS-1) and sum_right == (COLS-1)


def calc_sum(route, desk) -> int:
    """
    Вычисляет сумму по маршруту route на доске desk
    двигая координаты x(столбец), y(строка)
    """
    y = 0
    x = 0
    s = 0  # сюда накапливается сумма
    for i in route:
        # Проверяем, что данные корректны - из допустимого набора
        assert i in [FLAG_MOVE_DOWN, FLAG_MOVE_RIGHT]
        s += desk[y][x]
        if i == FLAG_MOVE_DOWN:
            y += 1
        if i == FLAG_MOVE_RIGHT:
            x += 1
    return s


def next_route(route):
    """
    По предыдущему маршруту возвращает следующий
    увеличивая на единицу число по правилам сложения
    в двоичной системе, представляя, что нулевой разряд - справа
    """
    digit = 0
    while digit < len(route):
        route[digit] += 1
        if route[digit] == 1:
            break
        else:
            route[digit] = 0
            digit += 1
    return route


if __name__ == "__main__":
    seed(42) # Устанавливаем зерно датчика сл. чисел, чтобы получить
    # всегда один и тот же результат
    TOTAL_DIGITS = ROWS-1 + COLS-1 # Всего разрядов в нашем маршруте
    desk = generate_desk(ROWS, COLS) 
    route = [0] * TOTAL_DIGITS # Начальный маршрут
    max_win = MIN_INT
    saved_route = route
    
    for i in range(0, 2**TOTAL_DIGITS): # TODO: цикл выходит за границы
        # TODO: а вдруг route был верным, а мы сразу ушли на следующий
        # как переделать?
        route = next_route(route)
        if not is_valid(route):
            continue
        s = calc_sum(route, desk)            
        if s >= max_win:
            max_win = s
            saved_route = route
            print(max_win, end="")
            print_route(saved_route)
    print("Done")







