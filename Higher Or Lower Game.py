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
