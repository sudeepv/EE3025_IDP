import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

def H(z,num_coeffs,den_coeffs):
    Num = np.polyval(num_coeffs,pow(z,-1))
    Den = np.polyval(den_coeffs,pow(z,-1))
    return Num/Den

x,fs = sf.read('Sound_Noise.wav')

omega = np.linspace(-np.pi,np.pi,len(x))
z = np.exp(1j * omega)  # z= e^{jw}

#b and a values previously obtained
b = np.array([0.00345416,0.01381663,0.02072494,0.01381663,0.00345416])
a = np.array([1.,-2.5194645,2.56083711,-1.20623537,0.22012927])

H = H(z,b,a)
#subplots
plt.plot(omega,abs(H))
plt.title('Magnitude of Impulse Frequency Response')
plt.xlabel('$\omega$')
plt.ylabel('$|H(j\omega)|$')
plt.grid()
#If using termux
plt.savefig('../figs/mag_H(jw).pdf')
plt.savefig('../figs/mag_H(jw).eps')
subprocess.run(shlex.split("termux-open ../figs/mag_H(jw).pdf"))

#else
#plt.show()
