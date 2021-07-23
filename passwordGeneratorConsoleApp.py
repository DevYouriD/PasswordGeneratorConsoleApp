import random

status = True

lower_case_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers =            ['0','1','2','3','4','5','6','7','8','9']
punctual_marks =     ['!','@','#','$','%','^','&','*']

while status:
    print('')
    print("Choose a password length between 5 and 128: ")
    print("Press Enter to exit ")
    print('')
    userInput = input()

    #CHOICE OF PASSWORD LENGTH
    if userInput:
        include_lower_case_letters = input("Do you want to include lower case letters in your password? Y/N \n")
        include_upper_case_letters = input("Do you want to include upper case letters in your password? Y/N \n")
        include_numbers =            input("Do you want to include numbers case letters in your password? Y/N? \n")
        include_punctual_marks =     input("Do you want to include punctual marks in your password? Y/N? \n")

        afterChoiceList = []

        if include_lower_case_letters == 'y' or include_lower_case_letters == 'Y':
            for x in lower_case_letters:
                afterChoiceList.append(x)

        if include_upper_case_letters == 'y' or include_upper_case_letters == 'Y':
            for x in upper_case_letters:
                afterChoiceList.append(x)

        if include_numbers == 'y' or include_numbers == 'Y':
            for x in numbers:
                afterChoiceList.append(x)

        if include_punctual_marks == 'y' or include_punctual_marks == 'Y':
            for x in punctual_marks:
                afterChoiceList.append(x)

        random.shuffle(afterChoiceList)

        print(afterChoiceList)

        password = []
        for x in range(5,int(userInput)):
            y = random.randint(0,len(afterChoiceList)-1)
            password.append(afterChoiceList[y])
        random.shuffle(password)
        password = ''.join([str(elem) for elem in password])
        print('')
        print('Your new password = ' + password)
        print('')

    #CHOICE OF EXIT
    elif userInput == '':
        exit()
    #WRONG INPUT
    # elif userInput < 5 or userInput > 128:
    #     print('Please fill in a number between 5 and 128.\n')
    #WRONG INPUT
    else:
        print('')
        print('Please fill in a valid input.\n')

