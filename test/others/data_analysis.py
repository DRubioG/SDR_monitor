import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift

file = open("./desarrollo/dual_sin/dual_sin.sim/sim_1/behav/xsim/datos_out.dat", 'rb')
# print(file.read())

line_good = []

for line in file:
    # line = line.split("\n")[0]
    line_good.append(int(line, 2))

# N = 3100
# T = 1.0 / 800.0
# yf = fft(line_good)
# xf = fftfreq(N, T)
# f = fftshift(xf)
# yplot = fftshift(yf)
# sp = np.fft.fft(line_good)
# plt.plot(sp)
# plt.figure()
plt.plot(line_good)
plt.show()