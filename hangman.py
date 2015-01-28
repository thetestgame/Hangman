import string
import urllib2
import random

def isWordGuessed(secretWord, lettersGuessed):
    return all(letter in lettersGuessed for letter in secretWord)

def getGuessedWord(secretWord, lettersGuessed):
    word = ""
    for i in range(0, len(secretWord)):
        character = secretWord[i]
        if (character in lettersGuessed):
            word = word + character
        else :
            word = word + "_ "
    return word

def getAvailableLetters(lettersGuessed):
    letters = string.ascii_lowercase
    available = ""
    for i in range(0, len(letters)):
        character = letters[i]
        if (not(character in lettersGuessed)):
            available = available + character
    return available

def isLetterInWord(secretWord, letter):
    return (letter in secretWord)

def getWordList():
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib2.urlopen(word_site)
    words = response.read()
    return words.splitlines()

def chooseRandomWord():
    words = getWordList();
    return random.choice(words)
    
def runGame(secretWord, mistakes, lettersGuessed):
    possibleGuesses = 8
    remaining = possibleGuesses - mistakes
    print 'You have ' + str(remaining) + ' guesses left.'
    print 'Available letters: ' + getAvailableLetters(lettersGuessed)
    guess = raw_input('Please guess a letter:').lower()
    if (guess in lettersGuessed):
        print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
    elif(isLetterInWord(secretWord, guess)):
        lettersGuessed.append(guess)
        print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
    elif (not(isLetterInWord(secretWord, guess))):
        lettersGuessed.append(guess)
        print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
        mistakes = mistakes + 1
    print '-------------'
    if (not isWordGuessed(secretWord, lettersGuessed) and (remaining-1) > 0):
        runGame(secretWord, mistakes, lettersGuessed)
    else:
        if (isWordGuessed(secretWord, lettersGuessed)):
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'
            
        
def hangman():
    secretWord = chooseRandomWord()
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    print '-------------'
    runGame(secretWord.lower(), 0, [])