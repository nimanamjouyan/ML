from statistics import mean
import numpy as np
from Line_Of_Best_Fit import best_fit_slope

xs = np.array([1,2,3,4,5], dtype=np.float64)
ys = np.array([5,4,6,5,6], dtype=np.float64)

m = round(best_fit_slope(xs,ys), 1)
print(m)