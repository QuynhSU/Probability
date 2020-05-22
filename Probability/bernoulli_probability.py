from scipy.stats import bernoulli
import seaborn as sb
import matplotlib.pyplot as plt

data_bern = bernoulli.rvs(size=1000, p =0.6)
# plt.plot(data_bern)
# plt.show()

ax = sb.distplot(data_bern, kde = True,color= 'crimson', hist_kws={"linewidth": 25, "alpha": 1})
ax.set(xlabel= "Bernouli", yLabel ="Frequency")
plt.show()
