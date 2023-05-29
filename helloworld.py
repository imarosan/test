# print("helloworld")
# a = 1
# b = 3

# while b >= a:
#     print("a is smaller than b, a = " + str(a) + " and b is = " + str(b))
#     a+=1
import random
name = input("Name: ")
age = int(input("Age: "))
print("Hello " + name)
if age < 20:
    if (20-age) == 1:
        print("I am " + str(20-age) + " year older than you!")
    else:
        print("I am " + str(20-age) + " years older than you!")
elif age==20:
    print("We are the same age!")
else:
    if (age-20) == 1:
        print("You are " + str(age-20) + " year older than me!") 
    else:
        print("You are " + str(age-20) + " years older than me!") 
print("I will guess your number, think of a number between 1, 100!")
input("When you are ready type anything: ")
number = random.randint(1,100)
guess = ""
guesshigh = 1
guesslow = 100
while guess != ("yes"):
    print("Is your number: " + str(number))
    guess = str.casefold(input("Yes? If not is it higher or lower? "))
    if guess == "higher":
        guesshigh = number
        # number = random.randint(guesshigh+1,guesslow)
        number = ((guesslow-guesshigh))
        if(number%2 == 1):
            number = int(((number+1)/2)+guesshigh)
        else:
            number = int(((number)/2)+guesshigh)
        # print(guesshigh,guesslow)
    if guess == "lower":
        guesslow = number
        # number = random.randint(guesshigh,guesslow-1)
        number = ((guesslow-guesshigh))
        if(number%2 == 1):
            number = int(((number-1)/2)+guesshigh)
        else:
            number = int(((number)/2)+guesshigh)
        # print(guesshigh,guesslow)
    elif guess != ("higher" or "lower"):
        print("Incorrect answer, please answer Yes, Higher or Lower")
print("Hoorray I have guessed your number!")

# print(guesshigh)
# print(number)
