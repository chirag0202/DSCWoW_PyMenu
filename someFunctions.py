'''
This script contains some of the function codes
'''
import subprocess
from colorama import init
import termcolor as tc
from shutil import copyfile
import getpass as gp
init()

def hadoop():
    """
    This function uses ansible to create a hadoop filesystem
    """
    output = subprocess.run(['ansible-playbook','playbooks/hadoop.yml'])
    print(output)

def docker():
    """
    This function uses ansible ti install docker on the target node
    """
    output = subprocess.run(['ansible-playbook','playbooks/docker.yml'])
    print(output)

def haproxy():
    """
    This function uses ansible to create a loadbalancer on AWS using haproxy
    """
    output = subprocess.run(['ansible-playbook','playbooks/haproxy.yml'])
    print(output)

def webserver_aws():
    """
    This function uses ansible to create a loadbalancer on AWS using haproxy
    """
    output = subprocess.run(['ansible-playbook','playbooks/webserver.yml'])
    print(output)

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

def webserver_status_remote():
    """
    Checks status of webserver on remote ip
    """
    ip = input(tc.colored("Enter remote ip: ", 'green', attrs=['bold']))
    output = subprocess.run(['ssh' ,f'root@{ip}', 'systemctl', 'status', 'httpd', '| grep' ,'active'])
    output.stdout

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
    passwd = gp.getpass(tc.colored("Enter root password: ", color='green', attrs=['bold']))
    pkg_name = input(tc.colored("Enter package name: ", color='green', attrs=['bold']))
    pkg_state = input(tc.colored("Enter package state(present/absent): ", color='green', attrs=['bold']))
    hosts_file = "[packs]\n{0} ansible_connection=ssh ansible_user=root ansible_password={1}".format(host, passwd)
    with open("playbooks/roles/install package/hosts", 'w') as file:
        file.write(hosts_file)
    with open('playbooks/roles/install package/pkg_name.yml', 'w') as var_file:
        var_file.writelines("pkg_name: {0}".format(pkg_name))
        var_file.writelines("\n")
        var_file.writelines("pkg_state: {0}".format(pkg_state))
    
    output = subprocess.run(['ansible-playbook', 'playbooks/roles/install package/pkg.yml', '-i', 'playbooks/roles/install package/hosts'])
    if output.returncode == 0:
        print(tc.colored("Task completed successfully", color='green', attrs=['bold']))
    else:
        print(tc.colored("Task failed!!!", color='red', attrs=['bold']))

def service():
    """
    This function start, stop or restarts a service
    """
    host = input(tc.colored("Enter remote ip(leave blank for localhost): ", color='green', attrs=['bold']))
    passwd = gp.getpass(tc.colored("Enter root password: ", color='green', attrs=['bold']))
    svc_name = input(tc.colored("Enter service name: ", color='green', attrs=['bold']))
    svc_state= input(tc.colored("Enter service state(started/stopped/restarted): ", color='green', attrs=['bold']))
    svc_enable = input(tc.colored("Wether service should be enabled(True/False): ", color='green', attrs=['bold']))
    hosts_file = "[svcs]\n{0} ansible_connection=ssh ansible_user=root ansible_password={1}".format(host, passwd)
    with open("playbooks/roles/services/svcs_name.yml", 'w') as svc_var:
        svc_var.writelines("svc_name: {0}\n".format(svc_name))
        svc_var.writelines("svc_state: {0}\n".format(svc_state))
        svc_var.writelines("svc_enable: {0}\n".format(svc_enable))
    with open("playbooks/roles/services/hosts", 'w') as file:
        file.write(hosts_file)
    output = subprocess.run(['ansible-playbook', 'playbooks/roles/services/svc.yml', '-i', 'playbooks/roles/services/hosts'])
    if output.returncode == 0:
        print(tc.colored("Task completed successfully", color='green', attrs=['bold']))
    else:
        print(tc.colored("Task failed!!!", color='red', attrs=['bold']))

def create_user():
    """
    This function will create a new user
    """
    host = input(tc.colored("Enter remote ip(leave blank for localhost): ", color='green', attrs=['bold']))
    passwd = gp.getpass(tc.colored("Enter root password: ", color='green', attrs=['bold']))
    hosts_file = "[usr]\n{0} ansible_connection=ssh ansible_user=root ansible_password={1}".format(host, passwd)
    username= input(tc.colored("Enter username: ", color='green', attrs=['bold']))
    user_passwd = gp.getpass(tc.colored("Enter the password: ", color='green', attrs=['bold']))
    state = input(tc.colored('Enter user state(present/absent): ', color='green', attrs=['bold']))
    with open('playbooks/roles/user/usr.yml', 'w') as user_file:
        user_file.writelines("user_name: {0}\n".format(username))
        user_file.writelines("user_passwd: {0}\n".format(user_passwd))
        user_file.writelines("user_state: {0}\n".format(state))
    with open('playbooks/roles/user/hosts', 'w') as file:
        file.write(hosts_file)
    output = subprocess.run(['ansible-playbook', 'playbooks/roles/user/user.yml', '-i', 'playbooks/roles/user/hosts'])
    if output.returncode == 0:
        print(tc.colored("Task completed successfully", color='green', attrs=['bold']))
    else:
        print(tc.colored("Task failed!!!", color='red', attrs=['bold']))

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

