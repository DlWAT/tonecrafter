# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:17:06 2021

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile
from scipy.signal import lfilter
from scipy.signal import butter,filtfilt
from scipy import signal
import soundfile
from scipy.fftpack import fft2, ifft2
L=[[]]

 


ass=0.4

for m in range (1,5):
    P=[]
    for i in range (2000):
        k=np.sin(-np.pi/2+4*np.pi/2000*i)+ass
        P.append(k)
        
        drive=95
        a=np.sin(((drive+1)/101)*(np.pi/2))
        k=2*a/(1-a)
        l=P[i]
        j=np.absolute(l)
        P[i]=(((1+k))*l)/((1+k*j))-ass
    L.append(P)
    plt.plot(L[m])
#    
for m in range (7):
    P=[]
    for i in range (2000):
        k=np.sin(-np.pi/2+4*np.pi/2000*i)+ass
        P.append(k)
        j=np.absolute(k)        
        if j<1/3:
            P[i]=2*k-ass
            
        elif 1/3<k<2/3:
            P[i]=(3-((2-3* P[i])**2))/3-ass
            
        elif -2/3<k<-1/3:
            P[i]=-((3+ass-((2-ass-3* (-P[i]))**2))/3)
        elif k<-2/3:
            P[i]=-(1)
            
        else:
            P[i]=1-ass
        
       
#    L.append(P)
#
#    plt.plot(L[m])



#for m in range (6):
#    P=[]
#    for i in range (2000):
#        k=-1+i*0.001
#        P.append(k)
#        
#        j=np.absolute(k)
#        d=5+5*m
#        if k==0:
#            P[i]=0
#        else:
#            P[i]=(k/j)*(1-np.exp((-d*(k**2))/j))
#    L.append(P)
#    plt.plot(L[m])            
            
            

plt.show