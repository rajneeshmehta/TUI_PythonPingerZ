#these variable acts as switch for changing the color
# import out user define function as well as variables
from Function import *
Message()

os.system("tput setaf {}".format(location_text))
os.system("tput setab {}".format(location_background))
location = input("\nEnter where you want to run command: ")

if location == "remote":
    os.system("tput setaf {}".format(server_ip_text))
    os.system("tput setab {}".format(server_ip_background))
    Server_IP = input("Enter the server IP: ")
    print("\nChecking connection......")
    os.system("sleep 2s")

#We have to add a connection checking code here


choice = 0  #let 0 be the default

while choice != 7:
    Message()
    
    
    os.system("tput setaf {}".format(options_text))
    os.system("tput setab {}".format(options_background))

    print("""
Press 1: to see Date     
Press 2 :to check cal    
Press 3 :conf web server 
Press 4 :to ceate user   
Press 5 :create file     
Press 6 :to setup NetWork
Press 7 :to exit         """)
    os.system("tput setaf {}".format(choice_text))
    os.system("tput setab {}".format(choice_background))
    choice = int(input("Enter your choice : "))
    if location == "local":
        if choice == 1:
            os.system("date")
        elif choice == 2:
            os.system("cal")
        elif choice == 3:
            os.system("")
        elif choice == 4:
            os.system("")
        elif choice == 5:
            os.system("")
        elif choice == 6:
            os.system("")
        elif choice == 7:

            os.system("tput setaf {}".format(exit_text))#before exiting make text white
            os.system("tput setab {}".format(exit_background))#and background black
            os.system("clear")#clear the screen
            exit()

    elif location == "remote":
        
        if choice == 1:
            os.system("ssh {} date".format(Server_IP))
        elif choice == 2:
            os.system("ssh {} cal".format(Server_IP))
        elif choice == 3:
            os.system("")
        elif choice == 4:
            os.system("")
        elif choice == 5:
            os.system("")
        elif choice == 6:
            os.system("")
        elif choice == 7:
            os.system("tput setaf {}".format(exit_text))#before exiting make text white
            os.system("tput setab {}".format(exit_background))#and background black
            os.system("clear")#clear the screen
            exit()
            
    os.system("tput setaf {}".format(continue_text))
    os.system("tput setab {}".format(continue_background))
    input("Enter to continue...")
    os.system("tput setab {}".format(global_background))

    os.system("clear")
    
