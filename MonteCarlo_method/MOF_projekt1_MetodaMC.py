import random       
import matplotlib.pyplot as plt 
import numpy as np

#implementacja funkcji ktora calkujemy
def function(x):
    return x**5 

#implementacja calkowania MC
def MC_integration(x0, xk, N):

    count = 0
    dx = xk - x0
    y = []

  #generowanie tablicy liczb losowych
    for j in range(N):
        y.append(random.uniform(x0,xk))

  #obliczanie wartosci funkcji
    for i in range(N):
        count = count + function(y[i])
    return count *dx/ N

#prezentacja wynikow calkowania funkcja
def integration_results(a,b,N):
    x = []
    for i in range(1,N):
        x.append(MC_integration(a,b,i))

    plt.plot(x,'ro',color='blue', markersize = 1.5)
    plt.plot([0,N],[0.1640625,0.1640625],color = 'red' ,linewidth = 0.8)
    plt.grid()
    plt.xlabel('$N$')
    plt.ylabel('$I$')
    plt.show()


#srednia wynikow
def mean(a,b,N,K):
    y = []
    for i in range(1, N):  
        y.append(0)
        for j in range(1,K):       
            y[i-1] = (y[i-1] + MC_integration(a, b, i)) #sumowanie K-krotne wynikow calkowania dla N = i
        y[i-1] = y[i-1]/K       #srednia z sumowania

    plt.plot(y,'ro',color='blue', markersize = 1.5)
    plt.plot([0,N],[0.1640625,0.1640625],color = 'red' ,linewidth = 0.8)
    plt.grid()
    plt.xlabel('$N$')
    plt.ylabel('$<I>$')
    plt.show()
 

def variance(a,b,N,K):
    y = []
    x = []
    z = np.zeros(K-1)

    for i in range(1, N):  
        y.append(0)
        x.append(0)
        #petla dla sredniej
        for j in range(1,K):
            z[j-1] = MC_integration(a, b, i)
            y[i-1] = y[i-1] + z[j-1] #sumowanie K-krotne wynikow calkowania dla N = i
        y[i-1] = y[i-1]/K #srednia z sumowania
        #petla dla wariancji
        for idx in range(1,K):
            x[i-1] = x[i-1] + (z[idx - 1] - y[i-1])**2
            z[idx-1] = 0
        x[i-1] = x[i-1]/K
     
    plt.plot(x,'ro',color='blue', markersize = 1.5)
    plt.grid()
    plt.xlabel('$N$')
    plt.ylabel('$Var(I)$')
    plt.show()


def mean_hist(a,b,N,K):
    y = []
    for i in range(1, N):  
        y.append(0)
        for j in range(1,K):       
            y[i-1] = (y[i-1] + MC_integration(a, b, i)) #sumowanie K-krotne wynikow calkowania dla N = i
        y[i-1] = y[i-1]/K       #srednia z sumowania

    plt.hist(y)
    plt.grid()
    plt.xlabel('$I$')
    plt.show()
 
    
mean(0.5,1,100,500)
