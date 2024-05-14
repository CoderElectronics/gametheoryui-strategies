import random

class ImportedStrat(GameStrategy):
    def __init__(self) -> None:
        super().__init__(name="Timid Arthur", author="Nobu", description="")

    def next_play(
        self, player_history: list[GameMove], opponent_history: list[GameMove]
    ) -> GameMove:
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """
        global random, reduce

        his = len(opponent_history)
        if his == 0:
            return GameMove.SHARE

        return (
            GameMove.STEAL
            if (sum([i.value for i in opponent_history]) / his) < 0.5
            else random.choices([GameMove.SHARE, GameMove.STEAL], (3, 1))[0]
        )


# This line is required!
userGame = ImportedStrat()
