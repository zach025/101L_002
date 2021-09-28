#CS 101 Lab
#Zach Opoka
#Email: zof6b@mail.umkc.edu
#prgram 2, assignment 3
print('Welcome to the Flarsheim Guesser!\n')
play_again = 'Y'
while play_again == 'Y':
    print('please think of a number between and including 1 to 100.\n')

    remain_3 = int(input('What is the remainder when your number is divided by 3?'))
    while remain_3 > 2:
        print('The valued entered must be less than 3')
        remain_3 = int(input('What is the remainder when your number is divided by 3?'))
    while remain_3 < 0:
        print('The value entered must be 0 or greater')
        remain_3 = int(input('What is the remainder when your number is divided by 3?'))

    remain_5 = int(input('What is the remainder when your number is divided by 5?'))
    while remain_5 > 4:
        print('The value entered must be less than 5')
        remain_5 = int(input('What is the remainder when your number is divided by 5?'))
    while remain_5 < 0:
        print('The value entered must be 0 or greater')
        remain_5 = int(input('What is the remainder when your number is divided by 5?'))

    remain_7 = int(input('What is the remainder when your number is divided by 7?'))
    while remain_7 > 6:
        print('The value entered must be less than 7')
        remain_7 = int(input('What is the remainder when your number is divided by 7?'))
    while remain_7 < 0:
        print('The value entered must be 0 or greater')
        remain_7 = int(input('What is the remainder when your number is divided by 7?'))

    for i in range(101):
        if (i % 3 == remain_3 and i % 5 == remain_5 and i % 7 ==remain_7):
            print('your number was',i)
            print('How amazing was that?')
            play_again = input('Do you want to play again? Y to continure, N to quit ==>')
    while (play_again != 'Y' and play_again != 'N'):
        play_again = input('Do you want to play again? Y to continure, N to quit ==>')

        
