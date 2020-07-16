import time
import sys
import subprocess
import os

os.system("clear")

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10./100)

slowprint('''\033[92m
if want find heartbleed vuln this tool is for you
''')

ip = input("Enter your target ip or domain:")	 
subprocess.call("nmap -d  --script ssl-heartbleed --script-args=vulns.showall  " + ip,shell=True)

