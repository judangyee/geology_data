import pandas as pd
import matplotlib.pyplot as plt
from sympy import *


dfh = pd.read_table('C:/Users/jooys/OneDrive/바탕 화면/workspace/geology/super_hot.txt',sep=',')
dfs = pd.read_table('C:/Users/jooys/OneDrive/바탕 화면/workspace/geology/sl_d_avg_new.txt',sep=',')

fYh = dfh['number'] +3 #폭염횟수 그래프
fYs = dfs['temp'] + 3 #해수면 스래프

plt.plot(diff(fYs),'ro-',label = 'sea level')
plt.plot(diff(fYh), 'go-', label = 'Heat wave')
plt.title('Diff of The number of Heat wave & Sea Level')
plt.xlabel('year')
plt.ylabel('diff')
plt.legend()
plt.show()