from statistics import mean
# import numpy as np
# xs = np.array([1,2,3,4,5], dtype=np.float64)
# ys = np.array([5,4,6,5,6], dtype=np.float64)

# Note that all inputs to this function are numpy arrays
def LOBF_m_b(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)**2) - mean(xs**2)))

    b = mean(ys) - m*mean(xs)

    return m, b
# Note that all inputs to this function are numpy arrays
def squared_error(ys_orig,ys_line):
    return sum((ys_line - ys_orig) * (ys_line - ys_orig))

# Note that all inputs to this function are numpy arrays
def coefficient_of_determination(ys_orig,ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr/squared_error_y_mean)