graph()
#Graph function up here because it's easier to use with foxdot
import matplotlib
import matplotlib.pyplot as plt
import math
import random as r
import numpy as nup
#
from FoxDot import *
plt.cla()#clears graph, just in case
#import FoxDot as fd
#from FoxDot import *
LHP= -4 #-3  # Left-hand endpoint of plot
RHP= 0.25#-3   # Right-hand endpoint of plot
XGRID = 5000  # Number of values to plot in x-direction
RES = (RHP-LHP)/XGRID # resolution, i.e., distance between x-values
OUT = 50    # number of iterates to throw out
IN = 100      # number of iterates to plot
x_0 = 0#3.14159/2 # default is 0
def f(x,c):
    return c*math.cos(x)
    #return x**2 + c
#    return c*math.sin(x)
    #c*(x - (x**3) /3)
	#sin:    c*math.sin(x)
	#quadratic:
    #return x**2 + c
    #return c*(x - (x**3) /3)
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
def lfoGenv2(lforange,size,roundTo=4,type='standard'):
    lfoReturn = []
    plotw = []
    samplerate = len(yPoints)/size
    toAdd = 0
    for j in yPoints[0::int(samplerate)]:
        plotw.append(j)
        if type == 'standard':
            toAdd = nup.interp(j,[btm,top],[lforange[0],lforange[1]])
            lfoReturn.append(float(round(toAdd,roundTo)))
        elif type == 'arp':
            toAdd = (round(toAdd,roundTo) % samplerate) + 1
            lfoReturn.append(toAdd)
    return lfoReturn
#
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
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
#
def toInt(list):
    return [int(i) for i in list]
#for use with sequencing
#just a quick tool for generating patterns, although I'll admit, your milage
#will vary graph to graph
def sequenceGen(x):
    return [1 if i > 0 else 0 for i in x]
def playGen(x,str1,str2):
    outList = []
    binary = sequenceGen(x)
    for i in binary:
        if i == 0:
            outList.append(str1)
        elif i == 1:
            outList.append(str2)
    return outList


#get absolute value, for parameters that don't like negative numbers
def absList(x):
    return [abs(i) for i in x]
#lfos = lfoGen(3,[3,11,9],[(20,127),(1,13),(-1,1)],[100,19,3],[0,0,0])
# for i in lfos:
#     lfoInts.append([])
#     for j in i:
#         lfoInts[counter].append(int(j))
#     counter += 1
lfo1 = lfoGenv2([-24,24],50,4)
lfo2 = lfoGenv2([-1,1],100,4)
lfo3 = lfoGenv2([1,3],3,1,'arp')
lfo4 = lfoGenv2([1,13],11,0)
lfo1Int = toInt(lfo1)
lfo2Int = toInt(lfo2)
lfo3Int = toInt(lfo3)
seq1 = playGen(lfo1,'x','-')
#plfos = plfoGen(lfos)

"""
Everything below here is foxdot-related code
and is poorly organized
"""




lfoInts = []
counter = 0

#below are some reasonable patterns I've been able to create with this specific function and resolution

p1 >> pluck(P[lfo1[::15]], dur=[1/4], amp=2, pan=[lfo2],reverb=[0.5,0.8], delay =-0.5,oct=5, root = var(lfo1Int[:8],[4]))
p2 >> bass(P[lfo1[::20]], dur=[1/2], amp=0.8, oct=5, dist=20, shape = 0.1 ,root = var(lfo1Int[:8],[4])).stutter(1,2)
d1 >> play(seq1[::3])

p1 >> sinepad(P[lfo4] + P[lfo4], dur=1/8, amp=0.7, delay=0.7,lpf=900, reverb=[0.5,0.8], oct=6, root = var([-5,-7,-10,-12],[4,4,2,1.5]))

p1 >> dirt(P[lfos[:3]], dur=[1/6], amp=1.2, reverb=[0.5,0.8], oct=[6], root = var(lfo1Int,[4]))


print(SynthDefs)


d1 = Player()

Clock.bpm = 120


print(lfo2)
rootI =
p1 >> arpy(P[lfos[:3]], dur=[1/6], amp=2, reverb=[0.5,0.8], oct=7, root = var(lfo1Int,[4]))

graph()

print(lfo3)

p1 >> pluck(lfo1Int, dur=lfo1, scale = Scale.minor)


p1 >> pluck(lfo1Int, dur=1/2, scale = Scale.yu)
p2 >> bass(orbitY)
print(type(lfo1))

p1 = Player()
p1 >> arpy(P[lfo1])


playArp(plfo[0],plfo[1])

p1 >> pluck()

plotX = lfoGen(3,[3,5,7],[(20,127),(1,13),(-1,1)],[100,19,3],[0,4,0], xory="x")

p1 >> arpy(lfo[2] + (lfo[0]), dur=[1.5/noteLength], scale = Scale.minor, amp=5)
print(lfo[0])

p1 >> pluck(lfo1Int)

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
