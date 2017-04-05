import time 
from matplotlib.finance import quotes_historical_yahoo_ochl 
from datetime import date 
from datetime import datetime 
import pandas as pd 
import matplotlib.pyplot as plt 
 
today = date.today() 
start = (today.year-1, today.month, today.day) 
quotes = quotes_historical_yahoo_ochl('MSFT', start, today) 
fields = ['date','open','close','high','low','volume'] 
 
list1 = [] 
for i in range(0,len(quotes)): 
        x = date.fromordinal(int(quotes[i][0])) 
        y = datetime.strftime(x,'%Y-%m-%d') 
        list1.append(y) 
#print list1 
quotesdfMS14 = pd.DataFrame(quotes, index = list1, columns = fields) 
quotesdfMS14 = quotesdfMS14.drop(['date'], axis = 1) 
#print quotesdf 
listtemp = [] 
for i in range(0,len(quotesdfMS14)): 
        temp = time.strptime(quotesdfMS14.index[i],"%Y-%m-%d") 
        listtemp.append(temp.tm_mon) 
         
print listtemp 
#tempkodf = quotesdfMS14.copy() 
#tempkodf['month'] = listtemp
quotesdfMS14['month'] = listtemp
openMS = quotesdfMS14.groupby('month').mean().open 
listopen = [] 
for i in range(1,13): 
        listopen.append(openMS[i]) 
#plt.plot(openMS.index, listopen)
#plt.plot(openMS.index, openMS.values)
#plt.plot(openMS.index, openMS.values,'-.*r')

plt.scatter(quotesdfMS14.close - quotesdfMS14.open, quotesdfMS14.volume)
plt.show()

'''
quotesINT = quotes_historical_yahoo_ochl('INTC', start, today) 
quotesdfINT = pd.DataFrame(quotesINT, columns= fields)
list = []
for i in range(0, len(quotesINT)):
    x = date.fromordinal(int(quotesINT[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    list.append(y)
quotesdfINT.index = list
quotesdfINT = quotesdfINT.drop(['date'], axis = 1)
list = []
quotesdfINT14 = quotesdfINT['15/01/01':'15/12/31']
#quotesdfINT14.open.plot()



compdf = pd.DataFrame()
compdf['MS'] = quotesdfMS14.open
compdf['INTC'] = quotesdfINT14.open
compdf.plot(title='open price of MS and INTEL')
plt.show()
'''
