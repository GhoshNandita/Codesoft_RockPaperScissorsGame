import random

class RockPaperScissorsGame:
    choices = ['rock', 'paper', 'scissors']
    
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0

    def get_user_choice(self):
        while True:
            user_input = input("Choose rock, paper, or scissors: ").lower()
            if user_input in self.choices:
                return user_input
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "user"
        else:
            return "computer"

    def update_scores(self, winner):
        if winner == "user":
            self.user_score += 1
        elif winner == "computer":
            self.computer_score += 1

    def display_result(self, user_choice, computer_choice, winner):
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
        else:
            print("Computer wins this round!")

    def display_scores(self):
        print(f"\nScores after {self.rounds_played} round(s):")
        print(f"You: {self.user_score}")
        print(f"Computer: {self.computer_score}\n")

    def play_again(self):
        choice = input("Do you want to play another round? (y/n): ").lower()
        return choice == 'y'

    def play_game(self):
        print("--- Welcome to Rock, Paper, Scissors! ---")
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()

            winner = self.determine_winner(user_choice, computer_choice)
            self.update_scores(winner)
            self.rounds_played += 1

            self.display_result(user_choice, computer_choice, winner)
            self.display_scores()

            if not self.play_again():
                print("\nThank you for playing! Final Scores:")
                self.display_scores()
                break

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play_game()