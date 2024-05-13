class ImportedStrat(GameStrategy):
    def __init__(self) -> None:
        super().__init__(name="Opposito", author="Nobu", description="Does the opposite move.")

    def next_play(self, player_history: list[GameMove], opponent_history: list[GameMove]) -> GameMove:
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """
        return abs(opponent_history[-1] - 1)


# This line is required!
userGame = ImportedStrat()
