import csv
import sys
import requests
import os
import time
import threading
import webbrowser
import colorama
from colorama import Fore
os.system(f'cls & mode 85,20 & title Jhook! Version 1.2!')

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

                  Made By Josè#0001  
                                                                                                                        
[1] Download The Newest Version
[2] Webhook Checker
[3] Webhook Deleter
[4] Webhook Sender
[5] Webhook Spammer
[6] Exit
Enter Your Choice ↓
 """)
   if choices == "1":
    update()
   elif choices == "2":
        checker()
   elif choices == "3":
        deleter()
   elif choices =="4":
        sender()
   elif choices =="5":
        spammer()
   elif choices =="6":
        sys.exit
   else:
         print("Enter The Right Option!")
         time.sleep(3)
         menu()



def update():
    print("This Will Just Install The Newest Update For Jhook")
    url ="https://cdn.discordapp.com/attachments/996509828908318813/1001543793859891260/update.py"
    webbrowser.open(url);
    
    

def checker():

   webhook= input("Enter Your Webhook Url:")
   r = requests.get(webhook)
   if r.status_code == 200:
    print(Fore.GREEN + "Webhook Is Working")
    time.sleep(2)
    os.system("cls")
    menu()
   else:
        print(Fore.RED + 'Webhook Is Not Working.')
        time.sleep(2)
        os.system("cls")
        menu()
      
def sender():
    print("This Will Send A Message To The There Discord Webhook")
    webhook = input('Enter Your Discord Webhook: ')
    message = input('Enter Your Discord Message: ')
    send = requests.post(webhook,json={'content': message})
    r = requests.get(webhook)
    if r.status_code == 200:
        print(Fore.GREEN + "Message Sent Sucessfully")
        time.sleep(2)
        os.system('cls')
        menu()
    
    else:
        print(Fore.RED + "Message Failed To Send")
        time.sleep(2)
        os.system("cls")
        menu()


def deleter():  
    url = input("Enter Your Webhook URL To Delete: ")
    try:
        c = requests.get(url)
        if c.status_code == 404:
            print(Fore.RED + "Webhook Fail To Delete")
            time.sleep(2)
            os.system('cls')
            menu()
        else:
            requests.delete(url)
            print(Fore.GREEN + "Webhook Sucessfully Deleted")
    except:
        print("Failed to delete webhook")
    time.sleep(2)
    os.system("cls")
    menu()

  

def spammer():
   webhook = input('Enter Your Webhook Url:')
   message = input("Enter Your Message Here:")
   while True:
    r = requests.post(webhook, json={"content" : message})
    session = {201,204,409}
    if r.status_code in session:
        print(Fore.YELLOW + f"Sent Message Sucessfully")
    elif r.status_code == 429:
        print(f"{Fore.MAGENTA}You Are Being Rate Limited ({r.json()['retry_after']}ms){Fore.RESET}")
        time.sleep(r.json()["retry_after"] / 1000)
        time.sleep(5)
        (menu)
        for i in range(2):
            threading.Thread(target=spammer, args=(message,webhook,)).start
    else:
      print(Fore.RED + f'Webhook Deleted')
      time.sleep(2)
      os.system('cls')
      menu()

spammed=1000    

main()
