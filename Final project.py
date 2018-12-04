import json
import sys
import datetime

adminchoice: ["admin", "a", "Admin", "leader", "Leader"]

def login(usr):
    uN = input("Name: ")
    pW = input("Password (If you're new this will be your new password): ")

    if uN in usr.keys():
        if pW == usr[uN]:
            print("Welcome back.")
        else:
            print("Incorrect password.")
            return False
    else:
        print("Hello, you're new here!")
        usr[uN] = pW
    writeUsers(usr)
    introDuc()
    return True


def introDuc():
    print("I will lead you though the system and teach you how to operate me.")
    story = input("But first I'd like to know who you are, tell me a bit about yourself ")
    mood = input("OK, so how do you feel today? ")
    if mood == "sad":
        print("That is not good, I hope I can cheer you up!")
    elif mood == "happy":
        print("That's good!")
    elif mood == "good":
        print("Nice!")
    else:
        print("I don't know what that means but I hope you're doing well!")

    choiceintro = input("Do you want to calculate with numbers, know the date/time or go to admin? ")
    if choiceintro == "admin" or "Admin":
        adminLog()

def adminLog():
    key = input("Password: ")
    if key == "xyleminternetpass":
        print("Permission Granted")
        adminInt()
    else:
        print("Permission Denied")
        adminLog()

def adminInt():
    adminchoice = input("""
Do you want to:
- See usernames
- Change admin key
- Change to default settings
""")
    if adminchoice == "usernames" or "See usernames" or "see usernames" or "Usernames":
        print(users)

def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def writeUsers(usr):
    with open("users.json", "w+") as f:
            json.dump(usr, f)

users = readUsers()
success = login(users)

while not success:
    success = login(users)


    
