from numpy import sin, arange
import matplotlib.pyplot as plt

A = 1 # Амплитуда
w = 1 # Частота колебания
fi = 0 # Начальная фаза

def osc(A, w, fi):
    row_t = arange(0, 10, 0.01)
    row_x = A * sin(w * row_t + fi)
    return row_t, row_x

def osc_plot(row_t, row_x):
    plt.figure('Гармонический осциллятор')
    plt.plot(row_t, row_x, 'r')
    plt.title('Гармонический осциллятор')
    plt.xlabel('Время')
    plt.ylabel('Смещение точки')
    plt.text(0, -1, 'A = {}; {} = {}; {} = {}'.format(A, chr(969), w, chr(966), fi), fontsize = 10)
    plt.grid(True)

row_t, row_x = osc(A, w, fi)
osc_plot(row_t, row_x)

plt.show()
