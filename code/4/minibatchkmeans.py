"""adapted from Béjar:K-means vs Mini Batch K-means: A comparison,
http://upcommons.upc.edu/bitstream/handle/2117/23414/R13-8.pdf

Given: k, mini-batch-size b, iterations t, data set X

Initialize each c E C with an x picked randomly from X
v <- 0
for i=1..t
    M <- b examples picked randomly from X
    for x E M
        d[x] <- f(C,x)
    for x E M
        c <- d[x]
        v[c] <- v[c] + 1
        η <- 1/(v[c])
        c = (1-η)c + ηx
"""

import table_reader


k,b,t,v = 20,1,10,0


def minibatchkmeans(X):
    for i in range(1,t):
        for b_ in range(0,b):
            M = X.__getRandomSample__()
        for x in M:
            C = f(C,x)          //catch center
        for x in M:
            c = C[x]
            v[x] = v[x] + 1
            n = 1/v[c]
            c = (1-n)*c + n*x

def f(C,x):
    return x //to be corrected