#these variable acts as switch for changing the color
# import out user define function as well as variables
from Function import *
Message()

os.system("tput setaf {}".format(location_text))
os.system("tput setab {}".format(location_background))
while True:
    passwd = getpass.getpass("enter your password")
    realone = "rgrkr"
    if passwd == realone:
        print("authentication secessfull")
        break
    else:
        print("authentication failed")
        o =input("Do you want to try again:yes/No  :")
        if o=='No':
            exit()
        else:
            os.system("clear")

location = input("\nEnter where you want to run command(local or remote): ")

if location == "remote":
    os.system("tput setaf {}".format(server_ip_text))
    os.system("tput setab {}".format(server_ip_background))
    Server_IP = input("Enter the server IP: ")
    print("\nChecking connection......")
    os.system("sleep 2s")

#We have to add a connection checking code here


choice = -1  #let -1 be default

while choice != 0:
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
    choice = int(input("Enter your choice : "))
    if location == "local":
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
            os.system("clear")  
            os.system("tput setab 4")
            os.system("tput setaf 0")
            os.system("systemctl start docker")
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
                    os.system("docker start {}".format(ContainerN))
                    option =input("Do you want to enter in container :yes/No")
                    if option =='yes':             
                        os.system("docker attach {}".format(ContainerName))
                elif choice ==8:
                    nameofContainer= input("Enter the name of container to be stoped")
                    os.system("docker container stop {}".format(nameOfContainer))
    
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
                input("Enter to continue....")
                os.system("clear")        

        
        
        
        
        elif choice == 0:
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
    os.system("tput setab {}".format(global_background))

    os.system("clear")
