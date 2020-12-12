'''
This is the frontend of our menu program
'''

from colorama import init
import termcolor as tc

#importing packages
from colorama import init
import termcolor as tc
import someFunctions as sf
#initialise the colorama for use with termcolor
init() 
print(tc.colored("\t\t\t ***************************************", color='green', attrs=['blink']))
print(tc.colored("\t\t\t *                                     *",color='green', attrs=['blink']))
print(tc.colored("\t\t\t * ",color='green', attrs=['blink']), end='')
print(tc.colored(" ", "green", on_color='on_white',attrs=['bold',]),end='')
print(tc.colored("Welcome To Radioactive python menu", "green", on_color='on_white',attrs=['bold',]),end='')
print(tc.colored(" *",color='green', attrs=['blink']))
print(tc.colored("\t\t\t *                                     *",color='green', attrs=['blink']))
print(tc.colored("\t\t\t ***************************************",color='green', attrs=['blink']))


def display_menu():
    """
    This function will display the menu to the user
    """
    menu = ''' 
    1.  print date
    2.  print calender
    3.  check webserver status
    4.  install webserver
    5.  install a package
    6.  start, stop or reload a service
    7.  configure yum
    8.  check hadoop status
    9.  create a directory
    10. create a user
    11. execute a command in another system
    12. Launch ec2-instance and configure webserver on top of it
    13. Configure load balancer using haproxy
    14. Setup hadoop master and worker nodes
    15. Install docker on redhat
    16. exit
    '''
    print(tc.colored(menu, color='green', attrs=['bold']))
if __name__ == '__main__':
    #This will run the full program
    while True:
        display_menu()
        print(tc.colored("Enter choice: ", 'green', attrs=['bold']), end='')
        ch = input()
        if ch == '1':
            sf.date()
        elif ch == '2':
            sf.calender()
        elif ch == '3':
            print(tc.colored("Do you want to run in localhost or remote ip:", 'green', attrs=['bold']), end=' ')
            choice = input()
            if choice == 'localhost':
                sf.webserver_status()
            else:
                sf.webserver_status_remote()
        elif ch == '4':
            print(tc.colored("Do you want to run in localhost or remote ip:", 'green', attrs=['bold']), end=' ')
            choice = input()
            if choice == 'localhost':
                sf.webserver_install()
            else:
                ip = input(tc.colored("Enter remote ip: ", 'green', attrs=['bold']))
                sf.webserver_install_remote(ip)
        elif ch == '5':
            sf.install_pkg()
        elif ch == '6':
            sf.service()
        elif ch == '9':
            sf.create_dir()
        elif ch == '10':
            sf.create_user()
        elif ch == '12':
            sf.launch_ec2_instance()
        elif ch == '14':
            sf.hadoop()
        else:
            break
