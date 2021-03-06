"""
TITLE:  BOOTSTRAPPING ZERO RATE CURVES.

DEFINITION: The Zero Rate r(0,t) between time 0 and time t is the
rate of return of a cash deposit made at time 0 and maturing at time t.
The zero-coupon yield or spot-rate curve is the term structure of discount 
rate of zero-coupon bonds.  A zero curve consists of the yield to maturity
for a portfolio of theoretical zero-coupon bonds that are derived from the 
input bonds portfolio.

STATEMENT OF PROBLEM: The coupon rate or treasury rates are only available for
certain maturities so we need to bootstrap for dates for which there are no available rates.

Consider the example below - from A Primer for the Mathematics of Financial Engineering -
The Prices and coupon rates for four semiannual coupon bonds with face value of 100 are as follows:

Maturity    Coupon Rate     Price
6 Months    0               99
1 Year      4               102
2 Years     4               103.5
5 Years     4               109

As you can see from above, we only have information for 6 months, 1 year, 2 years and 5 years.  However, the bond
portfolio consists of semi-annual coupon paying bonds so we need information for 1.5 year's time, 2.5 year's time, 
3 year's time, 4 year's time, 4.5 year's time in order to determine the price of a 3 year semi-annual coupon bond for 
example or price the 5 year bond.   So to achieve this objective, we have to bootstrap the zero rate 
using a mixture of interpolation and bootstrapping using Newton-Raphson.

The key assumption made in the book is that the cashflow are continously compounded and the formula for 
bootstrapping the zero rate is a little bit different coupon paying bond versus non-coupon paying bond.  
In order to follow this code, you have to get a copy of the book or borrow it from the library or your 
friend. (see page 153)

 ***This is a really rough prototype and will only work for the question in the book (the above question).  
 However, if you know python you can edit the code to work for other bond portfilios.  We will update it to 
 work for different length of maturity such as 10 years etc. i.e. make it more dynamic. Making it dynamic
 will require using python to calculate the first derivatives used in the Newton-Raphon module instead of 
 using Wolfram Alpha.  Again, this will be dealt with at a later time.
"""

#To bootstrap the zero rate for the 6 months zero-coupon paying bond we use the formula below:
import math

#To bootstrap the zero rate for the 6 months zero-coupon paying bond we use the formula below:
r06 =  (12.0/6)*math.log(100.0/99)

print "r06 is " + str(r06)

#To calculate the root of the original function - this function can be changed to a new one.


def func_calculator1(x):  #Price Function for Year 1
    return 102.0 - 2 *math.exp(-0.5*0.0201007) - 102*math.exp(-x)
    
#To calculate the root of the first derivative of the function.

def func_prime_calculator1(x):  #Derivative of Price Function for Year 1
    return 102.0*math.exp(-x)
    
    
def func_calculator2(x):  #Price Function for Year 2
    return 103.5 - 2.0*math.exp(-0.5*0.0201007) - 2.0*math.exp(-1*0.0196026) - 2.0*math.exp((-1.5*(0.0196026+x))/2.0) - 102*math.exp(-2.0*x)
    
#To calculate the root of the first derivative of the function.

def func_prime_calculator2(x):  #Derivative of Price Function for Year 2
    return 204.0*math.exp(-2.0*x) + 1.47811*math.exp(-0.75*x)
    
    
def func_calculator5(x):  #Price Function for Year 5
    return 109.0 - 2.0*math.exp(-0.5*0.0201007) - 2.0*math.exp(-1*0.0196026) - 2.0*math.exp(-1.5*0.02077345) - 2*math.exp(-2.0*0.0219443) - 2.0*math.exp((-2.5*(x+(5*0.0219443))/6.0)) - \
    2.0*math.exp((-3.0*(x+(2*0.0219443))/3.0)) - 2.0*math.exp((-3.5*(x+(0.0219443))/2.0)) - 2.0*math.exp((-4.0*(2*x+(0.0219443))/3.0)) - 2.0*math.exp((-4.5*(5*x+(0.0219443))/6.0)) - 102*math.exp(-5*x)

#To calculate the root of the first derivative of the function.

def func_prime_calculator5(x):  #Derivative of Price Function for Year 5
    return 5.17955*math.exp(-2.66667*x) + 3.36814*math.exp(-1.75*x) + 1.91412*math.exp(-x) + 0.796093*math.exp(-0.41667*x) +510*math.exp(-5*x) + 7.37757*math.exp(-3.75*x)
    


#This is the implementation of the Newton-Raphson method

def newton1(x): #Newton call for year 1
    epsilon = 10e-9
    maxIterationCount = 1000000
    x0 = x
    x1 = 0.0
    i = 0
    try:
        while (i < maxIterationCount):
            fValue = func_calculator1(x0)
            fDerivative = func_prime_calculator1(x0)

            x1 = x0 - fValue/fDerivative
        
            if abs(x1 - x0) <= epsilon:
                return x1
        
            x0 = x1
            ++i
    except (OverflowError,RuntimeError, TypeError, NameError):
        print""
        print "No Solution Was Found!!!."
        

