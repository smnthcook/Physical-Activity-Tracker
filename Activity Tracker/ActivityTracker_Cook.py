'''
ActivityTracker
Samantha Cook
4/21/2023
'''

import os

def main_menu():
    '''
    Main menu for the application.
    '''
    while True:
        
        print('1 - Create Account')
        print('2 - Delete Account')
        print('3 - Login')
        print('4 - Exit')
        option = input('Please enter your selection (1-4) >> ')
        if option == '1':
            create_account()
        elif option == '2':
            delete_account()
        elif option == '3':
            login()
        elif option == '4':
            break
        else:
            print('Invaild option selected!')
        print()
            
def create_account():
    '''
    Creates a new account if one does not exist If an account
    already exists, no account is created.
    '''
    name = input('Enter the name you want associated '
                'with the account >> ').lower().strip()
    if os.path.exists(name + '.txt'):
        print('This username already exists.')
    else:
        file = open(name + '.txt', 'x')
        file.close()
        print('The account was created successfully!')
        


def delete_account():
    '''
    Deletes an account if it exists.
    '''
    name = input('Enter the name you want to delete >> ').lower().strip()
    if os.path.exists(name + '.txt'):
        os.remove(name + '.txt')
        print('The account was deleted successfully!')
    else:
        print('No account exisists under that name!')
        
def login():
    '''
    Logs in to the user's account, if it exists.
    Calls the account menu if it exists.'
    '''
    name = input('Enter your username >> ').lower().strip()
    if os.path.exists(name + '.txt'):
        account_menu(name + '.txt')
    else:
        print('No account exists under that name!')


        
def account_menu(file_name):
        '''
        Account menu. Allows user to log, delete, and view activities
        '''
        print()
        while True:
            
            print('1 - Log Activities')
            print('2 - Delete Activity')
            print('3 - View Activities')
            print('4 - Exit to main menu')
            option = input('Please enter your selection (1-4) >> ')
            print()
            if option == '1':
                log_activities(file_name)
                
            elif option == '2':
                delete_activities(file_name)
                
            elif option == '3':
                view_activities(file_name)
                
            elif option == '4':
                break
            
            else:
                print('Invaild option selected!')
        


def log_activities(file_name):
    '''
    Logs multiple activities to the user's account. Writes the information
    to the file.
    '''
    repeat = "y"
    while repeat == 'y':
        
        activity_name = input('Enter the name of the activity >> ')
        hours = input('Enter the number of hours you did the activity >> ')
        calories = input('Enter the number of calories the activity burns per hour >> ')
        file = open(file_name, 'a')
        file.write(activity_name + ', ' + hours + ', ' + calories + '\n')
        file.close()
        repeat = input("Would you like to log another activity (y/n) >> ")
        print()



def delete_activities(file_name):
    '''
    Deletes multiple activities from the user's account.
    '''
    
    file = open(file_name, 'r')
    entries = file.readlines()
    file.close()
    
    repeat = "y"
    while repeat == "y":
        print("Your entries")
        for i in range(0, len(entries)):
            fields = entries[i].split(',')
            print(i + 1, '-', fields[0], 'for', fields[1], 'hours')
        print()
        index = int(input("Which activity would you like to delete (enter a number) >> ")) - 1
        if index < len(entries):
            entries.pop(index)
            print("Activity successfully deleted!")
        else:
            print("Invaild input. No activity at that number.")
        repeat = input("Do you want to delete another activity (y/n) >> ")
        print()
        
    file = open(file_name, "w")
    file.writelines(entries)
    file.close()
    

def view_activities(file_name):
    file = open(file_name, 'r')
    entries = file.readlines()
    file.close()
    for i in range(0, len(entries)):
        fields = entries[i].split(',')
        print(i + 1, '-', fields[0], 'for', fields[1], 'hours')

#main
main_menu()


