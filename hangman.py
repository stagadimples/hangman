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
    incorrect = 0

    def wordChoice(self):
        self.current = self.words[random.randint(0, 12)]
        self.ref = list(self.current)

    def guess(self):
        wordLength = len(self.ref)
        self.blank = list('_' * wordLength)
        while str(self.blank).find('_') != -1:
            self.letter = input('Guess: ')
            if self.letter not in self.ref:
                self.incorrect += 1
            else:
                position = [pos for pos, letter in enumerate(self.ref) if letter == self.letter] 
                self.blank[position[0]] = self.letter
                self.ref[position[0]] = '_'

            print(str(self.blank))

hangman = Hangman()
hangman.wordChoice()
hangman.guess()
