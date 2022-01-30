from colorama import Fore
import requests

print(Fore.GREEN+"""
████████╗███████╗███╗░░░███╗██████╗░  ███╗░░░███╗░█████╗░██╗██╗░░░░░
╚══██╔══╝██╔════╝████╗░████║██╔══██╗  ████╗░████║██╔══██╗██║██║░░░░░
░░░██║░░░█████╗░░██╔████╔██║██████╔╝  ██╔████╔██║███████║██║██║░░░░░
░░░██║░░░██╔══╝░░██║╚██╔╝██║██╔═══╝░  ██║╚██╔╝██║██╔══██║██║██║░░░░░
░░░██║░░░███████╗██║░╚═╝░██║██║░░░░░  ██║░╚═╝░██║██║░░██║██║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═╝░░░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝
                                                        - https://github.com/terminal1337""")




import sys
import time
from time import sleep
for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write(Fore.RED+"Loading[%-10s] %d%%" % ('='*i, 1*i))
    sys.stdout.flush()
    sleep(0.02)
print("\n \n")
domains = input(Fore.LIGHTMAGENTA_EX+"Do you want to check the available domains?[Y/n]: ")
if domains == "Y":
    print(Fore.LIGHTMAGENTA_EX+requests.get("https://www.1secmail.com/api/v1/?action=getDomainList").text)
elif domains =="n":
    pass
else:
    sys.exit(Fore.LIGHTMAGENTA_EX+"Error: Invalid Input")

count = int(input(Fore.LIGHTBLUE_EX+"How Many emails do you want to generate?[1-10]: "))
print(Fore.LIGHTBLUE_EX+"Generating Emails....")
for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write(Fore.BLUE+"Loading[%-10s] %d%%" % ('='*i, 1*i))
    sys.stdout.flush()
    sleep(0.02)
print("\n \n")

print(Fore.BLUE+"Email Generated:"+requests.get(f"https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={count}").text)

ask_email = input(Fore.LIGHTGREEN_EX+"Do you want fetch email from an email id?[Y/n]: ")

if ask_email == "Y":
    pass
else:
    sys.exit()
email_user = input(Fore.LIGHTGREEN_EX+"Enter the username of the email: ")
email_domain = input(Fore.LIGHTGREEN_EX+"Enter the domain of the email: ")
for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write(Fore.YELLOW+"Fetching Emails[%-10s] %d%%" % ('='*i, 1*i))
    sys.stdout.flush()
    sleep(0.02)
print("\n \n")

print(Fore.YELLOW+"Showing Recent Inboxs: \n " + requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={email_user}&domain={email_domain}").text)

id = int(input(Fore.LIGHTRED_EX+"Enter the id of the inbox to fetch complete message:"))
print(Fore.LIGHTRED_EX+"Raw Email: \n "+requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={email_user}&domain={email_domain}&id={id}").text)

print(Fore.LIGHTWHITE_EX+"Thanks for Using Our Service!! Kindly Star the repo on github :)")
exi = int(input(Fore.LIGHTWHITE_EX+"[1] Do you want to exit? or [2] fetch inbox again [3] fetch email again?"))
if exi == 1:
    sys.exit(Fore.LIGHTWHITE_EX+"tada...")
elif exi == 2:
    print(Fore.LIGHTWHITE_EX+"Showing Recent Inboxs: \n " + requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={email_user}&domain={email_domain}").text)
elif exi == [3]:
    print(Fore.LIGHTWHITE_EX+"Raw Email: \n "+requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={email_user}&domain={email_domain}&id={id}").text)