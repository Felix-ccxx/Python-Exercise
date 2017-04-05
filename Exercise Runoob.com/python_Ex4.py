from datetime import date

year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

datedelt=date(year,month,day)-date(year,1,1)
