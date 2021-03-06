
"""
This is the rough prototype for the "FIRST STAGE" of the HW Trinomial Interest Rate Tree.  The second and final stage will be 
implemented shortly and will be published in an article.  This tree building exercise will also be extended to Black Karasinski 
i.e the same tree can be used for BK.  You have to wait for the article to get a good/better feel for the implementation.  
See you next time!!!

Source: Options, Futures and Other Derivatives - John Hull Fifth Edition
        Short Rate Model Implementation & Extension - Chapter 6 by Ser-Huang Poon (Via Google Search)
"""

import sys
import math 



def initialTimeStep(years):
    initialVector = [[0]]
    timeStep = range(years)
    vectorSize = 2
    y = vectorSize
    
    for x in range(len(timeStep)):
        tracker = []
        for i in range(y+1):
            tracker.append(1)
        initialVector.append(tracker[:])
        y = y + 2
        tracker = []
    return initialVector[:]
    
print initialTimeStep(2)

"""
[[0], [1, 1, 1], [1, 1, 1, 1, 1]]

"""

j = initialTimeStep(2)

    

def interMediateTimeStep(initialTimeStep):
    interMediateTimeStep = [[0]]
    collector = []
    for x in range(1,len(initialTimeStep)):
        for y in range(len(initialTimeStep[x])):
            collector.append(x)
            x = x - 1
        interMediateTimeStep.append(collector)
        collector = []
    return interMediateTimeStep
    
g = interMediateTimeStep(j)
    
print g

"""
[[0], [1, 0, -1], [2, 1, 0, -1, -2]]

"""
vol = 0.01
a = 0.1
deltaT = 1   
deltaR = vol * math.sqrt(3 * deltaT)
M = -a * deltaT
jMax = int(math.ceil(-0.184/M))
jMin = -jMax    
    
def firstStage(interMediateTimeStep):
    firstStage = [[0.0000]]
    collector = []
    for x in range(1,len(j)):
        for y in range(len(g[x])):
            collector.append(g[x][y] * deltaR)
        firstStage.append(collector)
        collector = []
    return firstStage

trial = firstStage(g)   
           
test = [list(reversed(x)) for x in trial]



"""
                 0                    1                    2 
------------------|--------------------|--------------------|
                                          0.0346410161513775    
                                          0.0173205080756888    
                     0.0173205080756888   0.0000000000000000    
                     0.0000000000000000  -0.0173205080756888    
0.0000000000000000  -0.0173205080756888  -0.0346410161513775 


"""

"""
"""
The function called firstStage above can also be implemented using list comprehension like below:
    
q = [[deltaR * y for y in x] for x in g]

q2 = [list(reversed(x)) for x in q]

print_lattice2(q2, info = [])

                 0                    1                    2
------------------|--------------------|--------------------|
                                          0.0346410161513775    
                                          0.0173205080756888    
                     0.0173205080756888   0.0000000000000000    
                     0.0000000000000000  -0.0173205080756888    
0.0000000000000000  -0.0173205080756888  -0.0346410161513775



"""
"""




