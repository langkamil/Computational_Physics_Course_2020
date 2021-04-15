import numpy as np
import matplotlib.pyplot as plt

#implementacja rownania rozniczkowego
def oscillator(x, t, kappa, omega):
    return x[1],-kappa*x[1] - omega**2*x[0]  #return [dx/dt, dv/dt]

#implementacja metody eulera 
def euler(x, func, t, kappa, omega, h):
    y = func(x,t,kappa,omega)
    return x[0] + h*y[0], x[1]+ h*y[1] 


def osc_anal(amplitude, omega, t):
    return amplitude*np.cos(omega*t)

def vel_anal(amplitude, omega, t):
    return -amplitude*omega*np.sin(omega*t)

#funkcja przedstawiajaca wykres
def solution(method, equation, kappa, omega, h, n, amplitude):
    
    t = np.arange(0, n*h, h) #przedzial czasu
    x = np.zeros((n,2))  #tablica dwuwymiarowa z zerami
    
    x[0][0] = amplitude              
    
    for i in range(n - 1): 
        x[i+1] = method(x[i],oscillator, t[i], kappa, omega, h)

    plt.plot(t, x[:,0], 'r', label = "Metoda Eulera")
    plt.plot(t, osc_anal(amplitude, omega, t), 'b', label = 'Metoda analityczna')
    plt.xlabel("$t$")
    plt.ylabel("$x(t)$")
    plt.legend(loc='lower left')
    plt.grid()
    plt.show()

#portret fazowy
def phase_portrait(amplitude, omega):

    t = np.linspace(1.0, 11.0)
    plt.plot(osc_anal(amplitude,omega,t), vel_anal(amplitude,omega,t), 'b')
    plt.xlabel("$x(t)$")
    plt.ylabel("$dx(t)/dt$")
    plt.grid()
    plt.show()
      
 

def ErrorInTime(method, equation, kappa, omega, h, n, amplitude):
    
    t = np.arange(0, n*h, h) #przedzial czasu
    x = np.zeros((n,2))  #tablica dwuwymiarowa z zerami
    y = []
    z = []
    x[0][0] = amplitude              
    
    for i in range(n -1 ): 
        x[i+1] = method(x[i],oscillator, t[i] , kappa, omega, h)
        y.append(x[i][0])
        z.append(abs(y[i]-osc_anal(amplitude,omega,t[i])))

    plt.plot(z, 'r')
    plt.xlabel("$t$")
    plt.ylabel("$roznica$")
    plt.ylim(0,0.2)
    plt.grid()
    plt.show()


def global_error(method, equation, kappa, omega, n, amplitude):

    sum = []
    h = [T/500,T/300,T/200,T/100,T/70,T/50]

    for j in range(5):
        s = 0
        t = np.arange(0, n*h[j], h[j]) #przedzial czasu
        x = np.zeros((n,2))  #tablica dwuwymiarowa z zerami
        y = []
        x[0][0] = amplitude              
    
        for i in range(n-1): 
            x[i+1] = method(x[i],oscillator, t[i] , kappa, omega, h[j])
            y.append(x[i][0])
            s = abs(y[i]-osc_anal(amplitude,omega,t[i])) + s
        sum.append(s)
    plt.plot(h,sum, 'r')
    plt.xlabel("$h$")
    plt.ylabel("blad globalny")
    plt.grid()
    plt.show()


n = 100
kappa = 0 #oscylator nietlumiony
omega = np.sqrt(9.9/25) #wtedy T~10 
T = 2*np.pi/omega
global_error(euler,oscillator,kappa,omega,n,1)