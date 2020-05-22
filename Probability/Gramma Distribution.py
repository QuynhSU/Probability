from scipy.stats import gamma
import seaborn as sns
import matplotlib.pyplot as plt
data_gram = gamma.rvs(a= 5, size =1000)
ax = sns.distplot(data_gram, kde= True, bins=100, color = 'skyblue', hist_kws={"linewidth":15, 'alpha':1})
ax.set(xlabel= 'Gamma Distribution', ylabel='Frequency')

plt.show()