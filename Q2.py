import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt


# region 2.a
def Empirical_F(x):
    l = len(x)
    x.sort()
    matrixAsArrays = [[x[i], (lastIndexOf(x, x[i]) + 1) * (1 / l)] for i in range(l)]

    res = np.matrix(matrixAsArrays)
    return res


def lastIndexOf(arr, val):
    for i in range(len(arr)):
        if arr[len(arr) - (i + 1)] == val:
            return len(arr) - (i + 1)
    return -1


# endregion


# region 2.b
vector = binom.rvs(n=5, p=1/6, size=20)
print(vector)
# endregion

# region 2.c
empiricalFRes = Empirical_F(vector)
print(empiricalFRes)
# endregion

# region 2.d
plt.ylim(0, 1.1)
plt.xlim(0,5)
xVector = [item.item(0) for item in empiricalFRes]
xVector.append(5)
yVector = [item.item(1) for item in empiricalFRes]
yVector.append(1)
plt.step(xVector, yVector, where='post')
# endregion
# region 2.e
y = [0, 1, 2, 3, 4, 5]
theoreticalVector = binom.cdf(y, 5, 1 / 6)
print(theoreticalVector)
# endregion

# region 2.f
plt.step(y, theoreticalVector, where='post')
plt.show()
# endregion



# print(Empirical_F(b))
