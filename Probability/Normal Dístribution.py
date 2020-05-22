from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt
data_normal = norm.rvs(size = 10000, loc =0, scale=1)
print(data_normal)
ax = sns.distplot(data_normal,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')

plt.show()