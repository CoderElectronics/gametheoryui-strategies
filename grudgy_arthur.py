import random

class ImportedStrat(GameStrategy):
    def __init__(self) -> None:
        super().__init__(name="Grudgy Arthur", author="Nobu", description="")

    def next_play(self, player_history: list[GameMove], opponent_history: list[GameMove]) -> GameMove:
        global random
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """
        if len(opponent_history) > 0:
            return GameMove.STEAL if (sum(opponent_history) / len(opponent_history)) < 0.5 else random.choices([GameMove.SHARE, GameMove.STEAL], weights=(2, 1), k=1)[0]
        else:
            return GameMove.SHARE

# This line is required!
userGame = ImportedStrat()
