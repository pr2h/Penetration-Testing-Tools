def hujambo():
    print '''
##################################################
# Tool    : open_all_urls                        #
# Version : 1.0                                  #
# Coded with Python 2.7                          #
# Profile : https://github.com/pr2h/             #
# ######          #####   #                      #
# #    #  # ###  #     #  #                      #
# ######  ##         #    ######                 #
# #       #        #      #    #                 #
# #       #      #######  #    #                 #
##################################################
    '''
hujambo()

import subprocess

with open('urls.txt','r') as f:
    urls=f.readlines()
f.close()


# Have a tab already opened on firefox before running this program
for url in urls:
    url=url.strip('\n')
    url=url.strip(' ')
    subprocess.call([r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe','-new-tab',url])
