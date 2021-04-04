import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex

yn= np.loadtxt('ifft_y.dat')

plt.plot(yn)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

plt.tight_layout()

#if using termux
plt.savefig('../figs/ifft.eps')
plt.savefig('../figs/ifft.pdf')

#subprocess.run(shlex.splilt("termux-open ../Figures/ifft_yn.pdf"))

#else
plt.show()
