from numpy import sin, arange, random
import matplotlib.pyplot as plt

A = 1 # Амплитуда
w = 1 # Частота колебания
fi = 0 # Начальная фаза

def osc(A, w, fi):
    row_t = arange(0, 10, 0.1)
    row_x = A * sin(w * row_t + fi)
    return row_t, row_x

def n(k):
    length = k.shape[0]
    k1, k2 = 0, 0.05
    noise = random.normal(k1, k2, size=length)
    return noise

def signal_to_noise(a, ddof=0):
    k1 = a.mean()
    k2 = a.std(ddof=ddof)
    return k1/k2

def osc_plot(row_t, row_x):
    plt.figure('Гармонический осциллятор')
    plt.plot(row_t, row_x, 'r')
    plt.plot(row_t, row_x + n(row_t), label='s(k)+n(k)')
    plt.legend(['s(k)', 's(k)+n(k)'], loc=4)
    plt.title('Гармонический осциллятор\nГауссовский шум s(k)')
    plt.xlabel('Время(k)')
    plt.ylabel('Смещение точки(v)')
    plt.text(0, -1, 'A = {}; {} = {}; {} = {}'.format(A, chr(969), w, chr(966), fi), fontsize = 10)
    plt.grid(True)

row_t, row_x = osc(A, w, fi)
osc_plot(row_t, row_x)
print(f'SNR = {signal_to_noise(row_x + n(row_t))}')

plt.show()
