#!/usr/bin/env python3
from ctypes import *
import numpy as np
import matplotlib.pyplot as plt

libRK = np.ctypeslib.load_library("RK4.so",".")
libRK.rungekutta.argtypes = [POINTER(c_double),
                             POINTER(c_int32),
                             np.ctypeslib.ndpointer(dtype=np.float64)]
libRK.rungekutta.restype = c_void_p
a = np.zeros((1024,))
dt = POINTER(c_double)(c_double(0.01))
len = POINTER(c_int32)(c_int(1024))
libRK.rungekutta(dt, len, a)
plt.plot(a)
plt.show()
