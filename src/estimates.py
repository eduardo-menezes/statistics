## Creating the estimaters

open("DataE.py")

import DataE as dt

## Estimating beta0's variance

def varbeta0(y,ybar, x):
    sigmasqr = sigmasquared(y, ybar)
    Sxx = dt.variance(x)
    xsqr = 0
    n = len(x)
    for i in range(0,n):
        xsqr = x[i]^2 + xsqr

    varianceb0 = sigmasqr * xsqr/(n*Sxx)
    return varianceb0
## Estimating beta1's variance

def varbeta1(y,ybar):
    sigmasqr = sigmasquared(y,ybar)
    Sxx = dt.variance(x)
    varianceb1 = sigmasqr/ Sxx
    return varianceb1

## Estimating the variance of error

def sigmasquared(y,ybar):
    n = len(y)
    SSE = 0
    for i in range(0,n):
        SSE = (y[i] - ybar[i])**2  + SSE

    sigmasqr = SSE/(n-2)

    return sigmasqr