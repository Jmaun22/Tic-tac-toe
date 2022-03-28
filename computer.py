from Player import Player


# p = Player()
class Computer(Player):

    def __init__(self):
        super().__init__()



    def computer_piece(self, player_Choice):
        if p.player_Choice == 'o':
            print('Computer is X')
            computer_choice = 'x'
            return computer_choice
        else:
            print('Computer is O')
            computer_choice = 'o'
            return computer_choice

    def append_computer(self, computer_choice, computer_space, remaining_choices):
        index = self.remaining_choices.index(computer_space)
        print(computer_choice)
        print(index)

        self.remaining_choices[index] = computer_choice

        return self.remaining_choices
p = Player()
player_pick = p.playerPicks()
