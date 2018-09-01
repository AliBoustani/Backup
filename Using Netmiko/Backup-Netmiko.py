from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException

try:
    ans=True
    while ans:
        print("""\n Vendors List:  \n
        1.Cisco
        2.Juniper
        3.Arista
        4.HP
        5.Exit/Quite
        """)
        ans=raw_input(" Choose one of them!? ")
        if ans=="1":
            ans2=True
            while ans2:
                print("""\n>>>>> Which Cisco device do you have? \n
                  1.Cisco IOS
                  2.Cisco IOS-XE
                  3.Cisco IOS-XR
                  4.Cisco NX-OS
                  5.Cisco ASA
                  6.Back to Vendors
                  7.Exit/Quit
                  """)
                ans2=raw_input(" Choose one of the above mentioned device types? ")
                if ans2=="1":
                    print("\n>>>>>You Choosed 'Cisco IOS' <<<<<'\n")
                    ans = False
                    devtype = "cisco_ios"
                    cmd = "show run"
                    break
                elif ans2=="2":
                    print("\n>>>>>You Choosed 'Cisco IOS-XE' <<<<<'\n")
                    ans = False
                    devtype = "cisco_xe"
                    cmd = "show run"
                    break
                elif ans2=="3":
                    print("\n>>>>>You Choosed 'Cisco IOS-XR' <<<<<'\n")
                    ans = False
                    devtype = "cisco_xr"
                    cmd = "show run"
                    break
                elif ans2=="4":
                    print("\n>>>>>You Choosed 'Cisco NXOS' <<<<<'\n")
                    ans = False
                    devtype = "cisco_nxos"
                    cmd = "show run"
                    break
                elif ans2=="5":
                    print("\n>>>>>You Choosed 'Cisco ASA' <<<<<'\n")
                    ans = False
                    devtype = "cisco_asa"
                    cmd = "show run"
                    ans = False
                    break
                elif ans2=="6":
                    break
                elif ans2=="7":
                    print("\n Goodbye") 
                    ans2 = False
                    ans = None
                    break
                else:
                    print("\n NOT Valid !!! Please Try again")
        elif ans=="2":
            print("\n>>>>>You Choosed 'Juniper' <<<<<'\n")
            ans = False
            devtype = "juniper"
            cmd = "show configuration"
            ans = False
            break
        elif ans=="3":
            print("\n Arista Devices does not supported yet")
        elif ans=="4":
            print("\n Hp Devices does not supported yet") 
        elif ans=="5":
            print("\n Till next time") 
            ans = None
    
        else:
            print("\n Not Valid Choice Try again")  


    username = raw_input("\n Please Enter Your SSH Usernmae : ")
    password = getpass()
    
    print ". . . . . . . . . . . . \n"
    print ". . . . . . . . . . . . \n"
    
    IPs = raw_input("\n Please Enter name of the file that contains IP addresses : ")
    
    with open(IPs) as f:
        myIPs = f.read().splitlines()
    
    for IP in myIPs:
        print "Establishing Connection to . .  " + IP
        ip = IP
        device = {
            "device_type": devtype,
            "ip": ip,
            "username": username,
            "password": password
        }
        try:
            net_connect = ConnectHandler(**device)
            output = net_connect.send_command(cmd)
            with open("DeviceIP__"+ ip, "w") as file:
                file.write(output)
                
        except (AuthenticationException):
            print "Authentication failed for:  " + ip
            continue
        
        except (NetMikoTimeoutException):
            print "Time out to device: " + ip
            continue
            
        except (EOFError):
            print "End of file while attempting device: " + ip
            continue
        
        except (SSHException):
            print "SSH problem!!! Check SSH on device " + ip
            continue
        
        except Exception as otherError:
            print "Some Other Error !!! : " + otherError
            continue
except KeyboardInterrupt:
    print "\n\nProgram aborted by user. Exiting...\n"  





