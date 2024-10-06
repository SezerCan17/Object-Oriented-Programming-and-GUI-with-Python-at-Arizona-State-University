import tkinter as tk
import random

class Character:
    def __init__(self, name, health=100, strength=10):
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def hit(self, points):
        self.health -= points
    
    def is_alive(self):
        return self.health > 0

def start_game():
    name1 = entry_name1.get()
    name2 = entry_name2.get()
    
    player1 = Character(name1)
    player2 = Character(name2)
    
    while player1.is_alive() and player2.is_alive():
        player1.hit(player2.attack())
        if player1.is_alive():
            player2.hit(player1.attack())
    
    if player1.is_alive():
        result_label.config(text=f"{player1.name} wins!", fg="green")
    else:
        result_label.config(text=f"{player2.name} wins!", fg="red")

root = tk.Tk()
root.title("2v2 Game")
root.geometry("400x300")
root.config(bg="#2c3e50")

tk.Label(root, text="Player 1 Name:", bg="#2c3e50", fg="white", font=("Arial", 14)).pack(pady=5)
entry_name1 = tk.Entry(root, font=("Arial", 14), bg="white", fg="black")
entry_name1.pack(pady=5)

tk.Label(root, text="Player 2 Name:", bg="#2c3e50", fg="white", font=("Arial", 14)).pack(pady=5)
entry_name2 = tk.Entry(root, font=("Arial", 14), bg="white", fg="black")
entry_name2.pack(pady=5)

start_button = tk.Button(root, text="Start Game", command=start_game, font=("Arial", 14), bg="#3498db", fg="white", padx=10, pady=5)
start_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="#2c3e50", fg="white", font=("Arial", 16))
result_label.pack(pady=20)

root.mainloop()
