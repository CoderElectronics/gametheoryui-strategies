class ImportedStrat(GameStrategy):
    def __init__(self) -> None:
        super().__init__(name="yahoo", author="Shivam", description="Adapts based on opponent's recent moves")

    def analyze_opponent(self, opponent_history: list[GameMove]) -> GameMove:
        """
        :param opponent_history: List of the opponent's moves
        :return: The move that the opponent has been making more frequently in the last 10 rounds
        """
        if len(opponent_history) < 10:
            recent_history = opponent_history
        else:
            recent_history = opponent_history[-10:]

        num_shares = recent_history.count(GameMove.SHARE)
        num_steals = recent_history.count(GameMove.STEAL)

        if num_shares > num_steals:
            return GameMove.SHARE
        elif num_steals > num_shares:
            return GameMove.STEAL
        else:
            return GameMove.SHARE

    def next_play(self, player_history: list[GameMove], opponent_history: list[GameMove]) -> GameMove:
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """
        if len(opponent_history) == 0:
            return GameMove.SHARE
        else:
            return self.analyze_opponent(opponent_history)

# This line is required!
userGame = ImportedStrat()
