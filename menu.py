# import out user define function as well as variables
from Function import *

Message()
protect() # show message and ask for pasword
Message() #If passwaord is right then clear screen and show message again
os.system("tput setaf {}".format(location_text))
os.system("tput setab {}".format(location_background))
location = input("\nEnter where you want to run command(local or remote): ")

if location == "remote":
    os.system("tput setaf {}".format(server_ip_text))
    os.system("tput setab {}".format(server_ip_background))
    Server_IP = input("Enter the server IP: ")
    print("\nChecking connection......")
    os.system("sleep 3s")

#We have to add a connection checking code here


choice = -1  #let -1 be default

while choice != 0:
    if location == "local":
        options()
        choice = int(input("Enter your choice : "))
        local(choice)
    
    elif location == "remote":
        options()
        choice = int(input("Enter your choice : "))
        remote(choice,Server_IP)
    
    escape(choice)
