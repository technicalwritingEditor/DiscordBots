from random import randint
from BTYPE import cNum

class RPSGame:

    opts = ["rock", "scissors", "paper"]

    def __init__(self, userID, rounds=0, winner=None, comp_wins=0, user_wins=0):
        self.__userID = userID
        self.__round = rounds
        self.__winner = winner
        self.__comp_wins = comp_wins
        self.__user_wins = user_wins

    @property
    def userID(self):
        return self.__userID

    @property
    def round(self):
        return self.__round

    @property
    def winner(self):
        return self.__winner

    @property
    def user_wins(self):
        return self.__user_wins

    @property
    def comp_wins(self):
        return self.__comp_wins

    def __str__(self):
        return str(vars(self))

    __repr__ = __str__

    def status(self, rounds=False):
        return "SNMBot wins: " + str(self.__comp_wins) +\
               "\n<@" + self.__userID + "> wins: " + str(self.__user_wins) +\
               (("\nRounds Completed: " + str(self.__round)) if rounds else "")

    def play_round(self, word):
        if word.lower() in ("", " "):
            return "You have to chose at least one option <@" + self.__userID + ">!\nThe options are: " + str(self.opts) + ".\nTry again!"
        elif word.lower() not in self.opts:
            return "*" + word + "* is not an option <@" + self.__userID + ">!\nThe options are: " + str(self.opts) + ".\nTry again!"
        else:
            comp_pick = cNum(0, 2, randint(0,2))
            user_pick = cNum(0, 2, self.opts.index(word.lower()))
            mes = "I pick " + self.opts[int(comp_pick)] + " <@" + self.__userID + ">!\n"
            if comp_pick - 1 == user_pick:
                self.__user_wins += 1
                mes += "Aww Shucks, I lost!"
            elif comp_pick + 1 == user_pick:
                self.__comp_wins += 1
                mes += "Yes, I win!"
            else:
                mes += "Damn, a tie!"
            if self.__comp_wins == 3:
                self.__winner = "SNMBot"
            elif self.__user_wins == 3:
                self.__winner = "<@" + self.__userID + ">"
            self.__round += 1
            return mes + "\n\nResults after round " + str(self.__round) + ":\n" + self.status()


class User:
    def __init__(self, userID, rps_games=0, rps_wins=0, rps_losses=0, rps_game=None):
        self.__userID = userID
        self.__rps_games = rps_games
        self.__rps_wins = rps_wins
        self.__rps_losses = rps_losses
        self.__rps_game = rps_game

    @property
    def userID(self):
        return self.__userID

    @property
    def rps_games(self):
        return self.__rps_games

    @property
    def rps_wins(self):
        return self.__rps_wins

    @property
    def rps_losses(self):
        return self.__rps_losses

    @property
    def rps_game(self):
        return self.__rps_game

    @property
    def rps_kd(self):
        return self.__rps_wins / (self.__rps_losses if self.__rps_losses != 0 else 1)

    def play_rps(self):
        self.__rps_game = RPSGame(self.__userID)

    def game_over_rps(self):
        if self.__rps_game.winner == self.__userID:
            self.__rps_wins += 1
        else:
            self.__rps_losses += 1
        self.__rps_games += 1
        self.__rps_game = None

    def __str__(self):
        return str(vars(self))

    __repr__ = __str__