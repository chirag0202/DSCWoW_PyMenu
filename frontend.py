'''
This is the frontend of our menu program
'''

from colorama import init
import termcolor as tc
import play_sound as ps
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
    4.  install a package using yum
    5.  configure yum
    6.  check hadoop status
    7.  create a directory
    8.  create a user
    9.  execute a command in another system
    10. Launch ec2-instance
    11. Configure load balancer using haproxy
    12. Setup hadoop master and worker nodes
    13. Install docker on redhat
    14. exit
    '''
    print(tc.colored(menu, color='green', attrs=['bold']))
    ch = input("Enter choice:")
    playSound(ch)
if __name__ == '__main__':
    #run the functions for checking
    display_menu()