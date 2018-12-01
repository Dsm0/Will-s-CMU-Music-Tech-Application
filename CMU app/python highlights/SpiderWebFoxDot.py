graph()
#Graph function up here because it's easier to use with foxdot
import matplotlib
import matplotlib.pyplot as plt
import numpy as nup
import math
import sys
from FoxDot import *
#
plt.cla()#clears graph, just in case
LHP= -5  # Left-hand endpoint of plot
RHP= 5   # Right-hand endpoint of plot
btm = -5
top = 5
#
XGRID = 1000  # Number of values to plot in x-direction
RES = (RHP-LHP)/XGRID # resolution, i.e., distance between x-values
OUT = 50    # number of iterates to throw out
IN = 100      # number of iterates to plot
#
plt.ylim(top=top)  # adjust the top leaving bottom unchanged
plt.ylim(bottom=btm)  # adjust the bottom leaving top unchanged
plt.xlim(right=RHP)  # adjust the top leaving bottom unchanged
plt.xlim(left=LHP)  # adjust the bottom leaving top unchanged
#
x_0 = math.pi/8 # default is 0
#
c = 4
#
def f(x):
#    return x**2 + c
    #c*math.cos(x)
    #return c*(x - (x**3) /3)
	#sin:
  return c*math.sin(x)
	#quadratic:  x**2 + cx`
	#cos:	 c*math.cos(x)
#
xPoints = []#list used to generate graph
yPoints = []#list used to generate graph
plistpoint1 = []
plistpoint2 = []
#
xStart = LHP
#
for i in range(1000):
    x = LHP + i*(RES)
    #print(x)
    xPoints.append(x)
    x = f(x)
    #print(x)
    yPoints.append(x)#generate the lists of points
plt.plot(x,x) #plot a line y=x, useful for looking at iteration graphs
#plt.scatter(xPoints,yPoints,marker='o', s=.05)
plt.plot(xPoints,yPoints)#plot the generated points
#
for i in range(XGRID):
    #this is the function that draws lines between the iterated points
    p1 = x_0
#    print("p1  " , p1)
    p2 = f(x_0)
#    print("p2  " , p2)
    x_0 = p2
    if p2 > 10**50: #if a y value is stupidly large, just end the loop
     print("broken")
     break
    plistpoint1.append([p1,p1])#essentially, p2 becomes p1 becomes p2, etc.
    plistpoint2.append([p1,p2])#essentially, p2 becomes p1 becomes p2, etc.
    plt.plot([p1,p1],[p1,p2], color='violet')#vertical line
    plt.plot([p1,p2],[p2,p2], color='violet')#horizontal line
def graph():
    #plt.axhline(y=p1,xmin=p2,xmax=p2 ,color='green')
    plt.plot(xPoints, xPoints, color='blue') #the function that acutally graphs the points
    plt.scatter(xandyUsed[0],xandyUsed[1], s=0.1) #plots x and y values used in the lfo generation
    plt.show()
orbits = [val for pair in zip(plistpoint1, plistpoint2) for val in pair]
orbitX = [i[0] for i in orbits]#values of X
orbitY = [i[1] for i in orbits]#values of Y
#generates 2 lfos based on xposition and yposition, and ranges assigned for each value to oscillate between
def webLFOGen(xrange,yrange,sampleRate,roundTo=2,maxOrbit=5):
    outAll = []
    outX = []#lists for x and y values to be generated
    outY = []
    global xandyUsed
    xandyUsed = [[],[]]
    orbitCount = 0
    prev=nil
    for j in enumerate(orbitY[0::sampleRate]):
        x = orbitX[j[0]]
        y = j[1]
        #print(x)
        #enumerate is helpful because it gives both the index and the value of an item in the list
        #letting me coordinate the values with the x list easier
        toAddx = nup.interp(x,[btm,top],[xrange[0],xrange[1]])#map x value to a specified range
        xandyUsed[0].append(x)
        toAddy = nup.interp(y,[btm,top],[yrange[0],yrange[1]])#map y value to a specified range
        xandyUsed[1].append(y)
        outX.append(round(toAddx,roundTo))
        outY.append(round(toAddy,roundTo))
        #function to make sure that if it starts orbiting (ie. stays at one point,
        #or oscillates between a few points), it doesn't go on forever
        try:
            if any([xandyUsed[0][j[0]] == xandyUsed[0][j[0]-i] for i in maxOrbit]):
                print("orbit reached max")
                outAll.append(outX)
                outAll.append(outY)
                return(outAll)
        except:
            #print(xandyUsed[1][j[0]])
            #print(" -- ", xandyUsed[1][j[0]-1])
            nil
    outAll.append(outX)
    outAll.append(outY)
    return(outAll)
#turns list of anything into a list of integers
#helpful for Parameters that don't like floats
def toInt(list):
    return [int(round(i)) for i in list]
#for use with sequencing
#just a quick tool for generating patterns, although I'll admit, your milage
#will vary graph to graph
def sequenceGen(x):
    return [1 if i > 0 else 0 for i in x]
#get absolute value, for parameters that don't like negative numbers
def absList(x):
    return [abs(i) for i in x]
lfos = webLFOGen([1,20],[-1,1],2)
lfos2 = webLFOGen([1,90],[-12,12],2)
lfos3 = webLFOGen([-5,5],[-5,5],1,roundTo=2,maxOrbit=5)
lfosInts = [toInt(i) for i in lfos]
lfos2Ints = [toInt(i) for i in lfos2]
lfos3Ints = [toInt(i) for i in lfos2]
lfoSeqX = sequenceGen(xPoints)
lfoSeqY = sequenceGen(yPoints)
fp1 = Player()
fp2 = Player()
fp3 = Player()


"""
Everything below here is foxdot-related code
and is poorly organized due to "improvisational tendencies"
"""

fp1 >> dirt(P[2,2], dur=[1/6], amp=1.2, reverb=[0.5,0.8], oct=[6], root = var(lfosInts[::19],[2]), scale = Scale.yu)

print(lfosInts)
print(xandyUsed)

graph()

Root.default = var(P[lfos2Ints[1][1:]],lfoSeqX)

print(seq1)

help(arpy())

fp3 >> arpy(P[lfos3[0]]*50, dur=[1/16])
fp3 >> bass(P[lfos3[0]]*10, dur=[1/16])

Clock.bpm = 144

print(p1list)

help(loop)
fp1 >> pluck(P[lfos3Ints[0]]+ P[lfos2[0]],dur=[1/i for i in absList(lfosInts[0])])
#p1.solo + (-3)
fp2 >> bass(lfos3[1] + P[], amp=absList(lfos[0]), dur = [1/2,1/2])

print(ServerManager)
