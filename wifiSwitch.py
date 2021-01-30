import os 

def turnWifiOn():
    os.system("nmcli networking on")

def turnWifiOff(): 
    os.system("nmcli networking off")




