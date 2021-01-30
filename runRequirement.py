from scrapeRunningData import scrapeRunningData 
from wifiSwitch import turnWifiOn 
from wifiSwitch import turnWifiOff
from moveDownloads import deletecsv

#Checks if run requirements have been met 
import csv
import pandas as pd
import datetime

runRequirement = 3 

scrapeRunningData()

df = pd.read_csv('/home/ethanlee000/Downloads/Activities.csv', usecols=['Date','Distance'])
df['Dates'] = pd.to_datetime(df['Date']).dt.date
print(df)

dateList = df.Date.tolist()
distanceList = df.Distance.tolist()


for index, item in enumerate(dateList):
    dateList[index] = dateList[index][0:10]

x = datetime.datetime.now()
date = x.strftime('%Y-%m-%d')

if date in dateList: 
    print('Date found')

    filename = '/home/ethanlee000/Documents/Python/runRequirement/prevRunDist.txt'
    file_object = open(filename ,'r')
    prevData = file_object.read()
    runData = distanceList[0]
    runDataString = str(runData)

    if (runDataString == prevData):
        print("ERROR: Improper Running Data")
    elif runData < runRequirement:
        print("you didn't run enough!")
        turnWifiOff()
        file_object = open(filename, 'w')
        file_object.write(str(runData))
        file_object.close()
    elif runData > runRequirement: 
        print("You ran enough, good job!")
        turnWifiOn()
        file_object = open(filename, 'w')
        file_object.write(str(runData))
        file_object.close()
    else: 
        print("ERROR: Nothing happened")

else: 
    print("You didn't run today!")
    turnWifiOff()

deletecsv()
