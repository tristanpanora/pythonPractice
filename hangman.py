import random
import math

#pick short words only (9 or less chars)

i = random.randint(1,60000) #number of lines in the dictionary (no words that start with z)
count = 0
dict = open('smalldic.txt','r') #opens the file
for line in dict:
        count += 1
        if count == i:
                randomWord = line #iterate through small dictionary and select the random word
                break
dict.close()

#print(randomWord) #selected a random word from the dictionary
#guess = input("Enter guess letter: ") #waiting for guess from user
size = len(randomWord) #size of word
wordArray = []
wrongGuessArray = []

for letter in randomWord:
        wordArray.append(letter)
blanks = []

for i in range(0,size-1):
        blanks.append("_")

for q in range(0,size-1):
        print(blanks[q], end = '')

wrong_guess = 0

print("\nAllowed guesses: ", math.floor(size+(size/2.0))) #allowed guesses will change depending on the size of the word
#                                                               #allowed guesses is the word size + half of the size.


while wrong_guess < math.floor(size+(size/2.0)): #while the number of wrong guesses is below the limit
        print('\n') #print a new line

        guess = str(input("Enter guess letter: ")) #waiting for guess from user

        check_pos = -1 #checking position in the list

        for i in wordArray: #i is a character
                check_pos += 1 #increment the position counter by 1
                
                if i == guess: #check
                        blanks[check_pos] = guess
                elif guess not in wordArray and check_pos == size-1: #IF you have an incorrect guess
                        wrong_guess += 1
                        wrongGuessArray.append(guess) #add the wrong letter to a used letter bank
                        print("Used Letter Bank: ") #print out used letters that were wrong
                        for wrong in range(0,wrong_guess):
                                print(wrongGuessArray[wrong], " ", end = '')
                        print('\n\nWrong guess count: ', wrong_guess) #only prints incorrect guesses if your last guess was wrong
        print("\n")
        for p in range(len(blanks)):
                print(blanks[p], " ", end = '') #print the correct guessed letters on one line

        
        for p in range(len(blanks)):
                if "_" not in blanks and check_pos == size-1: #if no more'_' in blanks, then all the letters have been found
                        wrong_guess = 1000 #break the while loop, set to 1000 (no words are 1000 letters)
        

if wrong_guess == 1000: #will only equal 1000 if the word is correct
         print("\nYOU WIN!\nWord: ")
         print(randomWord)

elif wrong_guess == math.floor(size+(size/2.0)): #if you run out of guesses
        print("\nYOU LOSE!\n\nWord: ") #you lose
        print(randomWord) #reveals the word
        

