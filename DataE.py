""""

DataScience function

"""

import numpy as np

# funcao que calcula a media
def mean(x):

    m = 0 #cria uma variavel para acumular a soma
    for i in range(0,len(x)):

        m = (x[i] + m) #soma os valores

    mm = m/len(x)  #divide a soma pelo quantidade de valores
    return mm


def variance(x):
    n = len(x) #quantidade de valores
    mi = 0
    for i in range(0,n):
        mi = (x[i] + mi)

    mbar = mi / n #media

    mj = 0 #variavel auxiliar para acumular no loop
    for j in range(0,n):
        mj = (x[j] - mbar)**2 + mj

    sbar = mj/n #divide o valor acumulado pela quantidade de numeros
    print(sbar)

    return sbar

def covariance(x,y):
    n = nx = ny =  len(x) #quantidade de valores de x

    mi = 0
    for i in range(0,nx):
        mi = (x[i] + mi)

    xbar = mi / nx #media

    mj = 0
    for j in range(0,ny):
        mj = (y[j] + mj)

    ybar = mj / ny #media

    mk = 0 #variavel auxiliar para acumular no loop
    for k in range(0,n):
        mk = (x[k] - xbar)*(y[k] - ybar) + mk

    sxy = mk/(n-1) #divide o valor acumulado pela quantidade de numeros
    print(sxy)

    return sxy

def pearson(x,y): #função que calcula o coeficiente de Pearson / Function that calculates Pearson's coefficient

    n = nx = ny = len(x)
    mi = 0
    mj = 0
    xsqr = 0
    ysqr = 0

    for i in range(0,n):

        mi = (x[i] + mi)
        mj = (y[i]+ mj)
        xsqr = x[i]**2 + xsqr
        ysqr = y[i]**2 + ysqr

    xbar = mi/n  # media x
    ybar = mj/n  # media y

    xy = 0
    for j in range(0,n):
        xy = x[j]*y[j] + xy

    r = (xy - (n * xbar * ybar)) / (np.sqrt(xsqr - n * xbar ** 2) * np.sqrt(ysqr - n * ybar ** 2))
    print(r)

    return r


a = [1,2]
b = [1,2]
covariance(a,b)
pearson(a,b)

