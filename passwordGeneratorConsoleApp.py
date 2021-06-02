import random

status = False
lower_case_randomlist =     []
upper_case_randomlist =     []
numers_randomlist =         []
punctual_marks_randomlist = []

lower_case_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers =            ['1','2','3','4','5','6','7','8','9']
punctual_marks =     ['!','@','#','$','%','^','&','*','(',')']

while not status:
    print("Type either 8, 12, or 16 to choose a password length: ")
    print("To exit press Enter")
    userInput = input()
    print("")
    #CHOICE OF 8 DIGITS
    if userInput == '8':
        password = []
        for x in range(0,2):
            y = random.randint(0,25)
            password.append(lower_case_letters[y])
        for x in range(0,2):
            y = random.randint(0,25)
            password.append(upper_case_letters[y])
        for x in range(0,2):
            y = random.randint(1,9)
            password.append(y)
        for x in range(0,2):
            y = random.randint(0,9)
            password.append(punctual_marks[y])
        random.shuffle(password)
        password = ''.join([str(elem) for elem in password])
        print("Your new password = " + password)
        print("")
    #CHOICE OF 12 DIGITS
    if userInput == '12':
        password = []
        for x in range(0,3):
            y = random.randint(0,25)
            password.append(lower_case_letters[y])
        for x in range(0,3):
            y = random.randint(0,25)
            password.append(upper_case_letters[y])
        for x in range(0,3):
            y = random.randint(1,9)
            password.append(y)
        for x in range(0,3):
            y = random.randint(0,9)
            password.append(punctual_marks[y])
        random.shuffle(password)
        password = ''.join([str(elem) for elem in password])
        print("Your new password = " + password)
        print("")
    #CHOICE OF 16 DIGITS
    if userInput == '16':
        password = []
        for x in range(0,4):
            y = random.randint(0,25)
            password.append(lower_case_letters[y])
        for x in range(0,4):
            y = random.randint(0,25)
            password.append(upper_case_letters[y])
        for x in range(0,4):
            y = random.randint(1,9)
            password.append(y)
        for x in range(0,4):
            y = random.randint(0,9)
            password.append(punctual_marks[y])
        random.shuffle(password)
        password = ''.join([str(elem) for elem in password])
        print("Your new password = " + password)
        print("")
    if userInput == '':
        exit()
    else:
        print("Please fill in a valid input.")