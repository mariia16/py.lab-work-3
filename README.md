##Braine academy. Python Course. Laboratory Work #3

<b>Laboratory Work #3.4.</b>
<div>
   <i>Write a progam:</i>
   <ol>
  Write a program, which takes a year as input and returns message
if this is a leap year or note.
Please handle the exceptions which may arise is a user will enter non-numeric symbols.
Additional task – to show the closest leap year in casen
if entered year is not leap Optional task -
Add a possibility to print all the leap years within given range
1. Remind students about using input() functions
2. Leap year must be divided to 4 without remaining AND to 100 OR 400 without remaining too
3. Make sure program won’t be closed just after execution
4. add a functionality, which will show the closets leap year(no matter earlier of later) in case
if entered year is not leap
5. OPTIONAL. Add a possibility to print all the leap years within given range
   </ol>
</div>

<h6>Here is it solution code:</h6> 
```
try:
    year = int(input('Please, enter year'))
except ValueError:
    print('Not anumber passed')

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Leap year is ()'.format(year))
    print('It is a leap year! 366 days in a year!\n')
else:
    print('It is not a leap year! 365 days in a year!\n')
    for item in (year + 1, year - 1, year + 2, year - 2, year + 3, year - 3):  # Check close years is they are leap.
        if (item % 4 == 0) and (item % 100 != 0) or (item % 400 == 0):
            print('The closest leap year is: {}'.format(item))
            break
while True:
	response = (input('Do you want to enter the range? (Y/N) '))
	if response == 'Y':		# If a user wants to see all leap years within the range
		start_year = int(input('Enter the start year: '))
		end_year = int(input('Enter the end year: '))
		for year in range(start_year, end_year + 1):		# Checking all years within the range
			if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
				print('Leap year is: {}'.format(year))```

<b>Laboratory Work #3.5.</b>
<div>
   <i>Write a progam:</i>
   <ol>
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
    </ol>
</div>

<h6>Here is it solution code:</h6> 
```
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
        print('Empty names are considered as a breach try!')```