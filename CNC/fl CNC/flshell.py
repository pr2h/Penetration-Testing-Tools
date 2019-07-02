# Application Banner
def hujambo():
    print('''
##################################################
# Tool    : flshell                              #
# Version : 1.0                                  #
# Coded with Python 2.7                          #
# Source  : https://github.com/pr2h/             #
##################################################
    ''')

import sys
import time

def command_handler():
    prev_read = ''
    while True:
        command=''
        while command=='':
            try:
                command=raw_input('>> ')
                command=command.lower()

            except KeyboardInterrupt:
                print "\nYou pressed Ctrl+C. Try 'exit' instead"

        f = open('command.txt','w')
        f.write(command)
        f.flush()
        f.close()

        if command == 'exit':
            sys.exit()

        time.sleep(6)
        f = open('output.txt','r')
        content = f.read()
        try:
            print content
        except:
            print 'OUTPUT ERROR. Check out output.txt manually'
        f.close()

hujambo()
print 'FLSHELL OPENED'
command_handler()
