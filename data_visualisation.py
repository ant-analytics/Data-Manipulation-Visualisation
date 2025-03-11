import pandas as pd
import matplotlib.pyplot as plt

# load data
with plt.xkcd():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    ax.set_title('Simple plot')
    plt.show()
    