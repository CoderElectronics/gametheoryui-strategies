class ImportedStrat(GameStrategy):
    def __init__(self) -> None:
        super().__init__(name="STSTSH", author="Nobu", description="")
        self.n = -1

    def next_play(
        self, player_history: list[GameMove], opponent_history: list[GameMove]
    ) -> GameMove:
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """
        self.n += 1
        return GameMove.SHARE if self.n % 3 == 0 else GameMove.STEAL

# This line is required!
userGame = ImportedStrat()
