
import numpy as np
from My_Linear_Reg_Lib import*

xs = np.array([1,2,3,4,5], dtype=np.float64)
ys = np.array([5,4,6,5,6], dtype=np.float64)

m, b = LOBF_m_b(xs,ys)
print(round(m, 1), round(b, 1))

