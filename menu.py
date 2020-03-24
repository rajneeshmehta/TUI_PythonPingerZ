import os
os.system("tputsetaf 1")
print("""\t\t\tWelcome to Our TUI
				Created by PythonPingerZ""")

os.system("tput setaf 8")
print("\t\t\t-------------------------------------------------------")

print("""Press 1: to see Date
Press 2 :to check cal
Press 3 : conf web server
Press 4 :to ceate user
Press 5 :create file
Press 6 :to setup NetWork
Press 7 :to exit""")
choice = int(input("Enter your choice : "))
location = input("Enter where you want to run command: ")
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
        os.system("")
elif location == remote:
    Server_IP = input("Enter the server IP: ")
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

