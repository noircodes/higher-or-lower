import random
import operator

#define the variable
n = random.sample(range(1,100), 2)
ops = {">": operator.ge, "<": operator.le}
iterator = iter(n)
#Intro of the game
print("Welcome to the game 'Higher or Lower' !")
print("First number is " + str(n[0]) + ". Guess next number, Higher or Lower")
#Game Start
hilo = input("Enter Higher or Lower (>/<): ")
print(n)
result = ops[hilo](next(iterator),next(iterator))
if result == True:
    print("You Win!")
else:
    print("You Lose!")
