"""
Python Text RPG
Bubuka Sharif
"""

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100


# ########## Player Setup
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False


myPlayer = player()


# Title Screen
def title_screen_selections():
    option = input('>').strip()
    if option.lower() == 'play':
        start_game()
    elif option.lower() == 'help':
        help_menu()
    elif option.lower() == 'quit':
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print('Please enter a valid command.')
        title_screen_selections()


def title_screen():
    os.system('cls')
    print('#' * 29)
    print('## Welcome to the Text RPG! ##')
    print('#' * 30)
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    print('        - (c) 2021  -       ')
    print('      - sharifbubuka -     ')
    title_screen_selections()


def help_menu():
    print('#' * 45)
    print('# Welcome to the Help Menu of the Text RPG! #')
    print('#' * 45)
    print('- Use up, down, left, right to move')
    print('- Type your commands to do them')
    print('- Use "look" to inspect something')
    print('- Good luck and have luck!')


# ##### MAP
"""
a1,a2... # PLAYER STARTS AT b2
___________________
|     |     |     |  a4
___________________
|     |     |     |  b4 ...
___________________
|     |     |     |
___________________
|     |     |     |
___________________
"""

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examination'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {
    'a1': False, 'a2': False, 'a3': False, 'a4': False,
    'b1': False, 'b2': False, 'b3': False, 'b4': False,
    'c1': False, 'c2': False, 'c3': False, 'c4': False,
    'd1': False, 'd2': False, 'd3': False, 'd4': False
}

zonemap = {
    'a1': {
        ZONENAME: 'Town Market',
        DESCRIPTION: 'This is the town market.',
        EXAMINATION: 'A lot of people are out today. A chicken vendor is on your right. Everyone is wearing a mask.',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2'
    },
    'a2': {
        ZONENAME: 'Town Entrance',
        DESCRIPTION: 'This is the entrance to the town.',
        EXAMINATION: 'There is a sign post that reads, "Welcome to Tredville town."\n There is a T-junction right '
                     'ahead.',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3'
    },
    'a3': {
        ZONENAME: 'Town Square',
        DESCRIPTION: 'This is the town square.',
        EXAMINATION: 'There is a parade against domestic violence. The roads are filled with people.',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4'
    },
    'a4': {
        ZONENAME: 'Town Hall',
        DESCRIPTION: 'This is the city council hall.',
        EXAMINATION: 'There 2 cars parked outside and the mayor is talking to a lady at the entrance.',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: ''
    },
    'b1': {
        ZONENAME: 'Town Park',
        DESCRIPTION: 'This is the town park.',
        EXAMINATION: 'There are four people, 2 dogs and a car parked under a tree.',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2'
    },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home!',
        EXAMINATION: 'Your home looks the same - nothing has changed.',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3'
    }
}


# ##### GAME INTERACTIVITY
def print_location():
    print('\n' + '#' * (4 + len(myPlayer.location)))
    print(f'# {myPlayer.location.upper()} #')
    print(f'# {zonemap[myPlayer.location][DESCRIPTION]} #')
    print('\n' + '#' * (4 + len(myPlayer.location)))


def prompt():
    print('\n ==============================')
    print('What would you like to do?')
    action = input('>')
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'run', 'quit', 'examine', 'inspect', 'look']
    while action.lower() not in acceptable_actions:
        print('Unknown action, try again.\n')
        action = input()
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk', 'run']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())


def player_move():
    ask = 'Where would you like to move to?\n'
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    if dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    if dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    if dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)


def movement_handler(destination):
    print(f'\n You have moved to the {destination}.')
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print('You have already exhausted tis zone.')
    else:
        print('You can trigger a puzzle here.')


# ##### GAME FUNCTIONALITY
def start_game():
    setup_game()


def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
        # handle if puzzle has been solved, boss defeated, explored everything e.t.c


def setup_game():
    os.system('cls')

    # ##### NAME COLLECTION
    question1 = 'Hello, what\'s your name?\n'
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input('>')
    myPlayer.name = player_name

    # ##### ROLE COLLECTION
    question2_1 = f'Great, so what role do you want to play {myPlayer.name} ?\n'
    question2_2 = 'You can play as a warrior, mage or priest.\n'
    for character in question2_1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2_2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input('>')
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print(F'Well, great choice. You are now a {myPlayer.job}!\n')
    while player_job.lower() not in valid_jobs:
        print(f'{player_job} is not a valid role. Choose from: warrior, mage and priest.')
        player_job = input('>')
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print(f'Finally!! You are now a {myPlayer.job}!\n')

    # ##### PLAYER STATS
    if myPlayer.job == 'warrior':
        myPlayer.hp = 120
        myPlayer.mp = 20
    if myPlayer.job == 'priest':
        myPlayer.hp = 60
        myPlayer.mp = 60
    if myPlayer.job == 'mage':
        myPlayer.hp = 40
        myPlayer.mp = 120

    # ##### INTRODUCTION
    question3 = f'Welcome, {myPlayer.name}, the {myPlayer.job.upper()}.\n'
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speeches = [
        'Welcome to this fantasy world!',
        'I hope it greets you well!\n',
        'Just make sure you don\'t get too lost...',
        'Heheheh...'
    ]

    for speech in speeches:
        for character in speech:
            sys.stdout.write(character)
            sys.stdout.flush()
            if speeches.index(speech) == 0 or speeches.index(speech) == 1:
                time.sleep(0.03)
            elif speeches.index(speech) == 2:
                time.sleep(0.01)
            elif speeches.index(speech) == 3:
                time.sleep(0.02)

    os.system('cls')
    print('\n')
    print('#' * 21)
    print('# Let\'s start now! #')
    print('#' * 21)
    main_game_loop()


title_screen()
