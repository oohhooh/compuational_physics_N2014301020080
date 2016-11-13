import math 
import matplotlib.pyplot as plt 
g=9.8 
dt=0.01 
def adjust(theta): 
    while theta>math.pi: 
        theta=theta-2*math.pi 
    while theta<-math.pi: 
        theta=theta+2*math.pi 
        return theta 
def EC(omega0,theta0,q,l,FD,omegaD,T): 
    motion=[[]for i in range(3)] 
    motion[0].append(omega0) 
    motion1.append(theta0) 
    motion2.append(0) 
    while motion2[-1]<=T: 
        motion[0].append(motion[0][-1]+(-g*math.sin(motion1[-1])/l-q*motion[0][-1]+FD*math.sin(omegaD*motion2[-1]))*dt) 
        motion1.append(motion1[-1]+motion[0][-1]*dt) 
        motion2.append(motion2[-1]+dt) 
        return motion#omega,theta,t

omegaD=float(2.0/3) 
T=1000 
def Poin(motion): 
    poi=[[]for i in range(3)] 
    for n in range(int(omegaD*T/2/math.pi)): 
        number=int(round(2*n*math.pi/omegaD/dt)) 
        poi[0].append(motion[0][number]) 
        poi1.append(motion1[number]) 
        poi2.append(motion2[number]) 
        return poi

def bif(motion,FD): 
    m=[[]for i in range(2)]#FD,theta 
    for j in range(30,60): 
        num=int(round(2*j*math.pi/omegaD/dt)) 
        m[0].append(FD) 
        m1.append(motion1[num]) 
        return m 
    for i in range(150): 
        F_D=1.35+i*0.001 
        d=EC(0,0.2,0.5,9.8,F_D,2.0/3,600) 
        b=bif(d,F_D) 
        plt.plot(b[0],map(adjust,b1),'.',markersize=3.0,color='black')

plt.title('Bifurcation diagram  versus ') 
plt.xlim(1.35,1.50) 
plt.ylim(1,3) 
plt.show()   