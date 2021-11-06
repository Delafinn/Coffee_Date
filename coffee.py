import time

name1 = input("what is your name?") # asking the user their name
print("what a nice name")
time.sleep(1)

coffeequestion = input(name1 + " do you like coffee?")

if coffeequestion == " yes"  :
    print(name1 + " lets get some coffee.")
    time.sleep(2)

elif coffeequestion == " no" :
    print(name1 + " I'm gonna grab a coffee. \n   You are more than welcome to join me to the coffee shop")
    time.sleep(3)
    secondquestion = input(name1 + " are you coming?")


else:
    print(name1 + " I'm gonna grab a coffee. \n   You are more than welcome to join me to the coffee shop")
    time.sleep(3)
    secondquestion = input(name1 + " are you coming?")
