import sys
import hashlib
import getpass


def register():
    def usr():
        file_conn = open('users.txt')
        data = file_conn.read()
        file_conn.close()
    
        user_name = raw_input('Enter username :')
        if user_name in data:
            print 'ALLAH AGBAR! USER EXISTS!'
            usr()
        
        return user_name
        
    user = usr()

    password = hashlib.sha224(getpass.getpass('Please Enter a Password: ')).hexdigest()

    try:
        file_conn = open('users.txt','a')
        file_conn.write(user + '\n')
        file_conn.write(password + '\n \n')
        file_conn.close()
    except:
        sys.exit('There was a problem writing to the file!')

    print '\nPassword safely stored \n'
    pass
    

def process_file(file_name):
    
    user_names = []
    passwords = []
    
    try:
        file_conn = open(file_name)
        data = file_conn.readlines()

        for i in range(len(data)): 
            if i%2 == 0:
                user_names.append(data[i][:-1])
            else:
                passwords.append(data[i][:-1])
            
        file_conn.close()
    except:
        sys.exit('There was a problem reading the file!')
        
    return user_names, passwords

def registered():

    print '\nUser & Password Authentication Program v.01\n'

    user_names, passwords = process_file('users.txt')
        
    pass_try = 0 
    x = 3
    
    user = raw_input('Please Enter User Name: ')
    
    if user not in user_names:
        sys.exit('Unkown User Name, terminating... \n')
        
    while pass_try < x:
        user_input = hashlib.sha224(getpass.getpass('Please Enter Password: ')).hexdigest()
        if user_input != passwords[user_names.index(user)]:
            pass_try += 1
            print 'Incorrect Password, ' + str(x-pass_try) + ' more attemts left\n'
        else:
            pass_try = x+1
            
    if pass_try == x:
        sys.exit('Incorrect Password, closing \n')

    print 'User is logged in!\n'        

print "Hi! Are You registered?"

if input('1 for YES \n2 for NO \n :') == 1:
    registered()
else:
    register()
