# Application Banner
def hujambo():
    print '''
##################################################
# Tool    : file_locator (Win / Linux)           #
# Version : 1.0                                  #
# Coded with Python 2.7                          #
# Source  : https://github.com/pr2h/             #
##################################################
    '''

# Importing required modules
import subprocess
import sys
import time
import os

# Function to return command based on OS type : Windows / Linux
def command_fetch(loc):
    print '[*] Checking if system is Windows or Linux'
    # Windows OS
    if os.name == 'nt':
        print '[*] Detected Windows OS running on this machine'
        command = 'dir /s /b /o:gn ' + loc

    # Linux OS
    elif os.name == 'posix':
        print '[*] Detected Linux OS running on this machine'
        command = 'ls -LR ' + loc

    # Any other unsupported OS
    else:
        print '[!] OS not supported yet. Exiting..\n'
        sys.exit()

    # Returning appropriate command
    return command
    
# Function to cache the file/ directory list and find the command
def file_locator():
    try:
        # Getting the directory to cache
        loc = raw_input('[*] What do I cache? (e.g C:/Users or /root/this, (Default: Current Directory)) : ')
        if loc == '':
            # Fetching Current directory
            loc = os.getcwd()

    # In case user wants to exit the program            
    except:
        print '\n'
        sys.exit()

    # Editing the directory location string to account for unrequired characters and spaces inside the path
    loc = '"' + loc.replace('"','').lstrip().rstrip().rstrip('\\') + '"'

    # Fetching the command to be executed
    command = command_fetch(loc)
    print('[+] Caching the required filenames from ' + loc)

    # Checking if the directory exists
    if os.path.isdir(loc.lstrip('"').rstrip('"')) == True:
        print '[*] Verified that the given directory is valid'

    else:
        print '[!] Invalid directory. Have you supplied the correct path?\n'
        file_locator()
        
    print '[*] Executing command :',command

    # Executing command and calculating time taken
    start_time = time.time()
    all_files = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
    no_of_files = all_files.count('\n')+1
    print '[*] It took',time.time() - start_time,'seconds to obtain the complete list of ',str(no_of_files),'files. Pheww..'

    # Converting all_files into list
    all_files_list = all_files.split('\n')

    # Initializing string to find in filename
    findstr = ''
    print '\n'
    
    while True:
        # Obtaining the string to find in filename
        try:
            while findstr == '':
                findstr = raw_input('[*] What do you want to find ? : ')
        except KeyboardInterrupt:
            print '\n'
            sys.exit()
        except:
            print '\n'
            sys.exit()

        # Initializing flag to denote if there are any matching files
        flag = 0

        # Listing relevant files
        try:
            print '\n[*] Listing files :'
            for file1 in all_files_list:
                if findstr in file1:
                    print file1.rstrip(':')
                    # Signifying there is at least one file displayed
                    flag = 1
            
        except KeyboardInterrupt:
            print '[!] You interrupted the printing of results'

        except:
            print '[!] Unknown Error. Cannot print appropriate results'

        # Displaying message if no files were found
        if flag == 0:
            print '[*] No files found'
            print '\n'

        else:
            print '\n'

        # Redifinig findstr to it's original value to search again
        findstr = ''

if __name__=='__main__':
    # Displaying tool banner
    hujambo()

    # Calling the Function to cache the file/ directory list and find the command
    file_locator()
