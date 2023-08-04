# -*- coding: utf-8 -*-
"""
Made By: Bryson Smith 
"""
#import OS and Subprocess library 
import os 
import subprocess 
import time
#store file path based off of directory of python file. 
file_path = os.path.dirname(os.path.abspath(__file__))
#create command prompt to set directory as file path
#sets working directory as file path of .EXE
subprocess.call('cd '+ file_path , shell=True)
#run cacls command. 

output = subprocess.call('cacls \"SLEA Toolbar\" /e /t /g users:f', shell=True)
if output == 5:
    print("Access Denied, please run program as admin")
    time.sleep(2)
    exit()
else:
    print("Cacls Command Successful!")
    time.sleep(2)
#create firewall program path
Firewall_Program = file_path + '\\SLEA Toolbar\\' + 'SLEA Toolbar.exe'
#Create inbound firewall exceptions for SLEA Toolbar
subprocess.call('netsh advfirewall firewall add rule name=\"SLEA Toolbar\" dir=in action=allow program=\"{}\"'.format(Firewall_Program), shell=True)
#Create inbound firewall exceptions for SLEA UDP
subprocess.call('netsh advfirewall firewall add rule name="SLEA UDP" dir=in action=allow protocol=UDP localport=8080-10000', shell=True)
#Create outbound firewall exceptions for SLEA Toolbar
subprocess.call('netsh advfirewall firewall add rule name=\"SLEA Toolbar\" dir=out action=allow program=\"{}\"'.format(Firewall_Program), shell=True)
#Create outbound firewall exceptions for SLEA UDP
subprocess.call('netsh advfirewall firewall add rule name="SLEA UDP" dir=out action=allow protocol=UDP localport=8080-10000', shell=True)