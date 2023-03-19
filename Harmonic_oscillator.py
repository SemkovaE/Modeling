from numpy import sin
import matplotlib.pyplot as plt

A = 1 # Амплитуда
w = 1 # Частота колебания
t = 0 # Время
dt = 0.01 # Шаг
fi = 0 # Начальная фаза

def osc(A, w, t, dt, fi):
    row_t = []
    row_x = []
    while t <= 10:
        x = A * sin(w * t + fi)
        row_t.append(t)
        row_x.append(x)
        t += dt
    return row_t, row_x

def osc_plot(row_t, row_x):
    plt.figure('Гармонический осциллятор')
    plt.plot(row_t, row_x, 'r')
    plt.title('Гармонический осциллятор')
    plt.xlabel('Время')
    plt.ylabel('Смещение точки')
    plt.text(0, -1, 'A = {}; {} = {}; {} = {}'.format(A, chr(969), w, chr(966), fi), fontsize = 10)
    plt.grid(True)

row_t, row_x = osc(A, w, t, dt, fi)
osc_plot(row_t, row_x)

plt.show()