def create_dir():
    """
    This function creates a directory
    """
    host = input(tc.colored("Enter remote ip(leave blank for localhost): ", color='green', attrs=['bold']))
    passwd = gp.getpass(tc.colored("Enter root password: ", color='green', attrs=['bold']))
    hosts_file = "[dir]\n{0} ansible_connection=ssh ansible_user=root ansible_password={1}".format(host, passwd)
    with open('playbooks/roles/directory/hosts', 'w') as file:
        file.write(hosts_file)
    dir_name = input(tc.colored("Enter path of directory: ", color='green', attrs=['bold']))
    dir_state = input(tc.colored("Enter state of directory: ", color='green', attrs=['bold']))
    with open("playbooks/roles/directory/dir.yml", 'w') as dir_var:
        dir_var.writelines("dir_path: {0}\n".format(dir_name))
        if dir_state == 'present':
            dir_var.writelines("dir_state: directory\n")
        else:
            dir_var.writelines("dir_state: {0}\n".format(dir_state))
    output = subprocess.run(['ansible-playbook', 'playbooks/roles/directory/directory.yml', '-i', 'playbooks/roles/directory/hosts'])
    if output.returncode == 0:
        print(tc.colored("Task completed successfully", color='green', attrs=['bold']))
    else:
        print(tc.colored("Task failed!!!", color='red', attrs=['bold']))

def launch_ec2_instance():
    """
    This function launches ec2-instance
    """
    message = '''
    Please provide your access key and sceret key in a file called keys.yml in the format
    access_key: your_access_key
    secret_key: your_secret_key
    also provide your key file in the same folder
    press enter after you have done it.
    '''
    print(tc.colored(message, color='green', attrs=['bold']))
    input()
    key_name = input(tc.colored("Enter your ec2-instance key name: ", color='green', attrs=['bold']))
    copyfile('{0}.pem'.format(key_name), 'playbooks/roles/ec2-instance/{0}.pem'.format(key_name))
    subprocess.run(['chmod', '400', 'playbooks/roles/ec2-instance/{0}.pem'.format(key_name)])
    subprocess.run(['cp', 'keys.yml', 'playbooks/roles/ec2-instance/'])
    subprocess.run(['cp', 'index.html', 'playbooks/roles/ec2-instance/'])
    output = subprocess.run(['ansible-playbook', 'playbooks/roles/ec2-instance/aws-webserver.yml', '-i', 'playbooks/roles/ec2-instance/hosts', '--private-key', 'playbooks/roles/ec2-instance/{0}.pem'.format(key_name)])
    if output.returncode == 0:
        print(tc.colored("Task completed successfully", color='green', attrs=['bold']))
    else:
        print(tc.colored("Task failed!!!", color='red', attrs=['bold']))

def yum_config():
    """
    This module does the basoc configuration of yum
    """
    host = input(tc.colored("Enter remote ip(leave blank for localhost): ", color='green', attrs=['bold']))
    passwd = gp.getpass(tc.colored("Enter root password: ", color='green', attrs=['bold']))
    hosts_file = "[config_yum]\n{0} ansible_connection=ssh ansible_user=root ansible_password={1}".format(host, passwd)
    with open('playbooks/roles/yum config/hosts', 'w') as file:
        file.write(hosts_file)
    yum_name = input(tc.colored("Enter repo name: ",color='green', attrs=['bold']))
    yum_state = input(tc.colored("Enter repo state(present/absent): ",color='green', attrs=['bold']))
    yum_baseurl = input(tc.colored("Enter baseurl: ",color='green', attrs=['bold']))
    with open('playbooks/roles/yum config/yum_var.yml', 'w') as file:
        file.writelines("yum_name: {0}\n".format(yum_name))
        file.writelines("yum_state: {0}\n".format(yum_state))
        file.writelines("yum_baseurl: {0}\n".format(yum_baseurl))
    output = subprocess.run(['ansible-playbook', 'playbooks/roles/yum config/yum_config.yml', '-i', 'playbooks/roles/yum config/hosts'])
    if output.returncode == 0:
        print(tc.colored("Task completed successfully", color='green', attrs=['bold']))
    else:
        print(tc.colored("Task failed!!!", color='red', attrs=['bold']))
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
    #launch_ec2_instance()
    pass