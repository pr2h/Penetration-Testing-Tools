def hujambo():
    print('''
##################################################
# Tool    : url_opener                           #
# Version : 1.2                                  #
# Runs on : Windows                              #
# Source  : https://github.com/pr2h/             #
# Coded with Python 3                            #
# Release Date : 10th February 2020              #
##################################################
    ''')

import subprocess, os, sys, requests
requests.packages.urllib3.disable_warnings()

def response_code_checker(URL, number_of_times = 0):
    try:
        response = requests.get(URL, verify = False)
        return(response.status_code)

    except KeyboardInterrupt:
        print('\n[!] YOU PRESSED ABORT. QUITTING EXECUTION')
        sys.exit()

    except:
        if number_of_times < 2:
            print('[!] Unable to reach URL. Retrying..')
            number_of_times+=1
            response_code_checker(URL, number_of_times)
        else:
            print('[!] Unable to reach URL')
            return 0
    
# Usage Details / Help
def usage():
    print('SAMPLE USAGE: python url_opener.py --browser <firefox/ chrome> --tabs <number_of_tabs> --file <filename> --whitelistcodes <response_codes>')
    print('EXAMPLE (1) : python url_opener.py --browser chrome --tabs 10 --file sample.txt')
    print('EXAMPLE (2) : python url_opener.py -b chrome -f sample.txt -fc')
    print('EXAMPLE (3) : python url_opener.py -b chrome --file sample.txt -wc 200,400,404 -t 5\n')

    print('OPTIONS:')
    print('--help OR -h            : HELP')
    print('--browser or -b         : BROWSER SELECTION (chrome OR firefox)')
    print('--tabs OR -t            : NUMBER OF TABS TO SIMULTANEOUSLY OPEN')
    print('--file or -f            : FILE FOR URL INPUT')
    print('--whitelistcodes or -wc : ONLY OPEN URLs WITH SPECIFIED RESPONSE CODES')
    print('--forcecode or -fc      : FORCE DISPLAY RESPONSE CODES (WHEN -wc IS NOT USED) (slower)')
    sys.exit()

# Proccessing User Input (file/ browser/ tabs)
def user_input():
    tabs = 0
    whitelistcodes = ''
    forcecode = 0
    try:
        sys.argv[1]
    except:
        print('[!] --file AND --browser ARE MANDATORY OPTIONS. PLEASE REFER HELP\n')
        usage()

    arguments = sys.argv
        
    for argument in arguments:
        if argument == '--browser' or argument == '-b':
            try:
                browser_type = sys.argv[arguments.index(argument) + 1].lower()
                if browser_type == 'firefox':
                    browser_choice = 1
                elif browser_type == 'chrome':
                    browser_choice = 2
                else:
                    error

            except:
                print("\n[!] Wrong Arguments Provided for browser\n")
                usage()

        elif argument == '--tabs' or argument == '-t':
            try:
                tabs = int(sys.argv[arguments.index(argument) + 1])
                
            except:
                print("\n[!] Wrong Arguments Provided for tabs\n")
                usage()

        elif argument == '--file' or argument == '-f':
            filename = sys.argv[arguments.index(argument) + 1]

        elif argument == '--forcecode' or argument == '-fc':
            forcecode = 1

        elif argument == '--whitelistcodes' or argument == '-wc':
            try:
                whitelistcodes = sys.argv[arguments.index(argument) + 1]

                for item in whitelistcodes.split(','):
                    int(item)
                
            except:
                print("\n[!] Wrong Arguments Provided for whitelistcodes\n")
                usage()

        elif argument == '--help' or argument == '-h':
            usage()

    try:
        return browser_choice, tabs, filename, whitelistcodes, forcecode
    except:
        print('[!] --file AND --browser ARE MANDATORY OPTIONS. PLEASE REFER HELP\n')
        usage()

# Read the file specified
def file_reader(filename):
    urls = []
    
    try:
        f = open(filename,'r')
        urls = f.readlines()
        f.close()
    except:
        pass
    
    return urls

# Open the URLs
def url_opener():
    browser_choice, tabs, filename, whitelistcodes, forcecode = user_input()
    browser_choice = int(browser_choice)
    tabs = int(tabs)
    # forcecode is already in int

    urls = file_reader(filename)

    if len(urls) == 0:
        print('[!] File not found/ is empty. Please retry!')
        print('[!] Ensure filename has correct extension and location')
        sys.exit()

    while browser_choice == 0:
        if int(browser_choice) == 3:
            sys.exit()
            
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

    if tabs == 0:
        tabs = len(urls) + 10 # To keep opening tabs till the end of list

    number_of_urls_open = 0
    whitelistcodes_list = str(whitelistcodes).split(',')
        
    for url in urls:
        good_to_go = 0
        if whitelistcodes != '':
            response_code = response_code_checker(url)
            if str(response_code) in whitelistcodes_list:
                good_to_go = 1

        if whitelistcodes == '':
            number_of_urls_open+=1
            url = url.lstrip().rstrip().replace(' ','')
            if forcecode == 0:
                print('[*] Opening URL : ' + url)
            if forcecode == 1:
                response_code = response_code_checker(url)
                print('[*] Opening URL : ' + url + ', Response Code : ' + str(response_code))
            try:
                subprocess.call([browser_path,'-new-tab',url])
            except KeyboardInterrupt:
                print('\n[!] YOU PRESSED ABORT. QUITTING EXECUTION')
                sys.exit()

        elif whitelistcodes != '' and good_to_go == 1:
            number_of_urls_open+=1
            url = url.lstrip().rstrip().replace(' ','')
            print('[*] Opening URL : ' + url + ', Response Code : ' + str(response_code))
            try:
                subprocess.call([browser_path,'-new-tab',url])
            except KeyboardInterrupt:
                print('\n[!] YOU PRESSED ABORT. QUITTING EXECUTION')
                sys.exit()

        else:
            if response_code == 0 or response_code == None:
                print('[*] Skipping URL : ' + url.replace('\n','') + ', [!] UNABLE TO REACH THIS URL')
            else:
                print('[*] Skipping URL : ' + url.replace('\n','') + ', Response Code : ' + str(response_code))

        if number_of_urls_open % tabs == 0 and number_of_urls_open != 0:
            try:
                input('Press Enter to Continue')
            except KeyboardInterrupt:
                print('\n\n[!] YOU PRESSED ABORT. QUITTING EXECUTION')
                sys.exit()

if __name__=='__main__':
    hujambo()
    url_opener()
