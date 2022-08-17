### Lab
print("Welcome to the campaign program.\n")
myBudget = input("Enter your budget: ")

camFacebook = 100
camInstagram = 50

camFacebookTime = input("Enter how long do you want the Facebook campaign to run (in days): ")
camInstagramTime = input("Enter how long do you want the instagram campaign to run (in days): ")

camCost = (int(camFacebookTime) * int(camFacebook)) + (int(camInstagramTime) * int(camInstagram))
camCostVAT = int(camCost) + (int(camCost)*17/100)
print("The total price for the campaign is:" + str(camCost))
print("The total price for the campaign including tax is:" + str(camCostVAT))
if(int(myBudget) >= int(camCostVAT)):
    print("Successful")
else:
    print("Not enough money.\n")
    toadd = int(camCostVAT) - int(myBudget)
    print("Need to add: " + str(toadd) + "ILS")