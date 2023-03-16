# SDSH
This uses flask module in python to help you host a webserver on your local machine.
You would need to configure your local machine to allow outside connections.

** Usage **
Source code file (sdsh.py):
``` python sdsh.py [file_path] ```

Exe file (sdsh.exe):
``` sdsh.exe [file_path] ```

The code is very easy to write. 

Inside a .sdsh file, write:
```
Home page
PATH /

I suggest replacing 127.0.0.1 with the actual IPv4 of your local machine for other people on your network to connect (If you want to let outsiders connect then you would need to configure to local machine to accept outside connections)
HOST "127.0.0.1"

Selects a port to run on
PORT 7000

Select an html file to run on the server
HTML index.html 
```
In the code, the PATH keyword is used to specify a routing for your webapp.
** Examples **: 
You want a routing to your feedback form:
```
PATH /feedback
HOST '127.0.0.1'
PORT 7000
HTML form.html
```
Now if you type "https:[YOUR_WEB_DOMAIN]/feedback" you will be redirected to your feedback form!

# Credits
sandum51 - Programmer
Friendly Bot - VsCode Language Support Extension

## Disclaimer: Note that running a webserver on your local machine would require to you implent many security measures to prevent attacks ##
