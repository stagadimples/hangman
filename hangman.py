import random

class Hangman:
    words = [
        'keyboard',
        'comb',
        'apple',
        'table',
        'house',
        'bulldozer',
        'hat',
        'window',
        'glue',
        'bed',
        'sticker',
        'computer',
        'snake',
    ]
    current = ''
    incorrect = 0
    blank = ''
    ref = []
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    letter = ''
    positionRef = ''

    def wordChoice(self):
        self.current = self.words[random.randint(0, 12)]
        self.ref = list(self.current)


    def guess(self):
        wordLength = len(self.current)
        self.blank = list('_' * wordLength)
        while str(self.blank).find('_') != -1:
            self.letter = input('Guess: ')
            if self.letter not in self.ref:
                self.incorrect += 1
            else:
                position = self.current.find(self.letter)
                self.blank[position] = self.letter
                self.double()
                self.ref[position] = '_'
                self.current.replace(self.letter, '_')

            print(str(self.blank))

hangman = Hangman()
hangman.wordChoice()
hangman.guess()
