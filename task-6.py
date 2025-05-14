from random import randint
import time
from colorama import Fore, Style, init 

# Initialize colorama
init(autoreset=True)

shortest_pass = 6
max_pass = 8
min_ASCII = 33
max_ASCII = 126

def password():
    length = randint(shortest_pass, max_pass)
    res = ''
    for i in range(length):
        res += chr(randint(min_ASCII, max_ASCII))
    return res

choice = 'yes'
chance = 0

# Custom color codes for darker green
DARKER_GREEN = '\033[38;5;28m'  # ANSI code for a darker green

while choice.lower() == "yes":
    if chance == 0:
        print(Fore.LIGHTGREEN_EX + "Here's your password: " + Style.BRIGHT + password())
        choice = input("Do you want to generate a password again? Type 'yes' or 'no': ")
    
    elif chance > 0 and chance < 3:
        print(Fore.GREEN + "Again? " + Style.BRIGHT + "Here's your password: " + Style.BRIGHT + password())
        choice = input("Do you want to generate a password again? Type 'yes' or 'no': ")

    elif chance >= 3:
        print(DARKER_GREEN + "How long should I keep generating the password?!")
        print(DARKER_GREEN + "*sighs*")
        print(Fore.BLACK + "I won't generate one for you now.")  
        time.sleep(5)
        print(DARKER_GREEN + "Oh, you waited?! Fine. I'll generate one now...")
        print(DARKER_GREEN + "Here's your password: " + Style.BRIGHT + password())
        choice = input("Do you want to generate a password again? Type 'yes' or 'no': ")

    chance += 1

print(Fore.CYAN + "Hopefully this password stays in your mind!")
print(Fore.MAGENTA + "Until next time... stay safe, hacker!")
print(Fore.YELLOW + "Bye!")
