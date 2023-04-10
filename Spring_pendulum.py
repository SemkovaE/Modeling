from numpy import cos, arange, pi
import matplotlib.pyplot as plt

m = 1 # масса груза
g = 9.8 # сила тяжести
k = 1 # коэф. жест.
x0 = (m * g) / k # пружина растянута на величину
w = (k / m) ** 0.5 # частота

def spr(del_l, V0, m=1, k=1):
    '''
    V0 - начальная скорость
    del_l - смещение груза 
    '''
    fi0 = 0 # начальная фаза
    tol = (m / k) ** 0.5 * V0
    if tol:
        fi0 = -pi/2

    x_m = del_l + tol # амплитуда
    row_t = arange(0, 10, 0.1)
    row_x = x_m * cos(w * row_t + fi0) - x0
    return row_t, row_x

def spr_plot(row_t, row_x, q):
    plt.figure(q)#('Пружинный маятник')
    plt.plot([-1, row_t[0]], [-x0, -x0], 'r')
    plt.plot([0, 10],[-x0, -x0], color='#505050')
    plt.plot(row_t, row_x, 'r')
    plt.title('Пружинный маятник')
    plt.xlabel('Время')
    plt.ylabel('Смещение точки')
    plt.grid(True)

row_t, row_x = spr(1, 0)
spr_plot(row_t, row_x, 'смещение груза')
row_t, row_x = spr(0, 1)
spr_plot(row_t, row_x, 'сообщение скорости')

plt.show()