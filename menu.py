#these variable acts as switch for changing the color
global_background = 3
welcome_text = 4
welcome_background = 10
created_text = 17
created_background = 14
location_text = 9
location_background = 15
options_text = 4
options_background = 11
choice_text = 17
choice_background = 15
exit_text = 15
exit_background = 0
server_ip_text = 4
server_ip_background = 10
continue_text = 4
continue_background = 13
# import necessory module so we can run cmd through python
import os
os.system("tput setab {}".format(global_background))

os.system("clear")

os.system("tput setaf {}".format(welcome_text))
os.system("tput setab {}".format(welcome_background))

print("\t\t\t\tWelcome to Our TUI")

os.system("tput setaf {}".format(created_text))
os.system("tput setab {}".format(created_background))
print("\t\t\t     Created by PythonPingerZ     ")

os.system("tput setaf {}".format(location_text))
os.system("tput setab {}".format(location_background))
location = input("Enter where you want to run command: ")

if location == "remote":
    os.system("tput setaf {}".format(server_ip_text))
    os.system("tput setab {}".format(server_ip_background))
    Server_IP = input("Enter the server IP: ")


choice = 0  #let 0 be the default

while choice != 7:
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
            os.system("")
            
    os.system("tput setaf {}".format(continue_text))
    os.system("tput setab {}".format(continue_background))
    input("Enter to continue...")
    os.system("tput setab {}".format(global_background))

    os.system("clear")
    