"""
If we chose 10 years ... the tree will look like so.  It is trinomial because each rate can break into three versus two in 
in the case of binomial - this is the intermediate rate *R not R so R will be build in the second stage.  The function for
printing the tree was not released or published here.

                 0                    1                    2                    3                    4                    5                    6                    7                    8                    9                   10
------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
                                                                                                                                                                                                                  0.1732050807568877                    
                                                                                                                                                                                                                  0.1558845726811990                    
                                                                                                                                                                                             0.1558845726811990   0.1385640646055102                    
                                                                                                                                                                                             0.1385640646055102   0.1212435565298214                    
                                                                                                                                                                        0.1385640646055102   0.1212435565298214   0.1039230484541326                    
                                                                                                                                                                        0.1212435565298214   0.1039230484541326   0.0866025403784439                    
                                                                                                                                                   0.1212435565298214   0.1039230484541326   0.0866025403784439   0.0692820323027551                    
                                                                                                                                                   0.1039230484541326   0.0866025403784439   0.0692820323027551   0.0519615242270663                    
                                                                                                                              0.1039230484541326   0.0866025403784439   0.0692820323027551   0.0519615242270663   0.0346410161513775                    
                                                                                                                              0.0866025403784439   0.0692820323027551   0.0519615242270663   0.0346410161513775   0.0173205080756888                    
                                                                                                         0.0866025403784439   0.0692820323027551   0.0519615242270663   0.0346410161513775   0.0173205080756888   0.0000000000000000                    
                                                                                                         0.0692820323027551   0.0519615242270663   0.0346410161513775   0.0173205080756888   0.0000000000000000  -0.0173205080756888                    
                                                                                    0.0692820323027551   0.0519615242270663   0.0346410161513775   0.0173205080756888   0.0000000000000000  -0.0173205080756888  -0.0346410161513775                    
                                                                                    0.0519615242270663   0.0346410161513775   0.0173205080756888   0.0000000000000000  -0.0173205080756888  -0.0346410161513775  -0.0519615242270663                    
                                                               0.0519615242270663   0.0346410161513775   0.0173205080756888   0.0000000000000000  -0.0173205080756888  -0.0346410161513775  -0.0519615242270663  -0.0692820323027551                    
                                                               0.0346410161513775   0.0173205080756888   0.0000000000000000  -0.0173205080756888  -0.0346410161513775  -0.0519615242270663  -0.0692820323027551  -0.0866025403784439                    
                                          0.0346410161513775   0.0173205080756888   0.0000000000000000  -0.0173205080756888  -0.0346410161513775  -0.0519615242270663  -0.0692820323027551  -0.0866025403784439  -0.1039230484541326                    
                                          0.0173205080756888   0.0000000000000000  -0.0173205080756888  -0.0346410161513775  -0.0519615242270663  -0.0692820323027551  -0.0866025403784439  -0.1039230484541326  -0.1212435565298214                    
                     0.0173205080756888   0.0000000000000000  -0.0173205080756888  -0.0346410161513775  -0.0519615242270663  -0.0692820323027551  -0.0866025403784439  -0.1039230484541326  -0.1212435565298214  -0.1385640646055102                    
                     0.0000000000000000  -0.0173205080756888  -0.0346410161513775  -0.0519615242270663  -0.0692820323027551  -0.0866025403784439  -0.1039230484541326  -0.1212435565298214  -0.1385640646055102  -0.1558845726811990                    
0.0000000000000000  -0.0173205080756888  -0.0346410161513775  -0.0519615242270663  -0.0692820323027551  -0.0866025403784439  -0.1039230484541326  -0.1212435565298214  -0.1385640646055102  -0.1558845726811990  -0.1732050807568877                    
   

"""
#Define the Probabilities.....

def pAU(j,M):
    return (1.0/6.0 + ((j**2 * M**2) + (j * M))/2.0 )
    
def pAM(j,M):
    return ((2.0/3.0) - (j**2 * M**2))
    
def pAD(j,M):
    return ((1.0/6.0) + ((j**2 * M**2) - (j * M))/2.0 )
    

def pBU(j,M):
    return (1.0/6.0 + ((j**2 * M ** 2) - (j * M))/2.0 )
    
def pBM(j,M):
    return ((-1.0/3.0) - (j**2*M**2) + 2*j*M)
    
def pBD(j,M):
    return (7.0/6.0 + ((j**2 * M ** 2) - (3 * j * M))/2.0 )
    

def pCU(j,M):
    return (7.0/6.0 + ((j**2 * M ** 2) + (3 * j * M))/2.0 )
    
def pCM(j,M):
    return ((-1.0/3.0) - (j**2*M**2) - 2*j*M)
    
def pCD(j,M):
    return (1.0/6.0 + ((j**2 * M ** 2) + (j * M))/2.0 )


