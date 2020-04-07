#import neccessory module
import os
import datetime
import getpass as gp

import math
import random
import pygame
#these variable acts as switch for changing the color
global_background = 63
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
password_background = 2
password_text = 15

now = datetime.datetime.now()
nows = now.strftime("%Y-%m-%d %H:%M:%S")
key = "Red@hat"
#-------------------------------------------------------------
def Message():
    os.system("tput setab {}".format(global_background))

    os.system("clear")

    os.system("tput setaf {}".format(welcome_text))
    os.system("tput setab {}".format(welcome_background))

    print(f"{' ':<15}{nows:>65}")

    print("\t\t\t\tWelcome to Our TUI")

    os.system("tput setaf {}".format(created_text))
    os.system("tput setab {}".format(created_background))
    print("\t\t\t     Created by PythonPingerZ     ")

    #os.system("while :; do echo -n -e \"`tput cup 0 72``date +%T``sleep 1`\b\b\b\b\b\b\b\b\"; done &")

#-------------------------------------------------------------
def protect():

    password =""
    while password !=key:
        os.system("tput cup 10 15") # move the text to 10 row and 15 column
        os.system("tput setaf {}".format(password_text))
        os.system("tput setab {}".format(password_background))
        password = gp.getpass("Enter your password to proceed:")
        if password == key:
            break
        else:
            os.system("tput cup 11 15") # move the text to 10 row and 15 column
            os.system("tput setaf 1")
            os.system("tput setab 15")
            print("Error Wrong Password!!")

#--------------------------------------------------------------
def options():
    Message()
    
    os.system("tput setaf {}".format(options_text))
    os.system("tput setab {}".format(options_background))
    print("""
    Press 1: to see Date
    Press 2 :to check cal
    Press 3 :conf web server
    Press 4 :to ceate user
    Press 5 :create file
    Press 6 :to setup NetWork*
    Press 7 :to check program is installed or not
    press 8 :to find location of software
    press 9 :to kill any process
    press 10:to enter in docker world
    press 11:to go inside hardisk
    Press 14:to Play Tic-Tac-Toe Game
    Press 15:to Play Snake Game
    Press 0 :to exit
    * Not completed                              """)
    os.system("tput setaf {}".format(choice_text))
    os.system("tput setab {}".format(choice_background))

#--------------------------------------------------------------
def local(choice):
    if choice == 1:
        os.system("date")
    elif choice == 2:
        os.system("cal")
    elif choice == 3:
        os.system("systemctl disable firewalld")
        os.system("systemctl enable httpd")
        os.system("touch /var/www/html/index.html")
        os.system("echo \"Welcome to your web page\" > /var/www/html/index.html")
        os.system("firefox localhost")
    elif choice == 4:
        name = str(input("Enter the name of user you want to add: "))
        os.system("useradd {}".format(name))
    elif choice == 5:
        filename = str(input("Please enter the name of file with its format: "))
        os.system("touch {}".format(filename))
        os.system("echo \"your file has been created\"")
    elif choice == 6:
        os.system("")
    elif choice == 7:
        programName = input("Please enter the program name you want to check if it is installed or not: ")
        os.system("rpm -q {}".format(programName))
    elif choice == 8:
        softwareName = input("Please enter the software name you want to find  location:")
        os.system("which {}".format(softwareName))
    elif choice == 9:
        programName = input("Please enter the program name you want to kill: ")
        os.system("killall {}".format(programName))
        
    elif choice ==10:
        Message()
        docker()
    elif choice == 11:
        insidehardisk()

    elif choice == 14:
        Message()
        tictac()
        Message()
    elif choice == 15:
        Message()
        snake()
        Message()
        
    input("Enter to continue....")

#-----------------------------------------------------------------
def remote(choice,Server_IP):
    if choice == 1:
        os.system("ssh {} date".format(Server_IP))
    elif choice == 2:
        os.system("ssh {} cal".format(Server_IP))
    elif choice == 3:
        os.system("")
    elif choice == 4:
        name = str(input("Enter the name of user you want to add: "))
        os.system("ssh {} useradd {}".format(Server_IP,name))
    elif choice == 5:
        filename = str(input("Please enter the name of file with its format: "))
        os.system("ssh {} touch {}".format(Server_IP,filename))
        os.system("ssh {} echo \"your file has been created\"".format(Server_IP))
    elif choice == 6:
        os.system("")
    elif choice == 7:
        programName = str(input("Please enter the program name you want to check if it is installed or not: "))
        os.system("ssh {} rpm -q {}".format(Server_IP,programName))
        os.system("tput setaf {}".format(exit_text))#before exiting make text white
        os.system("tput setab {}".format(exit_background))#and background black
        os.system("clear")#clear the screen
        exit()
    elif choice == 8:
        softwareName = input("Please enter the software name you want to find  location:")
        os.system("ssh {} which {}".format(Server_IP,softwareName))
    elif choice == 9:
        programName = input("Please enter the program name you want to kill: ")
        os.system("ssh {} killall {}".format(Server_IP,programName))

    os.system("tput setaf {}".format(continue_text))
    os.system("tput setab {}".format(continue_background))
    input("Enter to continue...")

#-----------------------------------------------------------------
def escape(choice):
    if choice == 0:
        os.system("tput setaf {}".format(exit_text))#before exiting make text white
        os.system("tput setab {}".format(exit_background))#and background black
        os.system("clear")#clear the screen
        exit()
