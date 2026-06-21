import chess

class TerminalChess:
    def __init__(self):
        self.board = chess.Board()

    def display_board(self):
        print("\n    a   b   c   d   e   f   g   h")
        print("  +---+---+---+---+---+---+---+---+")
        
        # python-chess counts 0-63 starting from a1. We flip it to draw top-down (row 8 to 1)
        for row in range(7, -1, -1):
            row_str = f"{row + 1} |"
            for col in range(8):
                square = chess.square(col, row)
                piece = self.board.piece_at(square)
                if piece:
                    # Use professional unicode symbols for pieces
                    row_str += f" {piece.unicode_symbol()} |"
                else:
                    # Draw a light dot for empty spaces to keep alignment clean
                    row_str += " . |"
            print(row_str + f" {row + 1}")
            print("  +---+---+---+---+---+---+---+---+")
        print("    a   b   c   d   e   f   g   h\n")

    def play(self):
        print("=========================================")
        print(" 👑  TERMINAL CHESS ENGINE ACTIVATED  👑 ")
        print("=========================================")
        print("Use standard SAN notation (e.g., e4, Nf3, e7e5).")
        print("Type 'q' to forfeit and exit.")

        while not self.board.is_game_over():
            self.display_board()
            
            # Check whose turn it is
            turn = "White" if self.board.turn == chess.WHITE else "Black"
            move_input = input(f"🤖 {turn}'s move: ").strip()

            if move_input.lower() == 'q':
                print("\n🏳️ Game abandoned. Thanks for playing!")
                return

            try:
                # Try parsing as standard notation or raw square-to-square
                try:
                    move = self.board.parse_san(move_input)
                except ValueError:
                    move = self.board.parse_uci(move_input)

                if move in self.board.legal_moves:
                    self.board.push(move)
                else:
                    print("⚠️ Illegal move! Try looking for an open path.")
            except ValueError:
                print("⚠️ Invalid format! Use notation like 'e4' or 'e2e4'.")

        # Game Over Screen
        self.display_board()
        print("🏁 GAME OVER! 🏁")
        result = self.board.result()
        print(f"Result: {result}")