def newton2(x): #Newton call for year 2
    epsilon = 10e-9
    maxIterationCount = 1000000
    x0 = x
    x1 = 0.0
    i = 0
    try:
        while (i < maxIterationCount):
            fValue = func_calculator2(x0)
            fDerivative = func_prime_calculator2(x0)

            x1 = x0 - fValue/fDerivative
        
            if abs(x1 - x0) <= epsilon:
                return x1
        
            x0 = x1
            ++i
    except (OverflowError,RuntimeError, TypeError, NameError):
        print""
        print "No Solution Was Found!!!."
        
def newton5(x): #Newton call for year 5
    epsilon = 10e-9
    maxIterationCount = 1000000
    x0 = x
    x1 = 0.0
    i = 0
    try:
        while (i < maxIterationCount):
            fValue = func_calculator5(x0)
            fDerivative = func_prime_calculator5(x0)

            x1 = x0 - fValue/fDerivative
        
            if abs(x1 - x0) <= epsilon:
                return x1
        
            x0 = x1
            ++i
    except (OverflowError,RuntimeError, TypeError, NameError):
        print""
        print "No Solution Was Found!!!."
        
r6 = 0.020100
r12 = newton1(0.05)
r18 = (0.0196026 +0.0219443)/2.0
r24= newton2(0.05)  # Value is 0.021944274982594374
r30= (0.020801859402415773 + 5*0.0219443)/6.0
r36= (0.020801859402415773 +2*0.0219443)/3.0
r42= (0.020801859402415773 + 0.0219443)/2.0
r48= (2*0.020801859402415773 + 0.0219443)/3.0
r54= (5*0.020801859402415773 + 0.0219443)/6.0
r60= newton5(0.05)  ### Value is 0.020801859402415773

data = {}
data.update({"r06": r06})
data.update({"r12": r12})
data.update({"r18": r18})
data.update({"r24": r24})
data.update({"r30": r30})
data.update({"r36": r36})
data.update({"r42": r42})
data.update({"r48": r48})
data.update({"r54": r54})
data.update({"r60": r60})

import pandas as pd
print ""
df = pd.Series(data)
df.plot()


#Sample Output - these answers converge to the ones in the book
"""
r06    0.020101         - Six Months
r12    0.019603         - Year 1
r18    0.020773         - Year 1.5
r24    0.021944         - Year 2
r30    0.021754         - Year 2.5
r36    0.021563         - Year 3
r42    0.021373         - Year 3.5
r48    0.021183         - Year 4
r54    0.020992         - Year 4.5
r60    0.020802         - Year 5

"""
"""
BENCHMARKING TO MATLAB FINANCIAL INSTRUMENT TOOLBOX:
***The answers are not the same but are close the major reason I can think of is that in the python module we did not
take into account day count conventions and assumed that six months is 0.5 years etc.  But Matlab takes into account
day count convention - actual/actual, 30/360 etc. 

Bonds = [datenum('06/30/2000')   0.00  100  2  0  0;
         datenum('12/31/2000')   0.04  100  2  0  0;
         datenum('12/31/2001')   0.04  100  2  0  0;
         datenum('12/31/2004')   0.04  100  2  0  0];

Prices = [99.00;
          102.00;
         103.50 ;
          109.00; ];

Settle = datenum('1/1/2000');

OutputCompounding = 2;

[ZeroRates, CurveDates] = zbtprice(Bonds, Prices, Settle,OutputCompounding)

DateNumber = 730667;
DateNumber1 = 730851;
DateNumber2 = 731216;
DateNumber3 = 732312;

formatOut = 'mmmm-dd-yyyy';
str = datestr(DateNumber,formatOut)
str2 = datestr(DateNumber1,formatOut)
str3 = datestr(DateNumber2,formatOut)
str4 = datestr(DateNumber3,formatOut)


730667  0.0204      June-30-2000       %Matlab
730851  0.0197      December-31-2000   %Matlab
        0.0209      June-30-2001        %  (December-31-2000 + December-31-2001)/2.0 - Manually Interpolated
731216  0.0221      December-31-2001    %Matlab
        0.0219      June-30-2002        %  (5*December-30-2001 + December-31-2004)/6.0 - Manually Interpolated
        0.0217      December-31-2002    %  (2*December-30-2001 + December-31-2004)/3.0 - Manually Interpolated
        0.0215      June-30-2003        %  (December-30-2001 + December-31-2004)/2.0 - Manually Interpolated
        0.0213      December-31-2003    %  (December-30-2001 + 2*December-31-2004)/3.0 - Manually Interpolated
        0.0211      June-30-2004        %  (December-30-2001 + 5*December-31-2004)/6.0 - Manually Interpolated
732312  0.0209      December-31-2004   %Matlab


"""

