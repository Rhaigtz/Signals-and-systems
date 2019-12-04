import numpy as np
from scipy import signal
#Triangular
fs = 5
simetria = 0.5
t = np.linspace(0,1,100)
x = signal.sawtooth(2*np.pi*5*t, 0.5)

#Corrimiento y proporcionalidad
c = 4
p = 5

#Exponencial Decreciente
s = np.linspace(0, 1.5, 10)
h = np.exp(-s)

#Exponencial Creciente
#s = np.linspace(0, 1.5, 10)
#h = np.exp(s)

#Sin(x)/(x)
#s = np.linspace(-10, 10, 50)
#h = np.sin(s-c)/(s-c)

#Escalon
#s = np.arange(0, 10, 0.5)
#h = np.piecewise(s-c, s-c >= 5, [1,0])

#Impulso
#s = np.linspace(0, 10, 50)
#h = np.zeros(len(s))
#h[10+c] = 1

h = h*p

filtered = signal.convolve(x, h, mode='same') / sum(h)
import matplotlib.pyplot as plt
fig, (ax_orig, ax_h, ax_filt) = plt.subplots(3, 1, sharex=True)
ax_orig.plot(x)
ax_orig.set_title('Original pulse')
ax_orig.margins(0, 0.1)
ax_h.plot(h)
ax_h.set_title('Filter impulse response')
ax_h.margins(0, 0.1)
ax_filt.plot(filtered)
ax_filt.set_title('Filtered signal')
ax_filt.margins(0, 0.1)
fig.tight_layout()
plt.show()