from getpass import getpass
from paramiko.ssh_exception import SSHException


try:    
    #Module for output coloring
    from netmiko import ConnectHandler
    from netmiko.ssh_exception import NetMikoTimeoutException
    from netmiko.ssh_exception import AuthenticationException

except ImportError:
    print "\n### Module colorama needs to be installed on your system. ###\n"
    print "### Download it from: https://github.com/ktbyers/netmiko ###\n"
    print "### Or just install it via pip:  ' pip install netmiko '   ###\n"
    sys.exit()

try:
    ans=True
    while ans:
        print"""\n>>>>> Vendors List <<<<<\n
        1.Cisco
        2.Juniper
        3.Arista
        4.HP
        5.Exit/Quite
        """
        ans=raw_input("\n>>>>> Choose one of them? : ")
        if ans=="1":
            ans2=True
            while ans2:
                print """\n>>>>> Which Cisco device do you have? \n
        1.Cisco IOS
        2.Cisco IOS-XE
        3.Cisco IOS-XR
        4.Cisco NX-OS
        5.Cisco ASA
        6.Back to Vendors
        7.Exit
        """
                ans2=raw_input("\n>>>>> Choose one of the above mentioned device types? : ")
                ans2 = int(ans2)
                devtypes = [0,"cisco_ios","cisco_xe","cisco_xr","cisco_nxos","cisco_asa"]
                if 0<ans2<6:
                    devtype = devtypes[ans2]
                    print "\n>>>>>> You Choosed %s <<<<<<\n" %devtype
                    ans = False
                    cmd = "show run"
                    break
                elif ans2== 6:
                    break
                elif ans2== 7:
                    print "\n>>>>>>>>>> Goodbye !! <<<<<<<<<<\n" 
                    exit()
                else:
                    print "\n NOT Valid !!! Please Try again"
        elif ans=="2":
            print "\n>>>>> You Choosed 'Juniper' <<<<<'\n"
            ans = False
            devtype = "juniper"
            cmd = "show configuration"
            ans = False
            break
        elif ans=="3":
            print "\n>>>>> Sorry :( Arista Devices do not supported yet <<<<<"
        elif ans=="4":
            print "\n>>>>> Sorry :( Hp Devices do not supported yet <<<<<"
        elif ans=="5":
            print "\n>>>>>>>>>> Goodbye !! <<<<<<<<<<\n" 
            ans = None
            exit()
        else:
            print "\n>>>>> Not Valid Choice Try again <<<<<"  
            continue

    username = raw_input("\n>>>>> Please Enter Your SSH Usernmae : ")
    password = getpass()
    
    print "\n>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<\n"
    
    IPs = raw_input("\n>>>>> Please enter the name of the file that contains IP addresses : ")
    
    with open(IPs) as f:
        myIPs = f.read().splitlines()
    
    for IP in myIPs:
        print "\n >>>>> Establishing Connection to . . . " + IP
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
            print "/n!!!!!!!!!! Authentication failed for: %s !!!!!!!!!!\n" %ip
            continue
        
        except (NetMikoTimeoutException):
            print "/n!!!!!!!!!! Time out to device: %s !!!!!!!!!!\n" %ip
            continue
            
        except (EOFError):
            print "/n!!!!!!!!!! End of file while attempting device: %s !!!!!!!!!!\n" %ip
            continue
        
        except (SSHException):
            print "/n!!!!!!!!!! SSH problem!!! Check SSH on device %s !!!!!!!!!!\n" %ip
            continue  
        except Exception as otherError:
            print "/n!!!!!!!!!! Some Other Error !!!!!!!!!!\n"
            continue
except KeyboardInterrupt:
    print "\n\n!!!!!!!!!! Program aborted by user. Exiting... !!!!!!!!!!\n"  