def firstStageFinal(firstStage):
    collector = []
    collector2 = ()
    for x in range(len(firstStage)):
        for y in range(len(firstStage[x])):
            if firstStage[x][y] == jMax:
                collector2 = (pCU(firstStage[x][y],M),pCM(firstStage[x][y],M),pCD(firstStage[x][y],M))
            elif firstStage[x][y] == jMin:
                collector2 = (pBU(firstStage[x][y],M),pBM(firstStage[x][y],M),pBD(firstStage[x][y],M))
            else:
                collector2 = (pAU(firstStage[x][y],M),pAM(firstStage[x][y],M),pAD(firstStage[x][y],M))
            collector.append(collector2)
        collector2 = ()
    return collector
        
        
            
print firstStageFinal(g)
"""
I am still deciding which data structure to use here - I used a list and a tuple but i may change it to a list of list or 
a dictionary later.
The output from the above call look like so:
    
[(0.16666666666666666, 0.6666666666666666, 0.16666666666666666),
 (0.12166666666666666, 0.6566666666666666, 0.22166666666666668),
 (0.16666666666666666, 0.6666666666666666, 0.16666666666666666),
 (0.22166666666666668, 0.6566666666666666, 0.12166666666666666),
 (0.8866666666666667, 0.026666666666666727, 0.08666666666666666),
 (0.12166666666666666, 0.6566666666666666, 0.22166666666666668),
 (0.16666666666666666, 0.6666666666666666, 0.16666666666666666),
 (0.22166666666666668, 0.6566666666666666, 0.12166666666666666),
 (0.08666666666666666, 0.026666666666666727, 0.8866666666666667)]

""" 

"""
The table below is the output from all the codes above - Manually populated but will be implemented in Pandas later.
This is just the first stage of the tree building exercise.  We will implement the second stage later....in a couple
of weeks or sooner if time permits.  This is the way the outputs were presented in the sources.  Everything will be refined
later.  Frankly speaking, many third-party software have these implementations already but this is just for pedagogical 
exercise and to show what is going on under the hood if you are interested. And to write about these topics ultimately and put
my own style/flavor on it.  That said after this project I want to use the methodologies discussed here to model 
Multi-Curve Modeling Using Trees (to be based on a recent article by John Hull and Alan White) and also another one on CVA by 
another author or other authors.  I think sometimes when you are trying to model the more recent topics it gets in the way if 
you don't understand how to model the trees. But these are the core foundations so stay with me....Cheers!!!



Node            A           B           C           D           E           F           G           H           I
j               0           1           0           -1          2           1           0           -1          -2
j*deltaR        0.0000      0.01732     0.0000      -0.01732    0.03464     0.01732     0.00000     -0.01732    -0.03464
Pu              0.1666      0.1216      0.1666      0.2216      0.8866      0.1216      0.16667     0.22167     0.086667
Pm              0.66666     0.6566      0.6666      0.6566      0.02666     0.6566      0.65667     0.65666     0.026667
Pd              0.16666     0.22167     0.16667     0.12166     0.086667    0.22166     0.16667     0.121667    0.886667

"""

"""
SECOND STAGE COMPLETED ... NEEDS FINISHING TOUCHES & POLISHING:

BELOW IS THE FINAL INTEREST RATE TREE AND MATCHES THE FINAL RATE FROM THE TWO SOURCES:

CODES FOR THE SECOND STAGE NOT RELEASED AND WILL BE PUBLISHED IN AN ARTICLE IN THE NEAR FUTURE

STAY TUNED FOR BLACK KARASINSKI....same first stage as this one, only the second stage is different and we have to solve the rate

numerically no analytical solution.  See you next time!!!!!

OUTSTANDING:
(a) Regular Binomial Tree (Pending but prototyped via HL,BDT and KFW)
(b) Ho Lee (Done)
(c) BDT (Prototyped)
(d) KFW (Prototyped)
(e) HW (Done)
(f) BK (50% Done)
"""

Final Rate:
    
                 0                   1                   2
------------------|-------------------|-------------------|
                                        0.0971597185583342    
                                        0.0798392104826454    
                    0.0693705080756888  0.0625187024069567    
                    0.0520500000000000  0.0451981943312679    
0.0382400000000000  0.0347294919243112  0.0278776862555791


"""
"""
        
    



    
