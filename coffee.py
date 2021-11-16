import time


name1 = input("what is your name?") # asking the user their name
if name1 == "neo" :
    print("Mr.Anderson.")
if name1 == "dude" :
    print("sah dude!")
else :
    print("what a nice name")
time.sleep(1)

coffeequestion = input(name1 + " do you like coffee?") # making a while loop

while (coffeequestion != "yes" and coffeequestion != "no"):
    print(name1 + "I'm gonna grab a coffee. \n   You are more than welcome to join me to the coffee shop.")
    time.sleep(3)
    coffeequestion = input(name1 + " but really do you like coffee?")

if coffeequestion == "yes"  :
    print(name1 + " lets get some coffee. \n  I'm heading to the cofee shop now.")
    time.sleep(2)
    fq = input("what's your favorite drink?")


if coffeequestion == "no" :
    print(name1 + " I'm gonna grab a coffee. \n   You are more than welcome to join me to the coffee shop")
    time.sleep(3)
    sq = input(name1 + " are you joining?")
