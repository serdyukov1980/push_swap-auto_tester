import numpy as np
import scipy.stats
with open("test", "r") as file:

    arr = []
    for line in file:
        arr.append(int(line))
a = np.array(arr)
mean, var, std = scipy.stats.mvsdist(a)
print("result: {:.2f} {} {:.2f}, max: {}, min: {}".format(mean.mean(), u"\u00B1", std.std()*3, max(a), min(a)))
from matplotlib import pyplot as plt
#a = np.expand_dims(a, axis=1)
plt.hist(a, bins=100)
plt.show()


