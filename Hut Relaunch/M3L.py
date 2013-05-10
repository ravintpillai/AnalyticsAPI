import M1L
import M2L

stats = M1L.globalOutputList
preStats = M2L.globalOutputList

conversionByHour = []
for x in range (len(stats[0][1])):
	try: conversionByHour.append(((int(stats[0][1][x][0]),float (stats[0][1][x][2])/float (stats[0][1][x][1]))))
	except: conversionByHour.append((int(stats[0][1][x][0]),0))
conversionByHourPast = []
for x in range (len(preStats[0][1])):
	try: conversionByHourPast.append(((int(preStats[0][1][x][0]),float (preStats[0][1][x][2])/float (preStats[0][1][x][1]))))
	except: conversionByHourPast.append((int(preStats[0][1][x][0]),0))
convRateUplift = []
for x in range (len(conversionByHour)):
        convRateUplift.append((conversionByHour[x][1])/(conversionByHourPast[x][1])-1)
##print conversionByHour,conversionByHourPast,convRateUplift
