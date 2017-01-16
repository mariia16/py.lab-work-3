'''
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
'''

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
				print('Leap year is: {}'.format(year))

