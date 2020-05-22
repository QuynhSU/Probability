from scipy.stats import binom
import seaborn as sns
import matplotlib.pyplot as plt
data_binom = binom.rvs(n=10, p = 0.8, size = 10000)

ax = sns.distplot(data_binom, kde= False, color = 'skyblue', hist_kws ={"linewidth":15, 'alpha': 1})
ax.set(xlabel="Binomial Distribution", ylabel = 'Frequency')
plt.show()