def hujambo():
    print '''
##################################################
# Tool    : automated_url_opener                 #
# Version : 1.0                                  #
# Runs on : Windows                              #
# Source  : https://github.com/pr2h/             #
# Coded with Python 2.7                          #
##################################################
    '''

import subprocess, os, sys

def file_reader(filename):
    urls = []
    
    try:
        f = open(filename,'r')
        urls = f.readlines()
        f.close()
    except:
        pass
    
    return urls

def url_opener():
    while True:
        filename = raw_input('[+] Enter filename containing URLs : ')
        urls = file_reader(filename)

        if len(urls) == 0:
            print('[!] File not found. Please retry!')
            print('[!] Ensure filename has correct extension and location')
            continue
        else:
            break

    browser_choice = 0
    while browser_choice == 0:
        browser_choice = raw_input('Which browser you want to open in?:\n1. Firefox\n2. Chrome\nEnter choice (1 or 2) : ')
        try:
            browser_choice = int(browser_choice)         
            if browser_choice == 1 or browser_choice == 2 or browser_choice == 3:
                break
            print('[!] Wrong option entered. Please re-enter 1, 2 or 3')
            browser_choice = 0
        except:
            print('[!] Wrong option entered. Please re-enter 1, 2 or 3')
            browser_choice = 0

    if browser_choice == 1:
        if os.path.isfile('C:/Program Files/Mozilla Firefox/firefox.exe'):
            browser_path = 'C:/Program Files/Mozilla Firefox/firefox.exe'

        elif os.path.isfile('C:/Program Files (x86)/Mozilla Firefox/firefox.exe'):
            browser_path = 'C:/Program Files (x86)/Mozilla Firefox/firefox.exe'

        else:
            print('[!] Firefox not found. Trying with different Chrome')
            browser_choice = 2

    if browser_choice == 2:
        if os.path.isfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'):
            browser_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'

        elif os.path.isfile('C:/Program Files/Google/Chrome/Application/chrome.exe'):
            browser_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

        else:
            print('[!] Chrome not found. Exiting..')
            sys.exit()
            
    print('[*] Browser location : ' + browser_path)

    print('[#] NOTE : Keep at least one tab of firefox open for program to work')

    for url in urls:
        url = url.lstrip().rstrip().replace(' ','')
        print('[*] Opening URL : ' + url)
        subprocess.call([browser_path,'-new-tab',url])

if __name__=='__main__':
    hujambo()
    url_opener()
