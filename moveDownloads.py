import os 

def deletecsv():
    #os.system('cd /home/ethanlee000/Downloads')
    os.chdir("/home/ethanlee000/Downloads")
    os.system('rm *.csv')
