import sys, operator


print('This is a simple calculator. There is no guarantee this program will work ')
print('Please type \"help\" to show the list of commands')

# Asks the user what command they would like to run
while True:
    userCommand = input('''\nWhat command would you like to use? Please input a command below.
    help: Shows a list of commands
    quit: Quits the program.
    run: Starts the program.\n''')
    userCommand = userCommand.lower()
    if userCommand == 'help':
        continue
    elif userCommand == 'quit':
        print('Program terminated. ')
        sys.exit()
    elif userCommand == 'run':
        print('Starting program... ')
    else:
        print('Input not recognized.')
        continue

# Asks the user what they would like to do
    numberOne = int(input('What is the first number? '))

    userAction = input('''\nWhat operation would you like to use? Please type in a command.
    add: Adds 2 numbers
    sub: Subtracts 2 numbers
    div: Divides 2 numbers
    mul: Multiplies 2 numbers\n''')

    numberTwo = int(input('What is the second number? '))


    if userAction == 'add':
        finalNumb = operator.add(numberOne, numberTwo)
    elif userAction == 'sub':
        finalNumb = operator.sub(numberOne, numberTwo)
    elif userAction == 'div':
        finalNumb = operator.truediv(numberOne, numberTwo)
    elif userAction == 'mul':
        finalNumb = operator.mul(numberOne, numberTwo)
    else:
        print('Command not recognized.')
