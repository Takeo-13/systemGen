import systemgen

if __name__ == '__main__':
    x, y = input("Введи координаты в формате 'X Y': ").split()
    systemgen.System(x, y)