#!/usr/bin/python
# Version 0.1: analyze the result, and show in graphes
# Date:   20160610
#

import sys 
import re
import os
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def getTime(row):
   timeStr = row['result'].split(":")
   t = 0
   for item in timeStr:
      t = 60*t + int(item)
      #print item, t
   return t

def getSpeed(row):
   if row['group'] == '5KM':
      d = 5.0
   else:
      d = 10.0
   #print row['group'], row['time']
   # speed per hr
   s = d/row['time']*3600
   return s

def getMinMax(ages):
   min = 30
   max = 30
   for age in ages:
      if age < min and age > 12:
         min = age
         continue
      if age > max and age < 100:
         max = age
         continue
   return (min, max)   

def statAge(ageCol):
   ages = [0, 0, 0 , 0, 0, 0]
   for age in ageCol:
      if age < 12 or age > 100:
         # invalid age
         continue
      else:
         if age > 60:
            ages[4] += 1
         else:
            ages[int(age)/10 -1] += 1
   print ages
   return ages


def main(argv):
   df = pd.read_csv('result.txt')
   # analysis
   print df.describe()
   print df.head()

   df['age']   = df['born'].map(lambda x: 2016-int(x))
   df['time']  = df.apply(lambda row: getTime(row), axis=1)
   df['timemin']   = df['time'].map(lambda x: x/60)
   df['speed'] = df.apply(lambda row: getSpeed(row), axis=1)

   df.drop(df.columns[[0,2]],axis=1, inplace=True)

   print df.describe()
   print df.tail()

   total = len(df)
   fn    = len(df[df.gender=='Dame'])
   mn    = total - fn
   
   df1   = df[df.group=='5KM']
   df2   = df[df.group=='10KM']
   t1    = len(df1)
   fn1   = len(df1[df1.gender=='Dame'])
   mn1   = len(df1[df1.gender=='Hea'])
   

   print 'Total %d person joined this event, female %d, male %d' %(total, fn, mn)
   print 'Total %d person run 5KM,  female %d, male %d' %(t1, fn1, mn1)
   print 'Total %d person run 10KM, female %d, male %d\n' %(total-t1, fn-fn1, mn-mn1)

   print '\n'

   (young,old) = getMinMax(df['age'])
   print 'The youngest is %d, the oldest %d\n' %(young, old)

   fig = plt.figure()
   #N = 3
   #male   = [mn, mn1, mn-mn1]
   #female = [fn, fn1, fn-fn1]
   #ind = [1, 2, 3]
   #indLabel = ['total', '5KM', '10KM']
   #ax = plt.subplot(111)
   #ax.bar(ind-0.2, male, width=0.2, color='b', align='center')
   #ax.bar(ind,   female, width=0.2, color='r', align='center')
   #ax.xticks(ind, indLabel)
  
   # Man vs. Woman
   N = 6
   values = [mn, fn, mn1, fn1, mn-mn1, fn-fn1]
   ind = np.arange(N)
   indLabel = ['Male', 'Female', '5KM M', '5KM F', '10KM M', '10KM F']
   plt.subplot(211)
   plt.bar(ind,   values, width=0.2, color='r', align='center')
   plt.xticks(ind, indLabel)
   plt.title('The number of Male & Female')
   
   # Ages statistic
   ages = statAge(df['age'])
   ageLabel = ['12-19', '20-29', '30-39', '40-49', '50-59', '60+']
   plt.subplot(212)
   plt.bar(ind,   ages, width=0.2, color='b', align='center')
   plt.xticks(ind, ageLabel)
   plt.title('The number of different ages')

   # Time distribution
   dfm1   = df1[df1.gender=='Hea']
   dff1   = df1[df1.gender=='Dame']
   dfm2   = df2[df2.gender=='Hea']
   dff2   = df2[df2.gender=='Dame']
   #plt.subplot(313)
   bins = np.linspace(-10, 10, 100)
   #n,bins,patches = plt.hist([dfm1['time'].,dff1['time'],dfm2['time'],dff2['time']],alpha=0.5)

   df.groupby(['gender','group']).hist()
   #plt.hist(dfm1.time/60,alpha=0.5,label='Male 5KM')
   #plt.hist(dff1['time'],alpha=0.5,label='Female 5KM')
   #plt.hist(dfm2['time'],alpha=0.5,label='Male 10KM')
   #plt.hist(dff2['time'],alpha=0.5,label='Femal 10KM')
   plt.legend('upper right')
   plt.title('Time distribution')
   plt.show()

   


if __name__ == '__main__':
   main(sys.argv)
