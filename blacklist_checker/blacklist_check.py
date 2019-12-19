def vanakkam():
    print('''
##################################################
# Tool    : blacklist_check                      #
# Version : 1.0                                  #
# Coded with Python 3.7.4                        #
# Profile : https://github.com/pr2h/             #
# ######          #####   #                      #
# #    #  # ###  #     #  #                      #
# ######  ##         #    ######                 #
# #       #        #      #    #                 #
# #       #      #######  #    #                 #
##################################################
    ''')
    print('''
\nSummary : Blacklist IP/ hostname checker -
Input:
1) Full filename with extension (and path if the file exists in different path than program)
2) Please ensure each asset (IP/ hostname) is in each line, eg.
abcd.xyz
10.10.10.10
4.4.5.3
sampleurl.xyz
3) The given assets can be in the form of IPs or hostnames. In case of hostnames, they are automatically converted to IPs for comparison
4) The tool will automatically detect any invalid assets given
5) Output: List of SAFE and BLACKLISTED assets from your given list (printed on screen and logged in 'blacklist_output.log' in the same path as program

Disclamair: The tool just performs a comparison of Blacklisted IP list and your list of assets
The list of Blacklisted IPs is collected from source(s) available on interenet

Source(s):
1) https://myip.ms/files/blacklist/general/full_blacklist_database.zip
\n''')

import zipfile, os, requests, sys, socket, time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def print_and_log(line):
    print(line)
    log_filename = 'blacklist_output.log'
    f = open(log_filename, 'a')
    f.write('\n' + line)
    f.close()

def download_file(URL, filename):
    display = '[+] Downloading zip file (blacklisted IPs from internet)'
    print_and_log(display)

    display = '[*] Source = ' + URL
    print_and_log(display)

    try:
        req = requests.get(URL, verify=False)
    except:
        display = '[!] ERROR! No internet conenction/ Website unreachable'
        print_and_log(display)
        sys.exit()
        
    file = open(filename, 'wb')
    for chunk in req.iter_content(100000):
        file.write(chunk)
    file.close()
    
    display = '[*] Finished download'
    print_and_log(display)

def extract(filename):
    display = '[*] Performing zip file extraction'
    print_and_log(display)
    
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall()

    display = '[*] Completed extraction'
    print_and_log(display)

    display = '[*] Deleting zip file'
    print_and_log(display)
    
    os.remove(filename)

    display = '[*] Zip file deleted successfully'
    print_and_log(display)

def read_file(filename):
    display = '[*] Reading list of blacklisted IPs from text file'
    print_and_log(display)

    try:
        f = open(filename, 'r')
        content = f.readlines()
        f.close()
    except:
        return 0 # File does not exist

    ip_list = []

    for line in content:
        line = line.lstrip().rstrip()
        
        if line.startswith('#') or line == '':
            continue
            
        ip = line.split('#')[0]
        ip = ip.lstrip().rstrip().replace(' ','').replace('\n','')

        if ':' in ip:
            # ipv6 IP confirmed. We don't require that
            continue

        ip_list.append(ip)

    display = "[*] Read Completely and it's in my memory!"
    print_and_log(display)
    
    try:
        os.remove('full_blacklist_database.txt')
        display = '[*] Blacklist text file deleted successfully'
        print_and_log(display)
    except:
        pass
    return ip_list

def get_user_list():
    while True:
        user_input_file = input('[*] Enter filename with your IPs/ domains : ')
        user_list = read_file(user_input_file)
        print_and_log('[*] Input given, filename : ' + user_input_file)

        if user_list == 0:
            display = '[!] File not found. Please retry!'
            print_and_log(display)

            display = '[!] Ensure filename has correct extension and location'
            print_and_log(display)
            continue
        else:
            return(user_input_file, user_list)

def user_given_asset_verification(asset):
    # Determine if ip or hostname
    try:
        socket.inet_aton(asset)
        if ip.count('.')==3:
            # IPv4 IP confirmed
            ip = asset
            return ip
        else:
            # Not a valid IP
            return 0
                
    except:
        try:
            ip = socket.gethostbyname(asset)
            return ip
        except:
            # Not a valid hostname
            return 0

def cross_examination(user_list, blacklisted_ip_list):
    display = '[*] Beginning cross examination of User IP List vs Blacklisted IP List\n\n'
    print_and_log(display)
    
    for asset in user_list:
        verified_ip = user_given_asset_verification(asset)

        if verified_ip == 0:
            display = asset + ' : Not a valid hostname/ IP'
            print_and_log(display)

        else:
            if verified_ip in blacklisted_ip_list:
                display = '\n' + asset + ' : BLACKLISTED\n'
                print_and_log(display)
                
            else:
                display = asset + ' : SAFE'
                print_and_log(display)

    display = '\n\n[*] All Done!\n\n'
    
    print_and_log(display)
    
if __name__ == "__main__":
    vanakkam()
    URL = 'https://myip.ms/files/blacklist/general/full_blacklist_database.zip'
    filename = 'iplist.zip'
    blacklisted_filename = 'full_blacklist_database.txt'

    display = "\n\n\n############################### " + time.asctime(time.localtime(time.time())) + " ###############################\n"
    print_and_log(display)
    
    download_file(URL, filename)
    extract(filename)
    blacklisted_ip_list = read_file(blacklisted_filename)
    user_input_file, user_list = get_user_list()
    cross_examination(user_list, blacklisted_ip_list)

    display = "########################################################################################"
    print_and_log(display)
