import random
print ('Number Guessing Game')

number = random.randint(1,100)

chances = 0

print('Guess Number Between 1 to 100')
while chances < 20:
    guess = int(input("Guess The Number"))

    if guess == number:
        print("Congratulations You Win!")
        break
        
    elif guess < number:
        print("Your Guess Is Too Low! Try a higher number than", guess)
        break
    else: 
        print("Your Is Too High! Try a lower number than", guess)

    chances += 1

if not chances < 20:
    print("You lost! The Number was -> ", number)