import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex

def to_complex(field):
        field = str(field)[2:]
        field = field[0 : len(field) - 1]
        return complex(field.replace('+-', '-').replace('i', 'j'))

X_k = np.loadtxt('fft_x.dat', converters={0: to_complex}, dtype = np.complex128, delimiter = '\n')
H_k = np.loadtxt('fft_h.dat', converters={0: to_complex}, dtype = np.complex128, delimiter = '\n')
X_k = np.fft.fftshift(X_k)
H_k = np.fft.fftshift(H_k)


plt.subplot(2,1,1)
plt.plot(np.linspace(-np.pi,np.pi,len(X_k)),abs(X_k))
plt.grid()
plt.xlabel("$\omega$")
plt.ylabel("|X($\omega$)|")

plt.subplot(2,1,2)
plt.plot(np.linspace(-np.pi,np.pi,len(H_k)),abs(H_k))
plt.grid()
plt.xlabel("$\omega$")
plt.ylabel("|H($\omega$)|")
plt.tight_layout()

#if using termux
plt.savefig('../figs/fft.eps')
plt.savefig('../figs/fft.pdf')

subprocess.run(shlex.splilt("termux-open ../Figures/Hk.pdf"))

#else
#plt.show()
