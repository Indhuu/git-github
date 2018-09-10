# guess the number game
import random
name = input('Hello! what is your name?')
print ('well,' + name + ', I am thinking of a number between 1 and 20')
secretnumber = random.randint(1,20)
wrongguess = []
for guessestaken in range(1,7):
    print ('Take a guess.')
    guess = int(input())
    if guess< secretnumber:
        print ('your guess is too low.')
        wrongguess.append(guess)
    elif guess > secretnumber:
        print ('your guess is too high')
        wrongguess.append(guess)
    else:
        break
    
for num in wrongguess:
    print ('Wrong attempted values are ' + str(num))

  
for i in range(0,len(wrongguess)):
    j = i + 1
    print ('wrongguess of attept' +str(j) + 'is: ' + str(wrongguess[i]))

       
if guess == secretnumber:
    print('good job' + name + '! you guessed the number in  ' + str(guessestaken) + 'guesses')
    print('The correct number is '+ str(secretnumber))
else:
    print ('Nope. The number i was thinking was ' + str(secretnumber))






