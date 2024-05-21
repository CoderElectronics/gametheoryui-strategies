from game_class import GameStrategy, GameMove

class SocialCreditStrategy(GameStrategy):
    def __init__(self) -> None:
        super().__init__(name='Social Credit',
                         author='Hunter Baker',
                         description='Tracks arbitrary values to tell how well you can predict their moves')

        self.increment_number = 6
        self.clear_number = 12

        self.is_static = False
        self.is_tit_tat_variant = False

        self.last_tit_tat_move = None

        self.last_deviation = 1

        self.mean_steal_threshold = 0
        import numpy as np

        self.steal_risk_factor = lambda: np.random.uniform(0.0, 0.35)  # 0.2  # 0-1: 0 = always be cautious (STEAL), 1 = always be risky (SHARE)
        self.share_risk_factor = lambda: np.random.uniform(0.1, 0.2)  # 0.2  # 0-1: 0 = always be cautious (SHARE), 1 = always be risky (STEAL)

    def next_play(self, player_history: list[GameMove], opponent_history: list[GameMove]) -> GameMove:
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """
        import numpy as np

        current_move = len(player_history)
        my_history = (np.array([item.value for item in player_history], dtype=np.float64) - 0.5) * 2
        opp_history = (np.array([item.value for item in opponent_history], dtype=np.float64) - 0.5) * 2

        if current_move == self.increment_number:
            # Detect default strategies
            self.is_tit_tat_variant = True
            i = current_move - 1
            while i >= 0:
                i -= 1
                if not my_history[i] == opp_history[i + 1]:
                    self.is_tit_tat_variant = False
                    break
        if current_move == self.increment_number - 1:
            return self.last_tit_tat_move
        elif current_move > self.increment_number:
            if current_move > self.clear_number:
                opp_history = opp_history[self.increment_number-1:]

            mean = np.mean(opp_history)
            deviation = -(np.std(opp_history) - 1)

            if self.is_static:
                if deviation < self.last_deviation:
                    self.is_static = False
                self.last_deviation = deviation
                return GameMove.STEAL

            if mean < self.mean_steal_threshold:
                # Guess they will STEAL
                return GameMove.STEAL if np.abs(mean) * deviation > self.steal_risk_factor() else GameMove.SHARE
            else:
                # Guess they will SHARE
                return GameMove.SHARE if np.abs(mean) * deviation < self.share_risk_factor() else GameMove.STEAL

        else:

            if current_move < 2:
                self.last_tit_tat_move = GameMove.STEAL
            else:
                if current_move > 3:
                    arr = np.array([move.value for move in opponent_history])
                    self.is_static = np.all(arr == arr[0])
                    if self.is_static:
                        static_mode = not bool(np.prod(arr))
                        return GameMove.SHARE if static_mode else GameMove.STEAL
                self.last_tit_tat_move = GameMove.SHARE if opponent_history[-1].value else GameMove.STEAL
            return self.last_tit_tat_move


userGame = SocialCreditStrategy()
