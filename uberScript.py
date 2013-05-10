import AutoPostSLVersionWithSegments
import ipad
import io

isMobileData = AutoPostSLVersionWithSegments.globalOutputList
ipadData = ipad.globalOutputList
filename = 'C:\\Users\\thambapillair\\Documents\\'+ AutoPostSLVersionWithSegments.date1 +'smartphones.txt'
myNewFile = open (filename, 'w+')
myNewFile.write('Profile\tSmartphone Transactions\tSmartphone Visits\tSmartphone Revenue\n')

for x in range (15):
    print isMobileData[x][0]
    myNewFile.write((isMobileData[x][0])+'\t')
    print isMobileData[x][1][1]
    print ipadData[x][1]
    for y in range (1,4):
        print (int(float((isMobileData[x][1][1][y]))) - int(float(ipadData[x][1][0][y])))
        myNewFile.write((str(int(float(isMobileData[x][1][1][y])) - int(float(ipadData[x][1][0][y]))))+'\t')
    myNewFile.write('\n')

myNewFile.close()
