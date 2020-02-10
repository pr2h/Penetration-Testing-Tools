# automated_url_opener

<p>
##################################################<br>
# Tool    : url_opener                           
# Version : 1.2                                  
# Runs on : Windows                              
# Source  : https://github.com/pr2h/             
# Coded with Python 3                            
# Release Date : 10th February 2020              
##################################################</p><p><b>[ pr2h ]</b></p><p>Purpose    : Automation script used to open all URLs from a file in Firefox/ Chrome, creating a new tab for each URL.</p><p>This project is licensed under the terms of the MIT license.</p>
<p>
SAMPLE USAGE: python url_opener.py --browser <firefox/ chrome> --tabs <number_of_tabs> --file <filename> --whitelistcodes <response_codes><br>
EXAMPLE (1) : python url_opener.py --browser chrome --tabs 10 --file sample.txt<br>
EXAMPLE (2) : python url_opener.py -b chrome -f sample.txt -fc<br>
EXAMPLE (3) : python url_opener.py -b chrome --file sample.txt -wc 200,400,404 -t 5<br>
<br>
OPTIONS:<br>
--help OR -h            : HELP<br>
--browser or -b         : BROWSER SELECTION (chrome OR firefox)<br>
--tabs OR -t            : NUMBER OF TABS TO SIMULTANEOUSLY OPEN<br>
--file or -f            : FILE FOR URL INPUT<br>
--whitelistcodes or -wc : ONLY OPEN URLs WITH SPECIFIED RESPONSE CODES<br>
--forcecode or -fc      : FORCE DISPLAY RESPONSE CODES (WHEN -wc IS NOT USED) (slower)<br>
</p>
