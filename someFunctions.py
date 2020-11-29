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


if __name__ == "__main__":
    #run the functions for checking
    webserver_status()
    webserver_install()
    yum_install()
    create_user()