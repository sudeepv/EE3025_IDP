import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import soundfile as sf

#If using termux
import subprocess
import shlex

#Reading the soundfile 
input_signal, fs = sf.read('Sound_Noise.wav')
sampl_freq = fs
order = 4
n = int(len(input_signal))
n = int(2 ** np.floor(np.log2(n)))
xn = np.loadtxt('plot_xn.dat')
yn = np.loadtxt('plot_yn.dat')

#Plotting x(n) and y(n)
t = np.linspace(0, n-1,n)
plt.subplot(2,1,1)
plt.plot(t,xn)
plt.xlabel("$n$")
plt.ylabel("$x(n)$")

plt.subplot(2,1,2)
plt.plot(t,yn)
plt.xlabel("$n$")
plt.ylabel("$y(n)$")

#if using termux
plt.savefig('../figs/plot_xnyn.eps')
plt.savefig('../figs/plot_xnyn.pdf')

subprocess.run(shlex.splilt("termux-open ../figs/xn_yn.pdf"))

#else
#plt.show()

