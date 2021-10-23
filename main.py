import random

#define the variable
n = random.sample(range(0,100), 5)



#Intro of the game
print("Welcome to the game 'Higher or Lower' !")

#Game Start
def begin():
    print("First number is " + str(n[0]) + ". Guess next number, Higher or Lower")
    hilo = input("Enter Higher or Lower (>/<): ")
    y = n[+1]
    result = str(y) + hilo + str(n)
    
begin()
if  result == True:
    begin()
else:
    print("You Lose!")
