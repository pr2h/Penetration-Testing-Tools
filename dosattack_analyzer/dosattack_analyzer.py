# Application Banner
def hujambo():
    print '''
##################################################
# Tool    : dosattack_analyzer                   #
# Version : 1.2                                  #
# Coded with Python 2.7                          #
# Source  : https://github.com/pr2h/             #
##################################################
    '''

import requests
import time
import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# Ignoring warnings during requests.get
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def dos_attack_analyzer(URL):
    # Creating logfile name with current date and time (+30 mins)
    date_time = str(datetime.datetime.now() + datetime.timedelta(minutes=30))
    filename = 'doslog__' + date_time.replace('-','_').replace(' ','_').replace(':','_').split('.')[0]+'.txt'

    # Writing banner to file
    f1 = open(filename,'a')
    f1.write('#########################################################################')
    f1.write('\nFile                : dosattack_analyzer LogFile')
    f1.write('\nURL                 : ' + URL)
    f1.write('\nStart Date and Time : ' + date_time)
    f1.write('\n#########################################################################')
    f1.write('\n')

    # Initializing variables
    total = 0   # Total of all response times
    average = 0 # Average response time
    i = 0       # Number of requests made

    while True:
        i+=1
        start_time = time.time()
        # Current date and time (+30 mins)
        date_time = datetime.datetime.now() + datetime.timedelta(minutes=30)

        # Capturing response of URL
        try:
                response = requests.get(URL.lstrip().rstrip(), stream = True, verify=False).content
        except:
                # Displaying error if response is not captured due to application being down or excess response time
                downtime = "\n\nDowntime at "+str(date_time)
                print downtime
                f1.write(downtime)
                continue

        # Calculating time taken, total response time and average response time
        float_time_taken = time.time()-start_time
        total += float_time_taken
        average = total / i

        # Printing all calculated values and writing to logfile
        date_time_print = 'Date and time : '+str(date_time)
        time_taken = "Time taken : "+str(float_time_taken)
        average_time = "Average Time taken : "+str(average)
        write_string = date_time_print + ', ' + time_taken + ', '+ average_time

        print write_string.lstrip()        
        write_string = '\n' + write_string
        f1.write(write_string)
        f1.flush()

    f1.close()

if __name__=='__main__':
    # Displaying tool banner
    hujambo()
    URL = raw_input('Enter URL : ')
    URL = URL.lstrip().rstrip()
    dos_attack_analyzer(URL)
