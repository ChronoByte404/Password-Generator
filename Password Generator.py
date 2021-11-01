# Sanware Password Generator

# Required library

import random

# Program

print("[Sanware] Do you have a favourite pet or animal? If so, what is their name?")
PetName = input("You: ")
print("[Sanware] What's your favourite TV show or movie?")
TVShow = input("You: ")
print("[Sanware] What is your middle name?")
MiddleName = input("You: ")
print("[Sanware] What mobile device do you use?")
MobileDevice = input("You: ")
print("[Sanware] What computer operating system do you use?")
ComputerOS = input("You: ")

print("[Sanware] Stand by, gathering data.")

Collection1 = [PetName[::-1], TVShow[::-1], MiddleName[::-1], MobileDevice[::-1], ComputerOS[::-1]]

Collection2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

Collection3 = ["!", "?"]

print("[Sanware] Data has been gathered. Initiating random selection. Password generation in progress...")

FirstNumber = random.choice(Collection2)
SecondWord = random.choice(Collection1)
ThirdWord = random.choice(Collection2) + FirstNumber
FourthWord = random.choice(Collection1)
SpecialWord = random.choice(Collection3)

Password = (FirstNumber + SecondWord + ThirdWord + SpecialWord)

while " " in Password:
    Password = Password.replace(" ", "")

PasswordTxt = Password

print("[Sanware] Randomisation completed. A secure password has been generated. Saving it to a .txt file now.")

print("")

print("---Password---")

print("")

print(Password)

Password = open(f"Sanware_Passwords.txt", "a")
Password.write(f" | Password Generated: {PasswordTxt} | ")
Password.close()

time.sleep(20)
