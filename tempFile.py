from matplotlib import pyplot as plt
import numpy as np
def pltFunc():
    ang_freq=20
    times=5
    v1 = np.sin(ang_freq * times) #V_0sin(wt)
    v2 = ang_freq * np.cos(ang_freq * times)
    fig, axs = plt.subplots(2, sharex = True)
    fig.suptitle('Sinusoidal driving wave')
    axs[0].plot(times, v1)
    axs[0].set_title('Input voltage $V_1$')
    axs[0].set_ylabel('Voltage / V')
    axs[0].autoscale(enable=True, axis='x', tight=True)
    axs[1].plot(times, v2)
    axs[1].set_title('Output voltage $V_2$')
    axs[1].set_ylabel('Voltage / V')
    axs[1].autoscale(enable=True, axis='x', tight=True)
    plt.xlabel('Times / s')
    plt.show()

def testPlot():
    plt.plotfile(fname, ('date', 'volume', 'adj_close'))
    plt.plot([1, 0, 0, 4])
    plt.ylabel('some numbers')
    plt.show()    


def newPlot():
    ang_freq=np.pi
    times=np.linspace(0,5)
    
    v1=np.sin(ang_freq*times)

def dotStyle():
    plt.plot([y for y in range(10)],[x*3+8 for x in range(10)],'ro') 
    plt.axis([0, 100, 0, 100]) 
    plt.show()


def twoPlots():
    times=np.linspace(0,10)
    values1=5*times
    values2=2*times+times*times+1.5
    fig,axs=plt.subplots(2,sharex= True)
    fig.suptitle('Welcome to split graph')
    axs[0].plot(times,values1)
    axs[0].set_title('some title')
    axs[0].set_yticks([min(values1),0,max(values1)])
    axs[0].set_yticklabels(['$-V_0$','0','$V_0$'])
    axs[1].plot(times,values2)
    axs[1].set_title('some title 2')
    axs[1].set_yticks([min(values2),0,max(values2)])
    axs[1].set_yticklabels(['s$-V_0$','0','s$V_0$'])
    plt.xlabel('Hours')
    plt.show()

twoPlots()


