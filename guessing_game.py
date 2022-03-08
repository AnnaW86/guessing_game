from http.cookiejar import DefaultCookiePolicy
from multiprocessing import RLock


userInput = input("Choose rock, paper or scissors:").lower()
defaultInput = "rock"

if userInput == defaultInput:
    print("Ah, it's a draw")
elif userInput == "paper":
    print("Paper beats rock - you win!")
elif userInput == "scissors":
    print("Aha, rock beats scissors - you lose!")
else:
    print("Well that wasn't one of the options.")
