from game_class import GameStrategy


class ImportedStrat(GameStrategy):
    def __init__(self) -> None:
        super().__init__(name="Whatever", author="Shivam", description="it's just whatever.")
        # import numpy as np
        from collections import defaultdict
        self.q_table = defaultdict(lambda: [0, 0])  # Initialize Q-table with zero values
        self.alpha = 0.5  # Learning rate
        self.gamma = 0.9  # Discount factor
        self.epsilon = 0.1  # Exploration rate

    def get_state(self, player_history: list[GameMove], opponent_history: list[GameMove]) -> str:
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: The current state
        """
        # Use the last 10 rounds of both players' history to represent the state
        return str(player_history[-10:]) + str(opponent_history[-10:])

    def next_play(self, player_history: list[GameMove], opponent_history: list[GameMove]) -> GameMove:
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """
        import numpy as np
        # from collections import defaultdict
        state = self.get_state(player_history, opponent_history)
        if np.random.uniform(0, 1) < self.epsilon:
            action = np.random.choice([GameMove.SHARE, GameMove.STEAL])
        else:

            action = np.argmax(self.q_table[state])
        return action

    def update_q_table(self, reward: int, player_history: list[GameMove], opponent_history: list[GameMove]) -> None:
        """
        :param reward: The reward received in the last round
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        """
        old_state = self.get_state(player_history[:-1], opponent_history[:-1])
        new_state = self.get_state(player_history, opponent_history)
        old_value = self.q_table[old_state][player_history[-1]]
        future_values = self.q_table[new_state]
        self.q_table[old_state][player_history[-1]] = old_value + self.alpha * (reward + self.gamma * np.max(future_values) - old_value)

# This line is required!
userGame = ImportedStrat()
