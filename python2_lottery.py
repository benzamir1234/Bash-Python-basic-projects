# Lottery lab (random lib)
from random import randint
from time import sleep

print("Welcome to the Lottery!\n")
sleep(0.5)
myBudget = input("Enter your budget: ")
sleep(1)
myRounds = int(myBudget) // 3
print("You have " + str(myRounds) + " rounds")
sleep(1)
print("Lets begin!")
myScore = 0
while myRounds > 0:
    print(str(myRounds) + " rounds to go")
    print("Enter your numbers: ")
    numOne = input("Enter the first number: ")
    if int(numOne) > 37:
        print("Must be between 1-37, restarting")
        continue
    numTwo = input("Enter the second number: ")
    if numOne == numTwo:
        print("Numbers must not be repeated! restarting..")
        sleep(1)
        continue
    elif int(numTwo) > 37:
        print("Must be between 1-37, restarting")
        continue
    numThree = input("Enter the third number: ")
    if numThree == numTwo or numThree == numOne:
        print("Numbers must not be repeated! restarting..")
        sleep(1)
        continue
    elif int(numThree) > 37:
        print("Must be between 1-37, restarting")
        continue
    numFour = input("Enter the fourth number: ")
    if numFour == numOne or numFour == numTwo or numFour == numThree:
        print("Numbers must not be repeated! restarting..")
        sleep(1)
        continue
    elif int(numFour) > 37:
        print("Must be between 1-37, restarting")
        continue
    numFive = input("Enter the fifth number: ")
    if numFive == numOne or numFive == numTwo or numFive == numThree or numFive == numFour:
        print("Numbers must not be repeated! restarting..")
        sleep(1)
        continue
    elif int(numFive) > 37:
        print("Must be between 1-37, restarting")
        continue
    numSix = input("Enter the sixth number: ")
    if numSix == numOne or numSix == numTwo or numSix == numThree or numSix == numFour or numSix == numFive:
        print("Numbers must not be repeated! restarting..")
        sleep(1)
        continue
    elif int(numSix) > 37:
        print("Must be between 1-37, restarting")
        continue

    print("Generating the winning numbers", end="")
    randOne = randint(1, 37)
    randTwo = randint(1, 37)
    randThree = randint(1, 37)
    randFour = randint(1, 37)
    randFive = randint(1, 37)
    randSix = randint(1, 37)
    sleep(1)
    print(".", end="")
    sleep(1)
    print(".", end="")
    sleep(1)
    print(".\nDone!")

    print("Number 1 is: " + str(randOne) + " and yours is: " + str(numOne))
    print("Number 2 is: " + str(randTwo) + " and yours is: " + str(numTwo))
    print("Number 3 is: " + str(randThree) + " and yours is: " + str(numThree))
    print("Number 4 is: " + str(randFour) + " and yours is: " + str(numFour))
    print("Number 5 is: " + str(randFive) + " and yours is: " + str(numFive))
    print("Number 6 is: " + str(randSix) + " and yours is: " + str(numSix))
    trueCount = 0
    if int(numOne) == int(randOne) or int(numOne) == int(randTwo) or int(numOne) == int(randThree) or int(numOne) == int(randFour) or int(numOne) == int(randFive) or int(numSix) == int(randSix):
        trueCount += 1
    if int(numTwo) == int(randOne) or int(numTwo) == int(randTwo) or int(numTwo) == int(randThree) or int(numTwo) == int(randFour) or int(numTwo) == int(randFive) or int(numTwo) == int(randSix):
        trueCount += 1
    if int(numThree) == int(randOne) or int(numThree) == int(randTwo) or numThree == int(randThree) or int(numThree) == int(randFour) or int(numThree) == int(randFive) or int(numThree) == int(randSix):
        trueCount += 1
    if int(numFour) == int(randOne) or int(numFour) == int(randTwo) or int(numFour) == int(randThree) or int(numFour) == int(randFour) or int(numFour) == int(randFive) or int(numFour) == int(randSix):
        trueCount += 1
    if int(numFive) == int(randOne) or int(numFive) == int(randTwo) or int(numFive) == int(randThree) or int(numFive) == int(randFour) or int(numFive) == int(randFive) or int(numFive) == int(randSix):
        trueCount += 1
    if int(numSix) == int(randOne) or int(numSix) == int(randTwo) or int(numSix) == int(randThree) or int(numSix) == int(randFour) or int(numSix) == int(randFive) or int(numSix) == int(randSix):
        trueCount += 1
    print("true: " + str(trueCount))
    if trueCount == 0:
        print("0 Maches, Your score so far is: " + str(myScore))
        sleep(2)
    elif trueCount == 1:
        print("1 Maches, Your score so far is: " + str(myScore))
        sleep(2)
    elif trueCount == 2:
        print("2 Maches, Your score so far is: " + str(myScore))
        sleep(2)
    elif trueCount == 3:
        myScore += 10
        print("3 Maches you won 10, Your score so far is: " + str(myScore))
        sleep(2)
    elif trueCount == 4:
        myScore += 100
        print("4 Maches you won 100, Your score so far is: " + str(myScore))
        sleep(2)
    elif trueCount == 5:
        myScore += 5000
        print("5 Maches you won 5000, Your score so far is: " + str(myScore))
        sleep(2)
    elif trueCount == 6:
        myScore += 1000000
        print("6 Maches!! you won 1mil, Your score so far is: " + str(myScore))
        sleep(2)
    myRounds -= 1


    continue

print("You have no Rounds left.. Your prize is: " + str(myScore) + " Bye.")
