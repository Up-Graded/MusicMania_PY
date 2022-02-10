import os
import json
import random
import time
from operator import itemgetter

def signup():
    with open('users.json', 'r') as f:
        users = json.load(f)
    usernameInvalid = True
    while usernameInvalid:
        username = input("Enter your username: ")
        if str(username) not in users:
            usernameTaken = False
            for i in range(1, len(users['Users'])):
                if users['Users'][i]['Username'].lower() == username.lower():
                    usernameTaken = True
            if usernameTaken == False:
                time.sleep(1)
                os.system('cls')
                usernameInvalid = False
            else:
                os.system('cls')
                print("That username is already taken.")
                time.sleep(1)
                os.system('cls')
        else:
            os.system('cls')
            print("That username is already taken.")
            time.sleep(1)
            os.system('cls')
    passwordValid = False
    while passwordValid == False:
        password = input("Enter your desired password: ")
        os.system('cls')
        confirmPassword = input("Confirm your password: ")
        if password == confirmPassword:
            passwordValid = True
            os.system('cls')
            print('Successfully signed up.')
            time.sleep(1)
            os.system('cls')
        else:
            print("Passwords don't match.")
            time.sleep(1)
            os.system('cls')
    dict = {}
    dict['Username'] = str(username)
    dict['Password'] = str(password)
    users['Users'].append(dict)
    with open('users.json', 'w') as f:
        json.dump(users, f , indent = 4)
    return username

def login():
    with open('users.json', 'r') as f:
        users = json.load(f)
    usernameValid = False
    while not usernameValid: 
        username = input('Enter your username: ')
        usersLower = users.copy()
        for i in range(0, len(usersLower['Users'])):
            usersLower['Users'][i]['Username'] = usersLower['Users'][i]['Username'].lower()
            if usersLower['Users'][i]['Username'] == username.lower():
                index = i
                usernameValid = True
                os.system('cls')
        if not usernameValid:
            os.system('cls')
            print('Invalid Username.')
            time.sleep(1)
            os.system('cls')
    passwordValid = False
    while not passwordValid:
        password = input('Enter your password: ')
        if password == usersLower['Users'][index]['Password']:
            print('Successfully logged in.')
            passwordValid = True
            time.sleep(1)
            os.system('cls')
        else:
            print('Password not correct.')
            time.sleep(1)
            os.system('cls')
    return username
        
def leader():
    with open("leaderboard.json", "r") as f:
        leader = json.load(f)
    print(leader)

def complete():
    os.system('cls')
    choiceValid = False
    while not choiceValid:
        choice = input('Signup or login: ')
        if choice.lower() == 'signup':
            time.sleep(1)
            os.system('cls')
            username = signup()
            choiceValid = True
        elif choice.lower() == 'login':
            time.sleep(1)
            os.system('cls')
            username = login()
            choiceValid = True
        else:
            print('That is not a valid option.')
            time.sleep(1)
            os.system('cls')
    print('Hello', username)

    choiceValid = False
    while not choiceValid:
        choice = input('What do you want to do (game or lb)?  ')
        if choice.lower() == 'game':
            os.system('cls')
            game(username)
            choiceValid = True
        elif choice.lower() == 'lb':
            os.system('cls')
            leader()
            choiceValid = True
        else:
            print('That is not a valid option.')
            time.sleep(1)
            os.system('cls')

def game(username):
    with open("songs.json", "r") as f:
        songs = json.load(f)
    incomplete = True
    round = 0
    total = 0
    while incomplete:
        os.system('cls')
        round += 1
        score = round(songs, round)
        if score == 3:
            total += 3
        elif score == 1:
            total += 1
        else:
            incomplete = False
    print('You got {} score!'.format(total))
    with open("leaderboard.json", "r") as f:
        leaders = json.load(f)
    if score > leaders["Leaderboard"][5]["Score"]:
        leaders["Leaderboard"][5]["Name"] = username
        leaders["Leaderboars"][5]["Score"] = total
        leaders = sorted(leaders, key = itemgetter("Score"), reverse = True)
    


def gameRound(songs, round):
    attempt = 1
    score = 0
    randomSong = songs['Songs'][random.randint(0, len(songs['Songs'])- 1)]
    lyrics = randomSong['Lyrics']
    author = randomSong['Author']
    title = randomSong['Title']
    lyricsArray = []
    for x in range(len(lyrics)):
        newString = ""
        newString += lyrics[x][0]
        for i in range(len(lyrics[x])-1):
            newString += "_"
        lyricsArray.append(newString)
    lyricsSong = ' '.join(lyricsArray)
    while attempt < 3:
        print("Round: {}\nAttempt:{}\n\nAuthor:{}\nLyrics:\n{}".format(round, attempt, author, lyricsSong))
        guess = input('What do you think the song is called? ')
        if guess.lower() == title.lower():
            if attempt == 1:
                score = 3
                attempt = 4
            elif attempt == 2:
                score = 1
                attempt = 4
        else:
            attempt += 1
            os.system('cls')
            print('Incorrect guess!')
            time.sleep(1)
            os.system('cls')
    return score


complete()
