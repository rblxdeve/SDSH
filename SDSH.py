from sys import argv
from flask import Flask
import subprocess

app = Flask(__name__)
routing = ''
hoston = ""
porton = None
contenthtml = None

try:
    with open(argv[1], 'r') as f:
        content = f.readlines()
        for i in content:
            if i.startswith("HOST"):
                hoston = eval(i[5:]).strip()
            if i.startswith("PORT"):
                porton = int(i[5:].strip())
            if i.startswith("HTML"):
                contenthtml = open(eval(i[5:]).strip(), 'r').read()
            if i.startswith("PATH"):
                routing = i[5:].strip()
except FileNotFoundError as E:
    print(f"Error Detected => {E}")
except Exception as E:
    print(f"Error Detected => {E}")

@app.route(routing)
def home():
    return contenthtml

if __name__ == '__main__':
    try:
        if porton == None:
            app.run(debug=True, host=hoston)
        else:
            app.run(debug=True, host=hoston, port=porton)
    except Exception as E:
        print(f"Error Detected => {E}")
