from game_class import GameStrategy, GameMove

class ImportedStrat(GameStrategy):
    def __init__(self) -> None:
        super().__init__(name="LoseToWin", author="Carly", description="hi")
        self.last_move = GameMove.STEAL

    def next_play(self, player_history: list[GameMove], opponent_history: list[GameMove]) -> GameMove:
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """
        if len(opponent_history) == 0:
            # A. Start with split.
            self.last_move = GameMove.SHARE
        elif len(opponent_history) == 1:
            # B. If opponent’s first choice is a steal, then split.
            # C. If opponent’s first choice is a split, then steal.
            self.last_move = GameMove.SHARE if opponent_history[0] == GameMove.STEAL else GameMove.STEAL
        else:
            # D. Assume chosen action is steal unless following steps happen.
            self.last_move = GameMove.STEAL

            # E. If the opponent SHAREs twice in a row, switch to SHARE.
            if opponent_history[-1] == opponent_history[-2] == GameMove.SHARE:
                self.last_move = GameMove.SHARE

            # E.1 If the opponent steals, go to step F.
            if opponent_history[-1] == GameMove.STEAL:
                # F. If the opponent steals, SHARE once.
                self.last_move = GameMove.SHARE

                # F.1 If the opponent’s following action after stealing is steal, then continue with split until the opponent chooses split.
                if len(opponent_history) > 1 and opponent_history[-2] == GameMove.STEAL:
                    self.last_move = GameMove.SHARE

                # F.2 If the opponent splits again immediately after stealing, go back to step D.
                if len(opponent_history) > 1 and opponent_history[-2] == GameMove.SHARE:
                    self.last_move = GameMove.STEAL

        return self.last_move

# This line is required!
userGame = ImportedStrat()
