from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd

today=date.today()
start=(today.year,today.month-1,today.day)
quotes=quotes_historical_yahoo_ochl('KO',start,today)
fields=['date','open','close','high','low','volume']
list1=[]
for i in range(0,len(quotes)):
    x=date.fromordinal(int(quotes[i][0]))
    y=datetime.strftime(x,'%y-%m-%d')
    list1.append(y)
quotesdf=pd.DataFrame(quotes,index=list1,columns=fields)
quotesdf=quotesdf.drop(['date'],axis=1)
print quotesdf
