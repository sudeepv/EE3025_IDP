import numpy as np
from scipy import signal

#If using termux
import subprocess
import shlex
#end if

#b and a values previously obtained
b = np.array([0.00345416,0.01381663,0.02072494,0.01381663,0.00345416])
a = np.array([1.,-2.5194645,2.56083711,-1.20623537,0.22012927])

num = b
den = a

#Code below outputs the poles of the transfer function as a numpy array
#print(signal.TransferFunction(num,den).poles)
