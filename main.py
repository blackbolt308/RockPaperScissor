from random import random, choice
class Game:

    game_actions = {"Rock" : 1, "Paper" : 2, "Scissor" : 3}

    def run(self):

       # print(random(self.game_actions))
        player1 = choice(list(self.game_actions.keys()))
        player2 = choice(list(self.game_actions.keys()))
        print(f"Player 1 action => {player1}; Player 2 action: {player2}")
        winner_result = self.rule(player1, player2)
        if winner_result == "Tie":
            print("Both player actions are same. Hence match is a tie.")
        else:
            print(f"{self.rule(player1, player2)} Wins")

    def rule(self, player1_action, player2_action):
        result = "None"

        if player1_action == player2_action:
            result = "Tie"
        elif self.game_actions[player2_action] == 3 and self.game_actions[player1_action] == 1:
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
