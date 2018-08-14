from getpass import getpass
import json
from pyntc import ntc_device as NTC
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException

try:
    username = raw_input("Please Enter Your SSH Usernmae : ")
    password = getpass()
    
    print ". . . . . . . . . . . . \n"
    print ". . . . . . . . . . . . \n"
    
    IPs = raw_input("Please Enter name of the file that contains IP addresses : ")
    
    with open(IPs) as f:
        myIPs = f.read().splitlines()
    
    for IP in myIPs:
        print "Establishing Connection to . .  " + IP
        ip = IP
        ios_device = {
            "device_type": "cisco_ios",
            "ip": ip,
            "username": username,
            "password": password
        }
        ios_device = NTC(host=ip, username=username, password=password,device_type="cisco_ios_ssh")
        try:
            ios_device.open()
            output = ios_device.running_config
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