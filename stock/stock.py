# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:07:58 2016

@author: Yingqing Zhou
"""
# Filename: quotes.py
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd

class stock(object):
    def __init__(self):
        self.list = ['intel','eric','ms','yahoo']
        self.num = 50

    def test(self):
        print self.list, self.num
        
#        
#today = date.today()
#start = (today.year-2, today.month, today.day)
#quotesMS = quotes_historical_yahoo('ERIC', start, today)
#attributes=['date','open','close','high','low','volume']
#quotesdfMS = pd.DataFrame(quotesMS, columns= attributes)
#
#list = []
#for i in range(0, len(quotesMS)):
#    x = date.fromordinal(int(quotesMS[i][0]))
#    y = date.strftime(x, '%y/%m/%d')
#    list.append(y)
#quotesdfMS.index = list
#quotesdfMS = quotesdfMS.drop(['date'], axis = 1)
#list = []
#
#quotesdfMS15 = quotesdfMS['15/01/01':'15/12/31']
#for i in range(0, len(quotesdfMS15)):
#    list.append(int(quotesdfMS15.index[i][3:5])) #get month just like '02'
#quotesdfMS15['month'] = list
#print quotesdfMS15.groupby('month').mean().close
#
#list = []
#for i in range(0, len(quotesdfMS15)):
#    season = (int(quotesdfMS15.index[i][3:5]) - 1)/3 + 1
#    list.append(season)
#quotesdfMS15['season'] = list
#print quotesdfMS15.groupby('season').mean().close
#
#print quotesdfMS['15/01/01':'15/12/31'].sort('close', ascending=True)[-5:]
#print quotesdfMS['15/01/01':'15/12/31'].sort('close', ascending=False)[:5]
##print quotesdfMS15[quotesdfMS15['close']>12]
##print quotesdfMS15[quotesdfMS15.close>12]
#
#sorted = quotesdfMS.sort('close')
#print pd.concat([sorted[:5], sorted[-5:]])