#Task fizz-buzz:
#You have three numbers, they are entered from the console.
# The first number is called fizz, the second is called buzz.
# To the third, it is necessary to add up from the unit.
# Looking at the current number if it is a multiple of fizz –
# should output F instead of a number. If the number is a multiple of buzz -
# should output B instead of a number.
# If the number is a multiple of both fizz and buzz, FB should be displayed.
# If it is not a multiple of anything, we output the number.
# And so - until the third entered number is reached.
#Example of condition and result: Numbers 2, 5, 18 are entered
# The conclusion should be as follows: 1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F

fizz, buzz, num = (int(str) for str in input().split(' '))

for i in range(1,num+1):
    if not i%fizz and not i%buzz:
        print('FB', end = ' ')
    elif not i%fizz:
        print('F', end = ' ')
    elif not i%buzz:
        print('B', end = ' ')
    else:
        print(i, end = ' ')
