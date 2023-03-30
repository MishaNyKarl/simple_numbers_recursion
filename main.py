def simple_num(n):
    """При вводе числа n создает массив простых чисел с диапазоном от 0 до n.
    С помощью решета Эретосфера"""

    a = [i for i in range(n+1)]
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = [i for i in a if i != 0]
    print(a)
    return a


def infinity_simple(mas, gl):
    """Функция используется для просчитывания супер простых чисел
    (выводит простые числа, которые стоят на простых местах) любой глубины.
    На ввод требует массив и глубина простоты"""

    if gl == 1:
        return mas

    mas.insert(1,0)
    n = len(mas) - 1
    mas[0] = 0
    i = 2
    while i <= n:
        if mas[i] != 0:
            j = i + i
            while j <= n:
                mas[j] = 0
                j = j + i
        i += 1
    mas = [i for i in mas if i != 0]

    return infinity_simple(mas, gl-1)


simple_num(14)
print(infinity_simple(simple_num(11), 5))