def vanakkam():
    print '''
##################################################
# Tool    : pscan                                #
# Version : 1.6                                  #
# Coded with Python 2.7                          #
# Profile : https://github.com/pr2h/             #
##################################################
    '''
vanakkam()

import socket
import sys
import time

def port_scanner_display(ip,port,number_of_ports):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result=sock.connect_ex((ip,port))

    if result==0:
        try:
            service=socket.getservbyport(port)
        except:
            service=''
            
        print (str(port)+'/TCP'+'\t'+'open'+'\t'+service).expandtabs(10)
        
        
    else:
        #Display closed port if number of ports <= 10
        if number_of_ports<=10:
            try:
                service=socket.getservbyport(port)
            except:
                service=''
            
            print (str(port)+'/TCP'+'\t'+'closed'+'\t'+service).expandtabs(10)

    sock.close()

def port_scanner():
    print '\n\n'
    try:
        ip=''
        ips=[]
        ports=''
        while ip=='':
            ip=raw_input('Host to scan  : ')

        #Check if given input is ip or hostname; and if given IP is valid
    
        if ' ' in ip:
            ips=ip.split(' ')
        else:
            ips.append(ip)

        ##################### PORTS ######################################

        while ports=='':
            ports=raw_input('Ports to scan : ')

        if ',' in ports:
            flag=0
            if '-' in ports:
                flag=10
            ports=ports.split(',')

            temp_list=[]
                
            if flag==10:
                for item in ports:
                    if '-' in item:
                        ports.remove(item)
                        item=item.split('-')

                        if item[1]>=item[0]:
                            start_port=item[0]
                            end_port=item[1]
                        else:
                            start_port=item[1]
                            end_port=item[0]
                            
                        port=int(start_port)
                        while port<=int(end_port):
                            temp_list.append(port)
                            port+=1
                ports+=temp_list

        elif '-' in ports:
            ports=ports.split('-')

            if ports[1]>=ports[0]:
                start_port=ports[0]
                end_port=ports[1]
            else:
                start_port=ports[1]
                end_port=ports[0]

            ports=[]
            port=int(start_port)
            while port<=int(end_port):
                ports.append(port)
                port+=1

        else:
            ports=ports.split(',')

        number_of_ports=len(ports)

        ##################################################################
        
        for ip in ips:
            try:
                socket.inet_aton(ip)
                if ip.count('.')==3:
                    #It is an IP - confirmed
                    pass
                else:
                    print '####Given IP is not valid. Please re-enter####'
                    port_scanner()
            except:
                ip=socket.gethostbyname(ip)

            try:
                hostname=''
                hostname=socket.gethostbyaddr(ip)
            except:
                pass
            
            print '\n\n-------------------------------------------------------------------------'
            print 'Scan started at ',time.strftime('%X on %x')
            print '\nPORTSCAN RESULT FOR ',ip,
            if hostname!='':
                print ' (',hostname[0],')\n'
            else:
                print '\n'
            print ('PORT'+'\t'+'STATE'+'\t'+'SERVICE').expandtabs(10)
                    
            ports = [ int(x) for x in ports ]
            ports.sort()

            start_time=time.time()
            for port in ports:
                port_scanner_display(ip,port,number_of_ports)

            print '\nScan completed at ',time.strftime('%X on %x')
            print 'Runtime: ',round(time.time()-start_time,4),' seconds'
            print '-------------------------------------------------------------------------'

    except KeyboardInterrupt:
        print '\n\nExiting..'
        sys.exit()

    except:
        print '''
        ---------------------------- WRONG INPUT ----------------------------
        Input Format (e.g.):

        IP to scan    : randommsitee11.com 192.168.1.2
        Ports to scan : 445,80-81,3389,8080-8081
        ---------------------------------------------------------------------
        '''
        port_scanner()

port_scanner()
