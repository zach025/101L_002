import random

def play_again() -> bool:
    x = True
    play = input('Do you want to play again?')
    while x == True:
        if play.lower() in ('y','yes'):
            play = True
            x = False
            break
        if play in ('N','NO'):
            play= False
            x = False
        else:
            print('You must enter Y/YES/N/NO to continue. Please try again')
            x = True
            play = input('Do you want to play again?')
    return play
     
def get_wager(bank : int) -> int:
    wager = int(input('How many chips do you want to wager?'))
    while wager <= 0:
        print('The wager amount must be greater than 0. Please enter again.')
        wager = int(input('How many chips do you want to wager?'))
    while wager > bank:
        print('The wager amount can not be greater than how much you have.',bank)
        wager = int(input('How many chips do you want to wager?'))
    return wager            

def get_slot_results() -> tuple:
    reel1 = random.randint(0,10)
    reel2 = random.randint(0,10)
    reel3 = random.randint(0,10)
    return reel1, reel2, reel3

def get_matches(reel1, reel2, reel3) -> int:
    if (reel1 == reel2 and reel2 == reel3):
        matches = 3
    elif (reel1 == reel2 or reel3 == reel2):
        matches = 2
    else:
        matches = 0
    return matches

def get_bank() -> int:
    bank = int(input('How many chips do you want to start with?'))
    while bank <= 0:
        print('Too low a value, you can only choose 1-100 chips')
        bank = int(input('How many chips do you want to start with?'))
    while bank > 100:
        print('Too high a value, you can only choose 1-100 chips')
        bank = int(input('How many chips do you want to start with?'))
    return bank

def get_payout(matches):
    matches = get_matches
    if matches == 3:
        payout = (10 * wager) - wager
    elif matches == 2:
        payout = (wager * 3) - wager
    else:
        payout = -1 * wager
    return payout  


if __name__ == "__main__":

    play = True
    while play == True:

        bank = get_bank()

        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        play = play_again()