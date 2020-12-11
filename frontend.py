'''
This is the frontend of our menu program
'''
#importing packages
from colorama import init
import termcolor as tc
import play_sound as ps
import someFunctions as sf
#initialise the colorama for use with termcolor
init() 
print(tc.colored("\t\t\t ***********************************", color='green', attrs=['blink']))
print(tc.colored("\t\t\t *                                 *",color='green', attrs=['blink']))
print(tc.colored("\t\t\t * ",color='green', attrs=['blink']), end='')
print(tc.colored(" Welcome To Sappy's python menu", "green", on_color='on_white',attrs=['bold',]),end='')
print(tc.colored(" *",color='green', attrs=['blink']))
print(tc.colored("\t\t\t *                                 *",color='green', attrs=['blink']))
print(tc.colored("\t\t\t ***********************************",color='green', attrs=['blink']))

def playSound(key):
    """
    Play a sound when a key is pressed
    """
    ps.keyboardPress(key)
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
    6.  configure yum
    7.  check hadoop status
    8.  create a directory
    9.  create a user
    10. execute a command in another system
    11. Launch ec2-instance
    12. Configure load balancer using haproxy
    13. Setup hadoop master and worker nodes
    14. Install docker on redhat
    15. exit
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
        else:
            break
