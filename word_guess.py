from random import choice
from timeit import default_timer as timer


class WordGuess(object):

    def __init__(self, word_list=[], user=""):
        self.user = user
        self.word_list = word_list
        self.won = 0
        self.lost = 0
        self.score = 0
        self.word_time_dict = {}

    @staticmethod
    def load_word_list(filename):
        with open(filename, "r") as f:
            data = f.readlines()
        return data

    def clean_list(self, data):
        for each in data[:-1]:
            self.word_list.append(each[:-1])
        self.word_list.append(data[-1])

    def play_game(self):
        pick_word = choice(self.word_list)
        guess_word = list(pick_word)
        guess_word_len = len(guess_word)
        turns_allowed = guess_word_len + 3

        answer_list = ["__ "] * guess_word_len
        print(answer_list)

        start_time = timer()
        while turns_allowed:
            user_guess_letter = input("Enter a char:: ")
            if user_guess_letter is None and not user_guess_letter.isalpha():
                turns_allowed = turns_allowed - 1
                continue
            for index, char in enumerate(guess_word):
                if char == user_guess_letter:
                    answer_list[index] = char
                    self.score += 0.5
            print(answer_list)
            if answer_list == guess_word:
                end_time = timer()
                self.word_time_dict[pick_word] = end_time - start_time
                print("## You Won! ##")
                self.score += 2 + turns_allowed
                self.won += 1
                break
            turns_allowed = turns_allowed - 1
        else:
            print("@@ You Lost! @@")
            self.lost += 1
            self.score -= 0.3
        self.word_list.remove(pick_word)

    def play_again(self):
        self.play_game()
        play_more = input("Enter y to play:: ")
        while(play_more.lower()[0:1] == "y" and len(self.word_list) > 0):
            self.play_game()
            play_more = input("Enter y to play:: ")
        if len(self.word_list) == 0:
            print("END OF GAME: All words exhausted")

    def print_statements(self, total_time):
        print(("Hey {} , well played!".format(self.user)))
        print(("You played {} games".format(self.won + self.lost)))
        print(("Games Won = {}".format(self.won)))
        print(("Games lost = {}".format(self.lost)))
        print(("Your final Score = {}".format(self.score)))
        print(("Time Spent on Game = {} seconds".format(total_time)))
        if len(self.word_time_dict) > 0:
            print("Time spend on each correct guess")
            for word, time in self.word_time_dict.items():
                print(("{} : {} seconds").format(word, time))


if __name__ == '__main__':
    data = WordGuess.load_word_list("wordlist.txt")
    game = WordGuess()
    game.clean_list(data)
    name = input("Enter your name:: ")
    game.user = name
    start_time = timer()
    game.play_again()
    end_time = timer()
    game.print_statements(total_time=end_time - start_time)
