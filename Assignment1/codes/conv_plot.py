import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
from scipy import array, zeros, signal
from scipy.fftpack import fft, ifft, convolve

#If using termux
import subprocess
import shlex
#end if


#function to perform circular convolution

def conv(f, g):
  F = fft(f)
  G = fft(g)
  C = np.multiply(F,G)
  return ifft(C)

x,fs = sf.read('Sound_Noise.wav')
l = len(x)
y = np.zeros(l)
samp_freq = fs
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/samp_freq
b,a = signal.butter(order,Wn,'low')

h = np.zeros(l)
h[0] = (b[0]/a[0])
h[1] = (1/a[0])*(b[1]-a[1]*h[0])
h[2] = (1/a[0])*(b[2]-a[1]*h[1]-a[2]*h[0])
h[3] = (1/a[0])*(b[3]-a[1]*h[2]-a[2]*h[1]-a[3]*h[0])
h[4] = (1/a[0])*(b[4]-a[1]*h[3]-a[2]*h[2]-a[3]*h[1]
		-a[4]*h[0])
for i in range(5,l):
	h[i] = (1/a[0])*(-a[1]*h[i-1]-a[2]*h[i-2]-a[3]*h[i-3]-
			a[4]*h[i-4])


y = conv(x,h)
plt.plot(np.real(y))
plt.title('$y(n)$')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
#If using termux
plt.savefig('../figs/yn_conv.pdf')
plt.savefig('../figs/yn_conv.eps')
subprocess.run(shlex.split("termux-open ../figs/yn_conv.pdf"))
#else
#plt.show()
