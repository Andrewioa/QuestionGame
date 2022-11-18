from data import question_data


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class Player:
    def __init__(self, name):
        self.name = name
        self.correct = 0
        self.wrong = 0

    def report(self):
        print(f"You got {self.correct} correct answers and {self.wrong} wrong answers!")


class Game:
    def __init__(self):
        x= 0
        for i in question_data:
            x += 1
        self.questions = x

    def play_game(self):
        name = input("What is your name?")
        player = Player(name)
        next = 0
        while next < self.questions:
            quest = Question(question_data[next]["text"],
                             question_data[next]["answer"])
            ask = input(quest.text).capitalize()
            if ask == quest.answer:
                print('Correct!')
                player.correct += 1
            else:
                print("Wrong!")
                player.wrong += 1

            next += 1
        player.report()
        print(f"Thank you for playing {player.name}!")


game = Game()
game.play_game()
