import numpy as np
O = np.array([[10, 20],
              [20, 40]])
E = np.array([[11, 19],
              [19, 41]])
chi2 = np.sum((O - E)**2 / E)
print("Chi-Square Value:", chi2)
