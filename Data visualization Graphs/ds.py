import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation
from itertools import count
import random
x=[]
y=[]
index=count()
def animate():
    x.append(next(index))
    y.append(np.random.randint(0,5))
    plt.plot(x,y)
ani=FuncAnimation(plt.gcf(),animate,interval=1000)
plt.show()
