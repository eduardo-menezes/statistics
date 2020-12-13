# Vamos ler um arquivo csv

import DataE as dt
import pandas as pd
import matplotlib.pyplot as plt

url = "C:/Users/eduar/PycharmProjects/pythonProject1/Anscombe_quartet_data.csv"
data = pd.read_csv(url)


x123 = data['x123'].values
y1 = data['y1'].values
y2 = data['y2'].values
y3 = data['y3'].values
x4 = data['x4'].values
y4 = data['y4'].values

dt.pearson(x123, y3)


plt.figure(figsize=(4, 4), dpi=100)
#plt.scatter(x123, y1,  color='gray') #realiza o plot do gráfico de dispersão
#plt.scatter(x123, y2,  color='gray')
plt.scatter(x123, y3,  color='gray')
#plt.scatter(x4, y4,  color='gray')
plt.show()