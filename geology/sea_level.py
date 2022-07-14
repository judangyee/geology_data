import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_table('C:/Users/jooys/OneDrive/바탕 화면/workspace/geology/sl_d_avg_new.txt',sep=',') ## 경로는 각자 상황에 맞게 넣어주세요

plt.plot(df['year'], df['temp'], 'bo-')
plt.title("Sea Level")
plt.grid()
plt.xlabel('year')
plt.ylabel('level')
plt.show()