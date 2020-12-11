'''
This script contains some of the function codes
'''
import subprocess
from colorama import init
import termcolor as tc

init()
def date():
    """
    This function prints the date
    """
    output = subprocess.run("date")
    output.stdout

def calender():
    """
    This function prints the calender
    """
    output = subprocess.run('cal')
    output.stdout
def webserver_status():
    """
    This function checks the status of the webserver
    """
    output = subprocess.getoutput(cmd='systemctl status apache2 | grep active')
    print(output)
def webserver_status_remote():
    """
    Checks status of webserver on remote ip
    """
    ip = input(tc.colored("Enter remote ip: ", 'green', attrs=['bold']))
    output = subprocess.run(['ssh' ,ip, 'systemctl', 'status', 'httpd', '| grep' ,'active'])
    output.stdout
def webserver_install():
    '''
    This function will install webserver in the machine
    '''
    output = subprocess.run(['yum', 'install', 'httpd', '-y'])
    print(output)
def webserver_install_remote(ip):
    """
    Install webserver on remote ip
    """
    output = subprocess.run(['ssh', ip, 'yum', 'install', 'httpd', '-y', '&&', 'systemctl', 'start', 'httpd'], capture_output=True)
    if output.returncode == 1:
        print("httpd not installed")
    else:
        print("httpd installation successful")
def install_pkg():
    """
    This function will ask for a package name and install it
    """
    host = input(tc.colored("Enter remote ip(leave blank for localhost): ", color='green', attrs=['bold']))
    passwd = input(tc.colored("Enter root password: ", color='green', attrs=['bold']))
    pkg_name = input("Enter package name:")
    pkg_state = input("Enter package state(present/absent): ")
    hosts_file = "[packs]\n{0} ansible_connection=ssh ansible_user=root ansible_password={1}".format(host, passwd)
    with open("playbooks/install package/hosts", 'w') as file:
        file.write(hosts_file)
    with open('playbooks/install package/pkg_name.yml', 'w') as var_file:
        var_file.writelines("pkg_name: {0}".format(pkg_name))
        var_file.writelines("\n")
        var_file.writelines("pkg_state: {0}".format(pkg_state))
    
    output = subprocess.run(['ansible-playbook', 'playbooks/install package/pkg.yml', '-i', 'playbooks/install package/hosts'])
def create_user():
    """
    This function will create a new user
    """
    username = input("Enter username:")
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