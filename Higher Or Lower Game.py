import tkinter as tk
import random

class HigherLowerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Higher or Lower Game")
        self.root.geometry("600x400")
        self.root.configure(bg="#333333")

        self.current_number = random.randint(1, 100)
        self.players = []
        self.scores = {}
        self.current_player_index = 0
        self.rounds_played = 0

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.clear_window()

        self.welcome_label = tk.Label(self.root, text="Welcome to Higher or Lower!", font=("Arial", 24), bg="#333333", fg="white")
        self.welcome_label.pack(pady=20)

        self.player1_label = tk.Label(self.root, text="Player 1 Name:", font=("Arial", 18), bg="#333333", fg="white")
        self.player1_label.pack(pady=5)
        self.player1_entry = tk.Entry(self.root, font=("Arial", 18))
        self.player1_entry.pack(pady=5)

        self.player2_label = tk.Label(self.root, text="Player 2 Name:", font=("Arial", 18), bg="#333333", fg="white")
        self.player2_label.pack(pady=5)
        self.player2_entry = tk.Entry(self.root, font=("Arial", 18))
        self.player2_entry.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game, font=("Arial", 18), bg="#4CAF50", fg="white")
        self.start_button.pack(pady=20)

    def start_game(self):
        player1_name = self.player1_entry.get()
        player2_name = self.player2_entry.get()
        if player1_name and player2_name:
            self.players = [player1_name, player2_name]
            self.scores = {player1_name: 0, player2_name: 0}
            self.current_player_index = 0
            self.rounds_played = 0
            self.current_number = random.randint(1, 100)
            self.create_game_screen()

    def create_game_screen(self):
        self.clear_window()

        self.info_label = tk.Label(self.root, text="", font=("Arial", 18), bg="#333333", fg="white")
        self.info_label.pack(pady=20)

        self.number_label = tk.Label(self.root, text=str(self.current_number), font=("Arial", 24), bg="#333333", fg="white")
        self.number_label.pack(pady=20)

        self.higher_button = tk.Button(self.root, text="Higher", command=self.guess_higher, font=("Arial", 18), bg="#2196F3", fg="white")
        self.higher_button.pack(side="left", padx=20, pady=10, expand=True)

        self.lower_button = tk.Button(self.root, text="Lower", command=self.guess_lower, font=("Arial", 18), bg="#F44336", fg="white")
        self.lower_button.pack(side="right", padx=20, pady=10, expand=True)

        self.score_label = tk.Label(self.root, text="", font=("Arial", 18), bg="#333333", fg="white")
        self.score_label.pack(pady=20)

        self.round_label = tk.Label(self.root, text="", font=("Arial", 18), bg="#333333", fg="white")
        self.round_label.pack(pady=20)

        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.create_welcome_screen, font=("Arial", 18), bg="#FF9800", fg="white")
        self.reset_button.pack(pady=20)

        self.update_ui()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def update_ui(self):
        self.info_label.config(text=f"{self.players[self.current_player_index]}'s turn")
        self.number_label.config(text=str(self.current_number))
        self.score_label.config(text=f"Scores: {self.scores}")
        self.round_label.config(text=f"Rounds Played: {self.rounds_played}")

    def guess_higher(self):
        next_number = random.randint(1, 100)
        if next_number > self.current_number:
            self.scores[self.players[self.current_player_index]] += 1
            result = "correct"
        else:
            result = "wrong"
        self.current_number = next_number
        self.rounds_played += 1
        self.switch_turn(result)

    def guess_lower(self):
        next_number = random.randint(1, 100)
        if next_number < self.current_number:
            self.scores[self.players[self.current_player_index]] += 1
            result = "correct"
        else:
            result = "wrong"
        self.current_number = next_number
        self.rounds_played += 1
        self.switch_turn(result)

    def switch_turn(self, result):
        self.info_label.config(text=f"{self.players[self.current_player_index]}'s guess was {result}!\nNext number is {self.current_number}")
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.update_ui()

if __name__ == "__main__":
    root = tk.Tk()
    app = HigherLowerGame(root)
    root.mainloop()
