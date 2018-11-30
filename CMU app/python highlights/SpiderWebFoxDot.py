import matplotlib
import matplotlib.pyplot as plt
import numpy as nup
import math
import sys
from FoxDot import *
#
LHP= -5  # Left-hand endpoint of plot
RHP= 5   # Right-hand endpoint of plot
#
XGRID = 100  # Number of values to plot in x-direction
RES = (RHP-LHP)/XGRID # resolution, i.e., distance between x-values
OUT = 50    # number of iterates to throw out
IN = 100      # number of iterates to plot
p1list = []
p2list = []
btm = -5
top = 5
#
plt.ylim(top=top)  # adjust the top leaving bottom unchanged
plt.ylim(bottom=btm)  # adjust the bottom leaving top unchanged
plt.xlim(right=RHP)  # adjust the top leaving bottom unchanged
plt.xlim(left=LHP)  # adjust the bottom leaving top unchanged
#
x_0 = 2 # default is 0
#
c = -3
#
def f(x):
    #return x**2 + c
    #c*math.cos(x)
    #c*(x - (x**3) /3)
	#sin:
    return c*math.sin(x)
	#quadratic:  x**2 + cx`
	#cos:	 c*math.cos(x)
#
xPoints = []
yPoints = []
#
xStart = LHP
#
for i in range(1000):
    x = LHP + i*(RES)
    xPoints.append(x)
    x = f(x)
    yPoints.append(x)
plt.plot(x,x)
#plt.scatter(xPoints,yPoints,marker='o', s=.05)
plt.plot(xPoints,yPoints)
#
for i in range(XGRID):
    #print("inhere")
    p1 = x_0
#    print("p1  " , p1)
    p2 = f(x_0)
#    print("p2  " , p2)
    x_0 = p2
    if p2 > 10**50:
     next(range(XGRID), None)
    p1list.append(p1)
    p2list.append(p2)
    plt.plot([p1,p1],[p1,p2], color='violet')
    plt.plot([p1,p2],[p2,p2], color='violet')
    #plt.axvline(x=p1, ymin=p1, ymax=p2,color='green')
    #plt.axhline(y=p1,xmin=p2,xmax=p2 ,color='green')
def graph():
    plt.axhline(y=p1,xmin=p2,xmax=p2 ,color='green')
    plt.plot(xPoints, xPoints, color='blue')
    plt.scatter(xandyUsed[0],xandyUsed[1], s=0.1)
    plt.show()
#generates 2 lfos based on xposition and yposition, and ranges assigned for each value to oscillate between
def webLFOGen(xrange,yrange,sampleRate,maxOrbit=5):
    outAll = []
    outX = []
    outY = []
    global xandyUsed
    xandyUsed = [[],[]]
    orbitCount = 0
    for j in enumerate(yPoints[0::sampleRate]):
        #plotw[i].append(j)
        toAddx = nup.interp(xPoints[j[0]],[btm,top],[xrange[0],xrange[1]])
        xandyUsed[0].append(xPoints[j[0]])
        toAddy = nup.interp(j[1],[btm,top],[yrange[0],yrange[1]])
        xandyUsed[1].append(j[1])
    #    toAdd = toAdd.real.astype(int)
        #toAdd = int(toAdd) % params[i]
        outX.append(toAddx)
        outY.append(toAddy)
        prev = toAddx
        #function to make sure that if it starts orbiting, it doesn't go on forever
        if prev == toAddx:
            orbitCount += 1
            if orbitCount == maxOrbit:
                outAll.append(outX)
                outAll.append(outY)
                return(outAll)
        else:
            orbitCount = 0
    outAll.append(outX)
    outAll.append(outY)
    return(outAll)
#turns list of anything into a list of integers
def toInt(list):
    return [int(round(i)) for i in list]
#for use with sequencing
def sequenceGen(x):
    return [i if i > 0 else -1 for i in x]
def absList(x):
    return [abs(i) for i in x]
lfos = webLFOGen([1,50],[-1,1],20)
lfosInts = [toInt(i) for i in lfos]
lfoSeqX = sequenceGen(xPoints)
lfoSeqY = sequenceGen(yPoints)

graph()

print(lfosInts[1])
p1 = Player()
p1 >> pluck(lfosInts[0], amp=absList(lfos[1]))



print(ServerManager)
