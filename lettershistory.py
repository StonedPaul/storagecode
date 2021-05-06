import collections
import re
import matplotlib.pyplot as plt
import numpy as np

words = re.findall(r'\w+', open('textfile.txt').read().lower())
amount = collections.Counter(words)

#plt.bar(amount.keys(), amount.values())
print(amount)
#plt.show()
