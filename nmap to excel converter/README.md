# nmap_to_xl_conv (nmap to excel converter)

<b>Tool Info :</b> nmap_to_xl_conv; Version : 1.5; Src : https://github.com/pr2h/; Coded with Python 2.7;

<b>[ pr2h ]</b>

<b>USAGE EXAMPLE:</b>

	C:\Users\RandomUser\Desktop>python nmap_to_xl_conv.py

	Enter filename: C:\Users\RandomUser\Desktop\nmap_out\convert_this.txt

	File saved as : C:\Users\RandomUser\Desktop\nmap_out\convert_this.xlsx

<b>Purpose    :</b> This script is designed to present the nmap output (.txt) in an excel file for easier viewing for pentest

<b>TOOL Input :</b> nmap output .txt file (generated with the -oN command in nmap)

<b>TOOL Output:</b> Excel file mapping IPs with corresponding open ports as indicated by the nmap output text file.
			 It will be placed in the same directory as the 'TOOL Input' file.

<b>Tool Usage Help:</b>

1. Run the .py file. Make sure you have 'openpyxl' installed in the system: <i>python nmap_to_xl_conv.py</i>

It can be obtained by:

	a. pip install openpyxl
	
	OR

	b. Downloaded and installed from 'https://pypi.python.org/pypi/openpyxl'

2. Enter the filename. If the 'TOOL Input' file is located in any directory other than the .py file, enter the filename with the directory.

The 'TOOL Input' file can be anywhere in the system, but make sure to enter the correct full path.

	Same directory example : 'convert_this.txt'

	Other directory example: 'C:\Users\RandomUser\Desktop\convert_this.txt'

3. The 'TOOL Output' Excel file is placed in the same directory as the 'TOOL Input' file with the same name.
