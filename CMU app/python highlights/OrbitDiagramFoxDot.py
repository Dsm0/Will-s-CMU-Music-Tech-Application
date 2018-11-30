import matplotlib
import matplotlib.pyplot as plt
import math
import random as r
import numpy as nup
#
from FoxDot import *
#import FoxDot as fd
#from FoxDot import *
LHP= -2  # Left-hand endpoint of plot
RHP= 0.25   # Right-hand endpoint of plot
XGRID = 5000  # Number of values to plot in x-direction
RES = (RHP-LHP)/XGRID # resolution, i.e., distance between x-values
OUT = 50    # number of iterates to throw out
IN = 100      # number of iterates to plot
x_0 = 0#3.14159/2 # default is 0
minFreq = 220
maxFreq = 440
def f(x,c):
    #return c*math.cos(x) + c
    #return c*math.sin(x)
    #c*(x - (x**3) /3)
	#sin:    c*math.sin(x)
	#quadratic:
    return x**2 + c
	#cos:	 c*math.cos(x)
xPoints = []
yPoints = []
for i in range(XGRID):
    c = RHP - i*RES
    x = x_0
    for j in range(OUT):
        x = f(x,c)
    for j in range(IN):
        x = f(x,c)
    #    print(x)
        xPoints.append(c)
        yPoints.append(x)
def lfoGen(numLFOs,params,lfoRanges,lfoSizes,roundTo,xory="y"):
    lfoReturn = []
    plotw = []
    for i in range(numLFOs):
        lfoReturn.append([])
        plotw.append([])
        lfoSkip = len(yPoints)/lfoSizes[i]
        for j in yPoints[0::round(lfoSkip)]:
            plotw[i].append(j)
            toAdd = nup.interp(j,[btm,top],[lfoRanges[i][0],lfoRanges[i][1]])
            toAdd = round(toAdd,roundTo[i]) % params[i]
            lfoReturn[i].append(toAdd)
    if(xory == "x"):
        return plotw
    else:
        return lfoReturn
#
#Important bit right here:::
#"""Parameters in order:
#lfoGen(numLFOs,params,lfoRanges,lfoSizes,roundTo,xory="y")
#example) lfo = lfoGen(3,[3,5,7],[(20,127),(1,13),(-1,1)],[100,19,3],[0,4,0])
#numLFOs:: Int : the number of LFOs you want generated
#params:: List :: the multiples of values of yPoints you want
#lfoRanges :: List of tuple pairs :: the min and max values for each lfo
#lfoSizes :: list :: the length of pattern you want
#roundTo :: List :: the decimal you want each value of the lfo to be rounded to#
#output is list of lists, values generated according to the perameters
#"""
#Constant
#notes = interval[0::a]
#notesAsList = notes
#notes = Pattern(notes)
#timeInSec = (bpm/60)/noteLength
bpm = 120
Clock.bpm = bpm
p1 = Player()
prev = 0
arp = 0
interval = []
btm = min(yPoints)
top = max(yPoints)
#length = len(interval)
a = 50 #every __th value (higher number=less inaccurate)
bpm = 120
noteLength = 4 #ie: 32 would be a 32nd note, larger is quicker
#just a meathod of pattern generation I was messsing wiht
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
def printPitch():
    for i in notesAsList:
        print(i)
        time.sleep(1/(noteLength*4))
def graph():
    plt.scatter(xPoints,yPoints,marker='o', s=.05)
    #plt.scatter(plotX[0],lfo[0],marker='o', s=1, color="blue")
    #plt.scatter(plotX[1],lfo[1],marker='x', s=1, color="red")
    #plt.scatter(plotX[2],lfo[2],marker='+', s=1, color="green")
    #plt.axvline(x=4.2,color='red')
    plt.show()
def playArp(notes,durations):
    p1 >> arpy(notes, dur=durations, scale = Scale.chromatic)
def plfoGen(lfo):
    plfo=[]
    for i in range(len(lfo)):
        plfo.append(Pattern(lfo[i]))
    return plfo
#
"""
Stuff that just didn't pan out
def quickGen(input, lengthOfList):
    choice = r.choice(input)
    if choice <=1:
        return quickGen(input,lengthOfList)
    else:
        return r.sample(range(abs(math.ceil(choice))*1000), lengthOfList)
def tooBoredToWriteLFOs(numLFOs,seedSet=0):
    params = []
    lfoRanges = []
    lfoSizes = []
    roundTo = []
    if(seedSet != 0):
        r.seed(seedSet)
    else:
        r.seed()
    params.append(quickGen(yPoints,numLFOs))
    lfoRanges.append([quickGen(yPoints,2) for i in range(numLFOs)])
    lfoSizes.append(quickGen(yPoints,numLFOs))
    roundTo = [r.randint(0,5) for i in range(3)]
    return [numLFOs, params, lfoRanges, lfoSizes, roundTo]
#there's a list type in FoxDot called "pattern". It's a little more versitile then a list. Might as well get patterns too then.
lazyLFO = tooBoredToWriteLFOs(3)
lfo = lfoGen(lazyLFO[0],lazyLFO[1],lazyLFO[2],lazyLFO[3],lazyLFO[4])
"""
lfos = lfoGen(3,[3,11,9],[(20,127),(1,13),(-1,1)],[100,19,3],[0,0,0])
plfos = plfoGen(lfos)
lfoInts = []
counter = 0
for i in lfos:
    lfoInts.append([])
    for j in i:
        lfoInts[counter].append(int(j))
    counter += 1

print(lfoInts[1])

int
d1 >> play('x([---]--:)x')

p1 >> arpy(P[lfoInts[0]] + P[lfoInts[2]], dur=P[lfoInts[1]]/16 + 1/16, amp=2,reverb=[0.5,0.8], oct=4)

playArp(plfo[0],plfo[1])

p1 >> pluck(lfo[0:3])


if __name__=='__main__':
    #Thread(target = printPitch).start()
    Thread(target = playArp(plfo[0],plfo[1])).start()
    Thread(target = graph).start()
#older function
def oldFreqGen(xPoint,yPoint):
    for i in yPoint:
        freq = nup.interp(i,[btm,top],[20,127])
        interval.append(round(freq,3))

"""
mess with FoxDot stuff here
"""

plotX = lfoGen(3,[3,5,7],[(20,127),(1,13),(-1,1)],[100,19,3],[0,4,0], xory="x")

p1 >> arpy(lfo[2] + (lfo[0]), dur=[1.5/noteLength], scale = Scale.minor, amp=5)
print(lfo[0])


p1 >> pluck(lfo[0])

"""
mess with FoxDot stuff here
"""
