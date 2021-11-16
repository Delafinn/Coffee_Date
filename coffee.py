import time # used to slow down dialogue


name1 = input("what is your name?") # asking the user their name
if name1 == "neo" :
    print("Mr.Anderson.")
if name1 == "dude" :
    print("sah dude!")
else :
    print("what a nice name")
time.sleep(1)

coffeequestion = input(name1 + " do you like coffee?") # making a loop

while (coffeequestion != "yes" and coffeequestion != "no"): # loop if user doesn't say yes or no.
    print(name1 + " I'm gonna grab a coffee. \n   You are more than welcome to join me to the coffee shop.")
    time.sleep(3)
    coffeequestion = input(name1 + " But really do you like coffee?")

if coffeequestion == "yes"  :
    print(name1 + " Lets get some coffee.")
    time.sleep(2)
    fq = input("What's your favorite coffee drink?")


if coffeequestion == "no" :
    print(name1 + " I'm gonna grab a coffee. \n   You are more than welcome to join me to the coffee shop")
    time.sleep(3)
    sq = input(name1 + " Are you joining?")
