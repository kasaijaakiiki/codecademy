class OmwesoGame:
    def __init__(self):
        # Initialize the board with each player's first row containing 4 seeds and the rest empty
        self.board = [4] * 8 + [0] * 8 + [0] * 8 + [4] * 8
        self.current_player = 1  # Player 1 starts first
        self.rows = 4
        self.cols = 8

    def print_board(self):
        """Display the current state of the board."""
        print("\nCurrent Board:")
        for i in range(self.rows):
            print("Row", i + 1, self.board[i * self.cols:(i + 1) * self.cols])
        print()

    def is_valid_move(self, player, pit_index):
        """Check if the chosen pit belongs to the current player and is not empty."""
        if player == 1 and 0 <= pit_index < 16 and self.board[pit_index] > 0:
            return True
        elif player == 2 and 16 <= pit_index < 32 and self.board[pit_index] > 0:
            return True
        return False

    def sow_seeds(self, pit_index, player):
        """Sow seeds starting from the selected pit in a counterclockwise direction."""
        seeds = self.board[pit_index]
        self.board[pit_index] = 0
        index = pit_index

        while seeds > 0:
            index -= 1  # Move counterclockwise

            # Wrap around correctly for Player 1 (index 0-15) and Player 2 (index 16-31)
            if player == 1:
                # If Player 1 is sowing, once we reach the end of their side (index 0), we wrap to the last pit of Row 2 (index 15)
                if index == -1:
                    index = 15  # End of Row 1, wrap to Row 2
            elif player == 2:
                # If Player 2 is sowing, once we reach the end of their side (index 16), we wrap to the last pit of Row 3 (index 31)
                if index == 15:
                    index = 31  # End of Row 2, wrap to Row 3

            # Place one seed in the current pit
            self.board[index] += 1
            seeds -= 1

        return index

    def capture_seeds(self, last_index, player):
        """Capture seeds if the last seed lands on the opponent's side with exactly 2 or 3 seeds."""
        captures = 0
        if player == 1:
            # Player 1 can only capture from Player 2's side (indices 16-31)
            while 16 <= last_index < 32 and (self.board[last_index] == 2 or self.board[last_index] == 3):
                captures += self.board[last_index]
                self.board[last_index] = 0
                last_index -= 1
        else:
            # Player 2 can only capture from Player 1's side (indices 0-15)
            while 0 <= last_index < 16 and (self.board[last_index] == 2 or self.board[last_index] == 3):
                captures += self.board[last_index]
                self.board[last_index] = 0
                last_index -= 1
        return captures

    def play_turn(self):
        """Handle a single player's turn."""
        self.print_board()
        player = self.current_player

        while True:
            try:
                pit = int(input(f"Player {player}, choose a pit (1-16): ")) - 1
                if player == 2:
                    pit += 16  # Adjust for Player 2's row
                if self.is_valid_move(player, pit):
                    last_index = self.sow_seeds(pit, player)
                    break
                print("Invalid move. Choose a pit with more than one seed.")
            except ValueError:
                print("Please enter a valid number.")

        # Capture seeds if possible
        captured = self.capture_seeds(last_index, player)
        print(f"Player {player} captured {captured} seeds.\n")

        # Switch players
        self.current_player = 2 if self.current_player == 1 else 1

    def is_game_over(self):
        """Check if the game is over when one player's side is empty."""
        player1_side = sum(self.board[0:16])
        player2_side = sum(self.board[16:32])
        return player1_side == 0 or player2_side == 0

    def start_game(self):
        """Start the Omweso game."""
        print("Welcome to Omweso!")
        while not self.is_game_over():
            self.play_turn()

        # Determine the winner
        winner = 1 if sum(self.board[0:16]) > 0 else 2
        print(f"\nGame over! Player {winner} wins!")

# Run the game
if __name__ == "__main__":
    game = OmwesoGame()
    game.start_game()
