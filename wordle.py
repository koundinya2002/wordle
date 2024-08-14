import random

# sample space for words
words = [
    'word',
    'aback',
    'abase',
    'abate',
    'abbey',
    'abbot',
    'abhor',
    'abide',
    'abode',
    'about',
    'above',
    'abuse',
    'abyss',
    'ached',
    'aches',
    'acids',
    'acorn',
    'acres',
    'acrid',
    'acted',
    'actor',
    'acute',
    'adage',
    'adapt',
    'added',
    'adder',
    'adept',
    'adieu',
    'admit',
    'adobe',
    'adopt',
    'adore',
    'adorn',
    'adult',
    'aegis',
    'aeons',
    'affix',
    'afire',
    'afoot',
    'after',
    'again',
    'agape',
    'agate',
    'agent',
    'agile',
    'aging',
    'aglow',
    'agony',
    'agree',
    'ahead',
    'aided',
    'aides',
    'ailed',
    'aimed',
    'ankle',
    'annex',
    'annoy',
    'annul',
    'antes',
    'antic',
    'anvil',
    'apace',
    'apart',
    'boded',
    'bodes',
    'boggy',
    'bogus',
    'boils',
    'borne',
    'bosom',
    'bough',
    'bound',
    'bouts',
    'bowed',
    'bowel',
    'bower',
    'bowls',
    'boxed',
    'boxer',
    'boxes',
    'brace',
    'brags',
    'braid',
    'brain',
    'brake',
    'brand',
    'brass',
    'brats',
    'brave',
    'bravo',
    'brawl',
    'brawn',
    'bread',
    'break',
    'breed',
    'briar',
    'bribe',
    'brick',
    'bride',
    'brief',
    'brier',
    'brigs',
    'brims',
    'brine',
    'bring',
    'brink',
    'briny',
    'brisk',
    'broad',
    'broil',
    'broke',
    'brood',
    'brook',
    'broom',
    'broth',
    'brown',
    'brows',
    'bruin',
    'brunt',
    'brush',
    'brute',
    'bucks',
    'budge',
    'buggy',
    'bugle',
    'build',
    'built',
    'bulbs',
    'bulge',
    'bulks',
    'bulky',
    'bulls',
    'bully',
    'bumps',
    'bunch',
    'bunks',
    'buoys',
    'burly',
    'burns',
    'burnt',
    'burro',
    'burrs',
]


# choosing a word randomly
choosen_word = random.choice(words)

# for storing the boolean value whilst checking for conditions
answer = None

# counting the no. guesses
count = 0

# for storing letters which are present and not present in the word
incorrect = []
correct = []

# getting the length of the word, for future versions when words aren't just 5 lettered
size = len(choosen_word)

# ui outputs for user understanding
print("Guess the five letter word")
print("You got 5 chances to guess the word")

# printing in development phase for basic understanding
# print("Choosen Word:", choosen_word)

# 5 chances to guess the word, thus looping through 5 times. Need to loop depending on the length of the word
for i in range(5):
    guess = input("Guess here:")
    length = len(guess)

    while (length==size):
        # guessed at 1st chance
        count+=1
        if guess == choosen_word:
            # answer is set to true to break the while loop later on
            answer = True
            print("Congratulations, you've guessed it!")
            print("The word was", guess)
            break
        else:
            print("Incorrect, try again!")
            print("count=", count)
            remaining_chances = 5-count
            if remaining_chances>1:
                print("remaining chances:", remaining_chances)
            else:
                print("Last chance")
            for i in range(5):
                if guess[i] in choosen_word:
                    if guess[i] in correct:
                        pass
                    else:
                        correct.append(guess[i])
                else:
                    if guess[i] in incorrect:
                        pass
                    else:
                        incorrect.append(guess[i])
            print("letters", correct, "is/are present in the word")
            print("letters", incorrect, "is/are not present in the word")
            break
    if answer==True:
        break
    print()
   

print("count:", count)
if count == 1:
    print("Legendary")
elif count == 2:
    print("Epic")
elif count == 3:
    print("Heroic")
elif count == 4:
    print("Adventurer")
elif count == 5 and answer == True:
    print("Novice")
else:
    print("You lost!")
    print("The word was", choosen_word)
    print("Restart the game and try again!")