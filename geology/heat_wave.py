import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_table('C:/Users/jooys/OneDrive/바탕 화면/workspace/geology/super_hot.txt',sep=',') ## 경로는 각자 상황에 맞게 넣어주세요

plt.plot(df['year'], df['number'], 'ro-')
plt.title("The number of Heat Wave")
plt.grid()
plt.xlabel('year')
plt.ylabel('number')
plt.show()