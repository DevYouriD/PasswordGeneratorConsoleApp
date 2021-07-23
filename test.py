import random

userInput = input()

# def collectChoices():
lower_case_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers =            ['0','1','2','3','4','5','6','7','8','9']
punctual_marks =     ['!','@','#','$','%','^','&','*']

include_lower_case_letters = input("Do you want to include lower case letters in your password? Y/N ")
include_upper_case_letters = input("Do you want to include upper case letters in your password? Y/N ")
include_numbers =            input("Do you want to include numbers case letters in your password? Y/N? ")
include_punctual_marks =     input("Do you want to include punctual marks in your password? Y/N? ")

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

# for x in range(0,2):
#     collectChoices()

password = []
for x in range(0,int(userInput)):
    password.append[afterChoiceList(x)]
print(password)
password = ''.join([str(elem) for elem in password])
print("Your new password = " + password)

    # #CHOICE OF 8 DIGITS
    # if userInput == '8':
    #     password = []
    #     for x in range(0,2):
    #         y = random.randint(0,25)
    #         password.append(lower_case_letters[y])
    #     for x in range(0,2):
    #         y = random.randint(0,25)
    #         password.append(upper_case_letters[y])
    #     for x in range(0,2):
    #         y = random.randint(0,9)
    #         password.append(y)
    #     for x in range(0,2):
    #         y = random.randint(0,7)
    #         password.append(punctual_marks[y])
    #     random.shuffle(password)
    #     password = ''.join([str(elem) for elem in password])
    #     print("Your new password = " + password)
    #     print("")
    # #CHOICE OF 12 DIGITS
    # elif userInput == '12':
    #     password = []
    #     for x in range(0,3):
    #         y = random.randint(0,25)
    #         password.append(lower_case_letters[y])
    #     for x in range(0,3):
    #         y = random.randint(0,25)
    #         password.append(upper_case_letters[y])
    #     for x in range(0,3):
    #         y = random.randint(0,9)
    #         password.append(y)
    #     for x in range(0,3):
    #         y = random.randint(0,7)
    #         password.append(punctual_marks[y])
    #     random.shuffle(password)
    #     password = ''.join([str(elem) for elem in password])
    #     print("Your new password = " + password)
    #     print("")
    # #CHOICE OF 16 DIGITS
    # elif userInput == '16':
        # password = []
        # for x in range(0,4):
        #     y = random.randint(0,25)
        #     password.append(lower_case_letters[y])
        # for x in range(0,4):
        #     y = random.randint(0,25)
        #     password.append(upper_case_letters[y])
        # for x in range(0,4):
        #     y = random.randint(0,9)
        #     password.append(y)
        # for x in range(0,4):
        #     y = random.randint(0,7)
        #     password.append(punctual_marks[y])
        # random.shuffle(password)
        # password = ''.join([str(elem) for elem in password])
        # print("Your new password = " + password)
        # print("")