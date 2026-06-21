import random

class RockPaperScissors:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.choices = ["rock", "paper", "scissors"]
        
        # Simple text representation of the hands
        self.art = {
            "rock": "    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)",
            "paper": "    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)",
            "scissors": "    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"
        }

    def play(self):
        print("\n=================================")
        print(" 🪨  📄 ✂️  ROCK, PAPER, SCISSORS ✂️  📄 🪨 ")
        print("=================================")
        print("Type 'q' at any time to exit.\n")

        while True:
            print(f"🏆 SCOREBOARD: Player [{self.player_score}] - Computer [{self.computer_score}]")
            player_choice = input("Choose rock, paper, or scissors: ").strip().lower()

            if player_choice == 'q':
                print("\nThanks for playing! Final Score:")
                print(f"Player: {self.player_score} | Computer: {self.computer_score}\n")
                break

            if player_choice not in self.choices:
                print("⚠️ Invalid choice! Please type 'rock', 'paper', or 'scissors'.\n")
                continue

            computer_choice = random.choice(self.choices)

            print("\n--- PLAYER CHOSE ---")
            print(self.art[player_choice])
            print("\n--- COMPUTER CHOSE ---")
            print(self.art[computer_choice])
            print("----------------------\n")

            if player_choice == computer_choice:
                print("🤝 It's a tie!\n")
            elif (player_choice == "rock" and computer_choice == "scissors") or \
                 (player_choice == "paper" and computer_choice == "rock") or \
                 (player_choice == "scissors" and computer_choice == "paper"):
                print("🎉 You win this round!\n")
                self.player_score += 1
            else:
                print("💻 Computer wins this round!\n")
                self.computer_score += 1