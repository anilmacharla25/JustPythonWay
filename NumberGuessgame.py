import random 
name=input("hey! what's your name buddy!")
SecretNumber=random.randint(1,15)
print(f"hey {name} lets play a game, I'm thinking of a number between 1 to 15, can u guess!")
for GuessTaken in range(1,7):
    guess=int(input('enter your guess'))
    if guess>SecretNumber:
        print("Oops!  Its too high")
    elif guess<SecretNumber:
        print("Oops! it is too low")
    else:
        break
if guess==SecretNumber:
    print(f'you guessed it right in {GuessTaken} Guesses')
else:
    print("you've taken more than 6 guesses, Let me reveal the answer --",SecretNumber)


    
