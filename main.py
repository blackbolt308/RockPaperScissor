from random import random
class Game:

    game_actions = {"Rock" : 1, "Paper" : 2, "Scissor" : 3}

    def run(self):

       # print(random(self.game_actions))
        print(self.rule("Scissor", "Paper"))

    def rule(self, player1_action, player2_action):
        result = "None"

        if self.game_actions[player2_action] == 3 and self.game_actions[player1_action] == 1:
            result = "Player 1"
        elif self.game_actions[player2_action] == 1 and self.game_actions[player1_action] == 3:
            result = "Player 2"
        elif self.game_actions[player1_action] < self.game_actions[player2_action]:
            result = "Player 2"
        else:
            result = "Player 1"

        return result




if __name__ == "__main__":
    game = Game()
    game.run()
