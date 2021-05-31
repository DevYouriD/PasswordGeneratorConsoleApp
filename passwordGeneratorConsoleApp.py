import random

password = []

lower_case_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']

random1 = random.randint(0,25)
random2 = random.randint(0,25)
random3 = random.randint(0,25)

password.append(lower_case_letters[random1]), password.append(upper_case_letters[random2]),password.append(numbers[random3])

print(password)
