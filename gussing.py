import random 
number = random.randint(1,9)
guess = input('Guess the number')
chances = 0

if guess == number:
    print('Well done! You win')
    break

elif guess > number:
    print('It is a bit lower than that!')
    guess = input('Guess the number again.')
    chances = + 1
elif guess< number:
    print('Higher than that sorry!')
    guess = input('Guess the number again.') 
    chances = + 1   

if chances == 5:
    print('You lose! Refresh the game if you would like to try again.')