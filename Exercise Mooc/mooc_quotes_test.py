from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
import pandas as pd
today = date.today()
start = (today.year-2, today.month, today.day)
quotes = quotes_historical_yahoo_ochl('MSFT', start, today)

attributes = ['date','open','close','high','low','volume']
quotesdf = pd.DataFrame(quotes, columns = attributes)

list1 = []
for i in range(0, len(quotes)-1):
    x = date.fromordinal(int(quotes[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    list1.append(y)
quotesdf.index = list1
quotesdf = pd.DataFrame(quotes, index=list1,columns = attributes)
quotesdf = quotesdf.drop(['date'], axis = 1 )


quotesdf.ix['15/01/30':'15/02/10',['open', 'close']]
quotesdf['15/01/02':'16/01/02'].sort('close', ascending=False)[:5]


list2 = []
tmpdf = quotesdf['15/01/02':'15/12/31'].copy
for i in range(0, len(tmpdf)):
    list2.append(int(tmpdf.index[i][3:5]))
tmpdf['month'] = list2
print tmpdf[ tmpdf.close > tmpdf.open]['month'].value_counts()


tmpdf.groupby('month')['volume'].sum()

sorted=quotesdf.sort('close')
pd.concat([sorted[:5],sorted[len(sorted)-5:]])


