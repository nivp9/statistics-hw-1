import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
import pandas as pd

path = './assets/appendicitis.csv'
df = pd.read_csv(path)
# print(df)


# region 3 a
val_count = df['Pathology'].value_counts()
# print(val_count[2]/(val_count[1]+val_count[2]))
# endregion

# region 3 b
grouped_multiple = df.groupby(['Sex', 'Pathology']).count()
print(grouped_multiple)
# endregion

# region 3 c
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
labels = ['{}-{}'.format(i, j) for i, j in zip(bins[:-1], bins[1:])]
b = pd.cut(df['Age'], bins=bins, labels=labels, include_lowest=True)
x = df.groupby(['Sex', 'Pathology', b]).size().unstack(fill_value=0).stack().reset_index(name='count')
print(x)


# ind = np.digitize(df['Age'], bins)

# endregion

# region bonus

def Empirical_F(x):
    l = len(x)
    x.sort()
    return x, [(lastIndexOf(x, x[i]) + 1) * (1 / l) for i in range(l)]


def lastIndexOf(arr, val):
    for i in range(len(arr)):
        if arr[len(arr) - (i + 1)] == val:
            return len(arr) - (i + 1)
    return -1


women_ages = list(df[df['Sex'] == 'Female']['Age'])
men_ages = list(df[df['Sex'] == 'Male']['Age'])
x_women, y_women = Empirical_F(women_ages)
x_men, y_men = Empirical_F(men_ages)
plt.plot(x_women, y_women, label='Women')
plt.plot(x_men, y_men, label='Men')
plt.xlabel('Age')
plt.ylabel('Empirical distribution')
plt.title('Empirical distribution of the age of appendicitis patients')
plt.legend()
plt.show()

# endregion
