import time
import sys
import io
import datetime

import M3
import M3B
import M3L
import M3C

now = datetime.datetime.now()
day = now.day
hour = now.hour
if str(day).__len__() == 1:
  date1 = (now.strftime('20%y-%m-0')+str(day)+'@'+str(hour)+'hr')
else:
  date1 = (now.strftime('20%y-%m-')+str(day)+'@'+str(hour)+'hr')
date2 = date1

filename = 'G:\\Hut_Relaunch_Analytics\\HutRelaunch'+ date1 +'.txt'

myNewFile = open (filename , 'w+')
myNewFile.write('\tAll Visits\t\t\t\tVisits hitting Basket Page\t\t\t\tVisits hitting Login Page\t\t\t\tVisits hitting Checkout Page\n')
myNewFile.write('Hour\tVisits\tTransactions\tConversion\tConversion Uplift\tVisits\tTransactions\tConversion\tConversion Uplift\tVisits\tTransactions\tConversion\tConversion Uplift\tVisits\tTransactions\tConversion\tConversion Uplift\n')

##Note that the except clauses will hide errors!!!!!
for x in range (24):
    myNewFile.write(str(x))
    try: ##All Visits- Visits
        myNewFile.write('\t'+M3.M1.globalOutputList[0][1][x][1])
    except:
        myNewFile.write('\t0')
    try: ##All Visits- Transactions
        myNewFile.write('\t'+M3.M1.globalOutputList[0][1][x][2])
    except:
        myNewFile.write('\t0')
    try: ##All Visits- Conversion
        myNewFile.write('\t'+str(M3.conversionByHour[x][1]))
    except:
        myNewFile.write('\t0')
    try: ##All Visits- Conversion Uplift
        myNewFile.write('\t'+str(M3.convRateUplift[x]))
    except:
        myNewFile.write('\t0')
    try: ##Visits hitting Basket Page- Visits
        myNewFile.write('\t'+M3B.M1B.globalOutputList[0][1][x][1])
    except:
        myNewFile.write('\t0')
    try: ##Visits hitting Basket Page- Transactions
        myNewFile.write('\t'+M3B.M1B.globalOutputList[0][1][x][2])
    except:
        myNewFile.write('\t0')
    try: ##Visits hitting Basket Page- Conversion
        myNewFile.write('\t'+str(M3B.conversionByHour[x][1]))
    except:
        myNewFile.write('\t0')
    try: ##Visits hitting Basket Page- Conversion Uplift
        myNewFile.write('\t'+str(M3B.convRateUplift[x]))
    except:
        myNewFile.write('\t0')
    try: ##Visits hitting Login Page- Visits
        myNewFile.write('\t'+M3L.M1L.globalOutputList[0][1][x][1])
    except:
        myNewFile.write('\t0')
    try: ##Visits hitting Login Page- Transactions
        myNewFile.write('\t'+M3L.M1L.globalOutputList[0][1][x][2])
    except:
        myNewFile.write('\t0')
    try: ##Visits hitting Login Page- Conversion
        myNewFile.write('\t'+str(M3L.conversionByHour[x][1]))
    except:
        myNewFile.write('\t0')
    try: ##Visits hitting Login Page- Conversion Uplift
        myNewFile.write('\t'+str(M3L.convRateUplift[x]))
    except:
        myNewFile.write('\t0')
    try: ##Visits hitting Checkout Page- Visits
        myNewFile.write('\t'+M3C.M1C.globalOutputList[0][1][x][1])
    except:
        myNewFile.write('\t0')
    try: ##Visits hitting Checkout Page- Transactions
        myNewFile.write('\t'+M3C.M1C.globalOutputList[0][1][x][2])
    except:
        myNewFile.write('\t0')
    try: ##Visits hitting Checkout Page- Conversion
        myNewFile.write('\t'+str(M3C.conversionByHour[x][1]))
    except:
        myNewFile.write('\t0')
    try: ##Visits hitting Checkout Page- Conversion Uplift
        myNewFile.write('\t'+str(M3C.convRateUplift[x])+'\n')
    except:
        myNewFile.write('\t0\n')


myNewFile.close()
