

class Player():
    def __init__(self):
        super().__init__()

        self.remaining_choices = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
        # self.player_Choice = input('pick')


    def playerPicks(self):

        choice = input("'Pick X or O ")
        self.player_Choice = choice.lower()
        # print(self.player_Choice)

        return self.player_Choice

    def append_player(self, player_Choice, player_space):
        index = self.remaining_choices.index(player_space)
        print(player_Choice)
        print(index)

        self.remaining_choices[index] = player_Choice

        return self.remaining_choices
