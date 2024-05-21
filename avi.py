"""
Always steal game theory strategy for GameTheoryUI.
by: Ari Stehney

Customize the class below with your metadata and fill out the play function
"""

from game_class import GameStrategy, GameMove

class ImportedStrat(GameStrategy):
    def __init__(self) -> None:
        # This is where your metadata will go:
        super().__init__(name="First Impresstion", author="oivi yoidiva", description="hi")

    def next_play(self, player_history: list[GameMove], opponent_history: list[GameMove]) -> GameMove:
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """

        if len(opponent_history) > 0:
            return opponent_history[0]
        else:
            return GameMove.SHARE

# This line is required!
userGame = ImportedStrat()
