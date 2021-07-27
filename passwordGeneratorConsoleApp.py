import random

lower_case_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers =            ['0','1','2','3','4','5','6','7','8','9']
punctual_marks =     ['!','@','#','$','%','^','&','*']

status = True

while status:
    print('')
    print('Choose a password length between 5 and 128 characters: ')
    print('Press Enter to exit ')
    print('')
    userInput = input()

    #CHOICE OF PASSWORD LENGTH
    if userInput.isdigit() and int(userInput) > 4 and int(userInput) < 129:
        
        afterChoiceList = []
        status1 = True 
        status2 = True
        status3 = True
        status4 = True

        while status1:
            include_lower_case_letters = input('Do you want to include lower case letters in your password? Y/N \n')
            if include_lower_case_letters == 'y' or include_lower_case_letters == 'Y':
                for x in lower_case_letters:
                    afterChoiceList.append(x)
                status1 = False
                print('')
            elif include_lower_case_letters == 'n' or include_lower_case_letters == 'N':
                status1 = False
                print('')
            else:
                print('')
                print('WRONG INPUT \n')

        while status2:
            include_upper_case_letters = input('Do you want to include upper case letters in your password? Y/N \n')
            if include_upper_case_letters == 'y' or include_upper_case_letters == 'Y':
                for x in upper_case_letters:
                    afterChoiceList.append(x)
                status2 = False
                print('')
            elif include_upper_case_letters == 'n' or include_upper_case_letters == 'N':
                status2 = False
                print('')
            else:
                print('')
                print('WRONG INPUT \n')

        while status3:
            include_numbers = input('Do you want to include numbers in your password? Y/N? \n')
            if include_numbers == 'y' or include_numbers == 'Y':
                for x in numbers:
                    afterChoiceList.append(x)
                status3 = False
                print('')
            elif include_numbers == 'n' or include_numbers == 'N':
                status3 = False
                print('')
            else:
                print('')
                print('WRONG INPUT \n')

        while status4:
            include_punctual_marks = input('Do you want to include punctual marks in your password? Y/N? \n')
            if include_punctual_marks == 'y' or include_punctual_marks == 'Y':
                for x in punctual_marks:
                    afterChoiceList.append(x)
                status4 = False
                print('')
            elif include_punctual_marks == 'n' or include_punctual_marks == 'N':
                status4 = False
                print('')
            else:
                print('')
                print('WRONG INPUT \n')

        random.shuffle(afterChoiceList)

        if afterChoiceList:
            password = []
            for x in range(0,int(userInput)):
                y = random.randint(0,len(afterChoiceList)-1)
                password.append(afterChoiceList[y])
            random.shuffle(password)
            password = ''.join([str(elem) for elem in password])
            print('')
            print('Your new password = ' + password)
            print('')
        else:
            print('Character types must be included.')
        
    #CHOICE OF EXIT
    elif userInput == '':
        exit()
    #WRONG INPUT
    else:
        print('')
        print('Please fill in a valid input.\n')

