# print ("trzynascie".upper())

# print (len("thiscountsletters in a sentence"))

# Guess the number
import random 
  
print("Number guessing game") 
  
# Generating random numbers btween X and Y
number = random.randint(1,50)

# number of chances/inputs given

chances = 0

print("Guess a number between 1 and 50:")

#loop to count the number of chances
while chances < 5:

    # input
    guess =int(input())

    # comparing the numbers
    if guess == number:

        # if number entered is the same as random generated
        print("Congratulation You won!")
        break
    # if guess is too low
    elif guess < number:
        print("Your guess was too low")

    # if too high
    else:
        print("Your guess was too high")

    # increase the value of chance by 1
    chances += 1

# check whether the user guessed the correct number
if not chances < 5:
    print("You lose. The number is:", number)