import requests
import time
import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def hujambo():
    print '''
##################################################
# Tool    : dosattack_analyzer                   #
# Version : 1.1                                  #
# Coded with Python 2.7                          #
# Profile : https://github.com/pr2h/             #
# ######          #####   #                      #
# #    #  # ###  #     #  #                      #
# ######  ##         #    ######                 #
# #       #        #      #    #                 #
# #       #      #######  #    #                 #
##################################################
    '''

def dos_attack_analyzer(URL):
    filename = 'doslog__'+str(datetime.datetime.now()).replace('-','_').replace(' ','_').replace(':','_').split('.')[0]+'.txt'

    f1 = open(filename,'a')
    f1.write(URL)
    f1.write('\n\n')

    total = 0
    average = 0
    i = 0
    
    while True:
        i+=1
        start_time = time.time()
        response = requests.get(URL.lstrip().rstrip(), stream = True, verify=False).content
        float_time_taken = time.time()-start_time
        time_taken = "\nTime taken : "+str(float_time_taken)
        print time_taken
        total += float_time_taken
        average = total / i
        average_time = "Average Time taken : "+str(average)
        print average_time
        write_string = time_taken + ', '+average_time
        f1.write(write_string)
        f1.flush()
        
    f1.close()

if __name__=='__main__':
    hujambo()
    URL = raw_input('Enter URL : ')
    URL = URL.lstrip().rstrip()
    dos_attack_analyzer(URL)
