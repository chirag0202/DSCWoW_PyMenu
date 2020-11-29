'''
This script contains some of the function codes
'''
import subprocess

def webserver_status():
    """
    This function checks the status of the webserver
    """
    output = subprocess.getoutput(cmd='systemctl status apache2 | grep active')
    print(output)

def webserver_install():
    '''
    This function will install webserver in the machine
    '''
    output = subprocess.run(['yum', 'install', 'httpd', '-y'])
    print(output)
def yum_install():
    """
    This package will ask for a package name and install it
    """
    pkg_name = input("Enter package name:")
    output = subprocess.run(['yum', 'install', pkg_name, '-y'], capture_output=True)
    if output.returncode == 1:
        print("{0} not installed".format(pkg_name))
    else:
        print("{0} installation successful".format(pkg_name))
def create_user():
    """
    This function will create a new user
    """
    username= input("Enter username:")
    passwd = input("Enter the password:")
    output = subprocess.run(['useradd', username])
    subprocess.run(['passwd', passwd])
    if output.returncode == 1:
        print("User not created")
    else:
        print("User created")

def validIP(ip):
    """
    This function checks if an ip is valid or not
    """
    ip_slice = ip.split('.')
    print(ip_slice)
    for item in ip_slice:
        if int(item) > 255:
            return False
    return True

def isPingAble(ip):
    """
    This checks wether the ip is pingabe or not
    returns true if pingable false otherwise
    """
    cmd = ['ping', '-c', '1', ip]
    if subprocess.run(cmd).returncode == 0:
        return True
    return False

def execAnother():
    """
    This function will allow to excute a remote command in another system
    """
    ip = input("Enter the remote ip:")
    if not validIP(ip) and isPingAble(ip):
        print("Error!!!\nWrong IP")
    else:
        cmd = input("Enter the command:")
        output = subprocess.run(['ssh', ip, cmd])
        if output.returncode == 0:
            print("Command ran successfully")
        else:
            print("Command is unsucessfull")
            print("Error code: ", output.returncode)

if __name__ == "__main__":
    #run the functions for checking
    #to check a function uncomment and see if it works or not
    #webserver_status()
    #webserver_install()
    #yum_install()
    #create_user()
    #print(validIP("192.168.43.178"))
    #print(isPingAble('192.168.43.178'))
    #execAnother()
    pass