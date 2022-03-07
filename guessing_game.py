from multiprocessing import RLock


userInput = input("Choose rock, paper or scissors:").lower()

if userInput == "rock":
    print("You rock")
else:
    print("No you don't")
