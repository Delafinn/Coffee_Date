import time # used to slow down dialogue
import sys # used for quitting

while True: # Main loop



    name1 = input("what is your name? to exit the program type quit at any time") # asking the user their name
    if name1 == "neo" :
        print("Mr.Anderson.")
    if name1 == "dude" :
        print("sah dude!")
    if name1 == ("quit"):
        sys.exit("quitting program") # quitting
    else :
        print("what a nice name")
    time.sleep(2)

    coffeequestion = input(name1 + " do you like coffee? type either (y)es or (n)o ")

    while (coffeequestion != "yes" and coffeequestion != "y" and coffeequestion != "no" and coffeequestion != "n"): # loop if user doesn't say yes or no.
        coffeequestion = input(name1 + " do you like coffee?")

    if coffeequestion == "yes" or coffeequestion ==  "y":
        print(name1 + " Lets get some coffee.")
        time.sleep(2)
        fq = input("What's your favorite coffee drink?")
        if fq == "americano":
            print("That's my favorite coffee too!")
        if fq == ("quit"):
            sys.exit("quitting program") # quitting
        else:
            print("nice!")

    if coffeequestion == "no" or coffeequestion == "n":
        print(name1 + " I'm gonna grab a coffee. \n   You are more than welcome to join me to the coffee shop")
        time.sleep(3)
        sq = input(name1 + " Are you joining? type either (y)es or (n)o")
        if sq == "no" or sq == "n":
            print("see you soon!")
        if sq == "yes" or sq ==  "y":
            print("sweet!")
        if sq == ("quit"):
            sys.exit("quitting program") # quitting

    if coffeequestion == ("quit"):
        sys.exit("quitting program")  # quitting
