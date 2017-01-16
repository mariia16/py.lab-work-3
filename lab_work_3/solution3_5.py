'''
Write a program that will take username and password,
checks if they are in registered users dictionary,
if they are present – print “Access Granted”,
if not – handle it using KeyError Eception handling.
Raise RuntimeError and handle it if the name is empty.
For registered user, which is logged - let him know
if their password has unacceptable symbols (non alphanumeric)
and propose to change it using a dialog.
1. Tell the students about safer way to enter passwords (
import getpass, password = getpass.getpass('Please enter your password: ')):
2. Create a dict with users and passwords
3. Make a dialog to get username and password
4. Compare password with dict value for a given username
5. Handle the KeyError exception when there’ no such key (given name)
6. Raise and handle RuntimeError in case of empty name given as a breach try
7. Check password for a user entered if it’s have punctuation symbols (use string.punctuation)
8. Propose to change the password in case step 7 is True
'''

import getpass
import string

authorized_users = {
    'mariia': 'm1234',
    'irina': 'i1234',
    'tony': 't1234',
    'alex': 'a1234',
}
while True:
    try:
        name = input('Please enter your name: ')
        if name == '':
            raise RuntimeError
        print('Hello, {}'.format(name))
        password = input('Please enter your password: ')
        if authorized_users[name] == password:
            print('Access Granted!')
            break
    except KeyError:
        print("There's no such user registered!")
    except RuntimeError:
        print('Empty names are considered as a breach try!')

for symbol in authorized_users[name]:
    if symbol in string.punctuation:
        new_password = getpass.getpass(
            'Your password has unacceptable symbol in it: {} Please change your password: '.format(symbol))
        authorized_users[name] = new_password
        print('Your password is successfully updated!')