#------------------------------------------------------------------
def r_protect():
    while True:
        passwd = gp.getpass("enter your password")
        realone = "rgrkr"
        if passwd == realone:
            print("authentication successfull")
            break
        else:
            print("authentication failed")
            o =input("Do you want to try again:yes/No  :")
            if o=='No':
                exit()
            else:
                os.system("clear")
#------------------------------------------------------------------
def insidehardisk():
    
    hardisk = input("enter hardisk name")
    print("""             press m:to take help through menu
             press n:to create partition
             press w:to save current partition
             press q:to exit
             press d:to delete partition""")
    os.system("fdisk {}".format(hardisk))
 #------------------------------------------------------------------   
def docker():
    while True:
        print("\t\t\tWELCOME TO DOCKER")
        print(""" press 1: to see information about docker
                  press 2: to see images in our system
                  press 3: to see containers in our system
                  press 4: to pull any image from public registry
                  press 5: to launch any image
                  press 6: to see history of images launched
                  press 7: to launch stoped container
                  press 8: to stop container[container name needed]
                  press 9: to rm container from system[ container ID needed]
                  press 10: to remove IMAGE from system
                  press 11: to delete all container
                  press 12: to use Developer's mod
                  press 13: to use Advance Docker
press 0:to exit from Docker's World""")
        choice =int(input("ENTER THE CHOICE"))
        if choice == 1:
            os.system("docker info")
        elif choice == 2:
            os.system("docker image ls")
        elif choice == 3:
            os.system("docker container ps")
        elif choice ==4:
            nameOfImage=input("ENTER THE NAME OF IMAGE YOU WANT TO PULL")
            os.system("docker pull {}".format(nameOfImage))
        elif choice ==5:
            nameOfImage=input("Enter the name of Image")
            option = input("Do you want to Nomaenclature of container:yes/No")
            if option =='No':
                A=input("Do you want to launch your image in default network:yes/No")
                if A=='yes':
                    os.system("docker run -it -d {}".format(nameOfImage))
                else:
                    net=input("Enter the name of network[warning :network must be created]")
                    os.system("docker run -it -d --network {0} {1}".format(net,nameOfImage))
            else:
                Name = input("Enter the name of container you want to keep")
                B=input("Do you want to launch your image in default network:yes/No")
                if B=='yes':
                    os.system("docker run -it -d --name {} {}".format(Name,nameOfImage))
                else:
                    net=input("Enter the name of network[warning :network must be created]")
                    os.system("docker run -it -d --name {0} --network {1} {2}".format(Name,net,nameOfImage))
        elif choice ==6:
            os.system("docker container ps -a")
        elif choice ==7:
            ContainerName =input("Enter the name of container")
            os.system("docker start {}".format(ContainerName))
            option =input("Do you want to enter in container :yes/No")
            if option =='yes':
                os.system("docker attach {}".format(ContainerName))
        elif choice ==8:
            nameofContainer= input("Enter the name of container to be stoped")
            os.system("docker container stop {}".format(nameofContainer))

        elif choice ==9:
            IdOfContainer =input("Enter the ID of container to be removed")
            os.system("docker container rm {}".format(IdOfContainer))
        elif choice ==10:
            nameOfImage =input("Enter the Name of Image to be removed")
            os.system("docker image rmi {}".format(nameOfImage))
        elif choice ==11:
            War =input("Warning :: you may lose your important data :yes/No")
            if War =='yes':
                os.system("docker container rm -f $(docker container ls -a -q)")
        elif choice ==12:
            while True:
                print(""""press 1: to create own network
                      press 2: to create an image
                      press 0: to exit from developer's mod""")
                choice =int(input("ENTER THE CHOICE"))
                if choice ==1:
                    nameOfDriver=input(""""Enter Name Of Drive
                                       1:bridge
                                       2:host
                                       3:null""")
                    if nameOfDriver=='bridge' or nameOfDriver=='host' or nameOfDriver =='null':
                        nameOfNetwork=input("Enter Name Of Network")
                        os.system("docker network create --driver {} {}".format(nameOfDriver,nameOfNetwork))
                        print("Network {} Created".format(nameOfNetwork))
                    else:
                        print("Driver Not available")
                elif choice ==2:
                    nameOfContainer =input("Name Of modifed Container")
                    nameOfImage=input("Enter Name Of Image you want to keep")
                    os.system("docker commit {} {}".format(nameOfContainer,nameOfImage))
                    print("Image {} Created".format(nameOfImage))
                elif choice ==0:
                    break
        elif choice ==0:

            os.system("tput setab 0")
            os.system("tput setaf 7")
            break

#----------------------------------------------------------------------
def snake():
    print("\t\t\t\tLaunching Game.....")
    os.system("sleep 1s")
    print("Checking for Updates\n")
    os.system("sleep 2s")
    print("""It may take some time depending on your internet connectivity and size of update\n\n""")
    os.system("sleep 2s")
    os.system("pip3 install pygame")
    os.system("sudo dnf install -y python3-tkinter")
    os.system("python3 snake.py")

#----------------------------------------------------------------------
def tictac():
    print("\t\t\t\tLaunching Game.....")
    os.system("sleep 1s")
    print("Checking for Updates\n")
    os.system("sleep 2s")
    print("""It may take some time depending on your internet connectivity and size of update\n\n""")
    os.system("sleep 2s")
    os.system("sudo dnf install -y python3-tkinter")
    os.system("python3 tictactoe.py")
