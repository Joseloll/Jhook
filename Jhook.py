import csv
import sys
import requests
import os
import time
import threading
import colorama
from colorama import Fore
os.system(f'cls & mode 85,20 & title Jhook! Version 1.0!')

def main():
   menu()

def menu():
   choices = input(Fore.CYAN + """
   /$$$$$       /$$   /$$                     /$$            
   |__  $$      | $$  | $$                    | $$            
      | $$      | $$  | $$  /$$$$$$   /$$$$$$ | $$   /$$      
      | $$      | $$$$$$$$ /$$__  $$ /$$__  $$| $$  /$$/      
 /$$  | $$      | $$__  $$| $$  \ $$| $$  \ $$| $$$$$$/       
| $$  | $$      | $$  | $$| $$  | $$| $$  | $$| $$_  $$       
|  $$$$$$/      | $$  | $$|  $$$$$$/|  $$$$$$/| $$ \  $$      
 \______/       |__/  |__/ \______/  \______/ |__/  \__/                   

                  Made By Jose  
                                                                                                                         
[1] Webhook Checker
[2] Webhook Deleter
[3] Webhook Spammer
[4] Exit
Enter Your Choice ↓
 """)
   if choices == "1":
    checker()
   elif choices == "2":
        deleter()
   elif choices =="3":
        spammer()
   elif choices =="4":
        sys.exit
   else:
         print("Enter The Right Option!")
         time.sleep(3)
         menu()

def checker():

   webhook= input("Enter Your Webhook Url:")
   r = requests.get(webhook)
   if r.status_code == 200:
    print(Fore.GREEN + "Webhook Is Working")
    time.sleep(2)
    menu()
   else:
        input(Fore.RED + 'Webhook Is Not Working.')
        time.sleep(2)
        menu()
      
        
(menu)

def deleter():
    url = input('Enter Your Webhook You Wanna Delete:')
    requests.delete(url)
    print(Fore.GREEN + "Webhook SucessFully Deleted") 
    time.sleep(2)
    menu()
   


  

def spammer():
   webhook = input('Enter Your Webhook Url:')
   message = input("Enter Your Message Here:")
   while True:
    r = requests.post(webhook, json={"content" : message})
    session = {201,204,409}
    if r.status_code in session:
        print(Fore.YELLOW + f"Sent Message Sucessfully")
    elif r.status_code == 409:
        print(Fore.MAGENTA + "You Are Being Rate Limited")
        time.sleep(5)
        (menu)
        for i in range(2):
            threading.Thread(target=spammer, args=(message,webhook,)).start
           
        menu()

spammed=1000    

main()
