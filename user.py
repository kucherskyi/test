# -*- coding: utf-8 -*-

import sys
import hashlib
import getpass

loginStatus = False
username = 0


# Function to register new user
def register():

    # function to check, if username exists
    def usr():
        file = open('users.txt', 'w')
        file.close()
        file_conn = open('users.txt')
        data = file_conn.read()
        file_conn.close()
        user_name = raw_input('Enter Username :')

        if user_name in data:
            print 'ALLAH AGBAR! USER EXISTS!'
            usr()
        return user_name

    user = usr()
    password = hashlib.sha224(getpass.getpass('Enter Password: ')).hexdigest()

    try:
        file_conn = open('users.txt', 'a')
        file_conn.write(user + '\n')
        file_conn.write(password + '\n \n')
        file_conn.close()
    except:
        sys.exit('There was a problem writing to the file!')

    print '\nYou are registered now!\n'
    registered()
    pass


# Function to check username and password
def process_file(file_name):

    user_names = []
    passwords = []

    try:
        file_conn = open(file_name)
        data = file_conn.readlines()

        for i in range(len(data)):
            if i % 2 == 0:
                user_names.append(data[i][:-1])
            else:
                passwords.append(data[i][:-1])

        file_conn.close()
    except:
        sys.exit('There was a problem reading the file!')

    return user_names, passwords


# Function to login with registered user
def registered():

    user_names, passwords = process_file('users.txt')
    pass_try = 0
    x = 3
    user = raw_input('Please Enter User Name: ')

    if user not in user_names:
        print ('Unkown User Name, Try again... \n')
        registered()

    while pass_try < x:
        pas = getpass.getpass('Enter Password: ')
        user_input = hashlib.sha224(pas).hexdigest()
        if user_input != passwords[user_names.index(user)]:
            pass_try += 1
            print 'Incorrect, ' + str(x-pass_try) + ' attemts left\n'
        else:
            pass_try = x+1

    if pass_try == x:
        sys.exit('Incorrect Password, closing \n')

    print 'You are logged in!'
    global loginStatus
    loginStatus = True
    global username
    username = user
