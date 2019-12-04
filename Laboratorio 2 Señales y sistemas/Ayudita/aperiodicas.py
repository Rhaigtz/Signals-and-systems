import numpy as np
from scipy import signal

binnom = 'Exponencial Decreciente'
e = np.linspace(0, 1.5, 10)
expd = np.exp(-e)

cinnom = 'Exponencial Creciente'
expc = np.exp(e)

tinnom = 'Sin(x)/(x)'
s = np.linspace(-10, 10, 50)
sin = np.sin(s)/(s)

winnom = 'Escalon'
es = np.arange(0, 10, 0.5)
esc = np.piecewise(es, es >= 5, [1,0])

signom = 'Impulso'
i = np.linspace(0, 10, 50)
imp = np.zeros(len(s))
imp[25] = 1

sig = imp
win = esc
filtered = signal.convolve(sig, win, mode='same') / sum(win)
import matplotlib.pyplot as plt
fig, (ax_orig, ax_win, ax_filt) = plt.subplots(3, 1, sharex=True)
ax_orig.plot(sig)
ax_orig.set_title(signom)
ax_orig.margins(0, 0.1)
ax_win.plot(win)
ax_win.set_title(winnom)
ax_win.margins(0, 0.1)
ax_filt.plot(filtered)
ax_filt.set_title('Señales Convolucionadas')
ax_filt.margins(0, 0.1)
fig.tight_layout()
plt.show()
