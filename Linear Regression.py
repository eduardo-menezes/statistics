## Aqui vamos resolver o problema de regressão linear
## vamos definir uma função que recebe dados

open("DataE.py")
import DataE as dt
import numpy as np

def linearmodel(x,y):

    #Calculando as medidas de cada vetor
    Ex = dt.mean(x)
    Ey = dt.mean(y)

    #Estimando o coeficiente angular

    beta1 = dt.covariance(x,y) / dt.variance(x)

    #Estimando o coeficiente linear

    beta0 = Ey - beta1*Ex


    yy  = np.zeros(len(x))
    print(yy)
    for i in range(0, len(x)):
        yy[i] = beta0 + beta1*x[i]
        print(yy)

    return yy

