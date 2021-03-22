import os
import getpass
from termcolor import colored

passwd = getpass.getpass("Enter the passsword - ")

if passwd!="akansh028":
    print("Wrong password")
    exit()

print("Want to run program Locally or Remotely ? ")

wish = input()

while True:
    os.system("clear")    

    if wish=="locally":
        print(colored("""Press 1: For date and time
Press 2: For calculator
Press 3: To install new software
Press 4: To open python interpretor
Press 5: For httpd web server configuration
Press 6: To open gedit text editor
Press 7: To start docker container
Press 8: To see docker images
Press 9: To launch docker container
Press 10: To list out running containers
Press 11: To get into docker container
Press 12: To pull any docker image
Press 13: To open firefox
Press 14: To create LVM partition
Press 15: Launching instance on aws cloud
Press 16: To exit 
    ""","red"))

        n = int(input("Enter your choice - "))
        if n==1:
            os.system("date")
        elif n==2:
            os.system("cal")
        elif n==3:
            software = input("Enter your software name - ")
            os.system("yum install {} -y".format(software))
        elif n==4:
            os.system("python")
        elif n==5:
            os.system("cd /var/www/html")
            os.system("echo 'Hello, myself Akansh Agarwal' > /var/www/html/lw.html")
            os.system("setenforce 0")
            os.system("systemctl stop firewalld")
            os.system("systemctl start httpd")
            print("Httpd configured sucessfully")
            os.system("ifconfig enp0s3")
        elif n==6:
            os.system("gedit")
        elif n==7:
                os.system("systemctl start docker")
                print("Docker started")
        elif n==8:
                os.system("docker images")
        elif n==9:
                osname = input("Enter your OS name\n")
                imgname = input("Enter your Image Name")
                os.system("docker run -dit --name {} {}".format(osname,imgname))
        elif n==10:
                os.system("docker ps -a")
        elif n==11:
                os.system("docker attach {}".format(osname))
        elif n==12:
                osname = input("Enter os name - ")
                version = input("Enter version - ")
                os.system("docker pull {}:{}".format(osname,version))
        elif n==13:
                os.system("firefox")
        elif n==14:
                os.system("pvcreate /dev/sdb")
                os.system("vgcreate arth-vg /dev/sdb")
                os.system("lvcreate --size 5G --name arth-lv arth-vg")
                os.system("mkfs.ext4 /dev/arth-vg/arth-lv")
                os.system("mount /dev/arth-vg/arth-lv /lvm")
        elif n==15:
                os.system("aws ec2 run-instances --image-id ami-015a6758451df3cb9 --instance-type t2.micro --count 1 --subnet-id subnet-9f7df1c6 --security-group-ids sg-02089309c3d33f824")
        elif n==16:
                print("exit")
                print(colored("Thanks for using","red"))
                break
        elif wish == "remotely":
                ip = input("enter the ip address: ")
                print("Press 1: for date command")
                print("Press 2: for cal command:")
                print("Press 3: to exit")

                n = int(input("enter the number: "))

                if n==1:
                        os.system("ssh {} date".format(ip))
                elif n==2:
                        os.system("ssh {} cal".format(ip))
                elif n==3:
                        exit()
        else:
                print("Not Valid")
        input("Press Enter to Proceed")

