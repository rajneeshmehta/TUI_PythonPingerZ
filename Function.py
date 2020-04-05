#import neccessory module
import os 
<<<<<<< HEAD
import getpass
=======
import getpass as gp
>>>>>>> 4dcf651ea56fd03a9a4fac8e9c3fe4ea803aaa5a
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

key = "Red@hat"
#-------------------------------------------------------------
def Message():
    os.system("tput setab {}".format(global_background))

    os.system("clear")

    os.system("tput setaf {}".format(welcome_text))
    os.system("tput setab {}".format(welcome_background))

    print("\t\t\t\tWelcome to Our TUI")

    os.system("tput setaf {}".format(created_text))
    os.system("tput setab {}".format(created_background))
    print("\t\t\t     Created by PythonPingerZ     ")

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
    Press 3 :conf web server*                    
    Press 4 :to ceate user                       
    Press 5 :create file                         
    Press 6 :to setup NetWork*                   
    Press 7 :to check program is installed or not
    press 8 :to find location of software        
    press 9 :to kill any process                 
    press 10:to enter in docker world            
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
        os.system("")
    elif choice == 4:
        name = str(input("Enter the name of user you want to add: "))
        os.system("useradd {}".format(name))
    elif choice == 5:
        filename = str(input("Please enter the name of file with its format: "))
        os.system("cat {}".format(filename))
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
        print("\t\t\tWELCOME TO DOCKER")
        os.system("systemctl start docker")


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
                  press 11: to delete all container""")
        choice =int(input("ENTER THE CHOICE:"))
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
    os.system("tput setaf {}".format(continue_text))
    os.system("tput setab {}".format(continue_background))
    input("Enter to continue...")
#-----------------------------------------------------------------
def remote(choice):
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


