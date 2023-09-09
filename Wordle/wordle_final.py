import tkinter as tk
import random
import copy

class WordleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("WORDLE Game")
        self.root.geometry("512x768")  # Larger window size

        self.guesses = 6
        self.words = []
        with open("words2.txt", "r") as f:
            self.words = [line.strip().lower() for line in f]

        self.word2 = random.choice(self.words)
        self.word = list(self.word2)

        self.previous_attempts = []
        self.attempts=[]
        self.create_ui()

    

    def create_ui(self):
        self.rules_button = tk.Button(self.root, text="Rules", command=self.show_rules)
        self.rules_button.pack(pady=10)

        self.guess_entry = tk.Entry(self.root, width=20)
        self.guess_entry.pack(pady=5)

        self.attempt_button = tk.Button(self.root, text="Attempt WORDLE", command=self.attempt_wordle)
        self.attempt_button.pack(pady=5)

        self.give_up_button = tk.Button(self.root, text="Give Up", command=self.give_up)
        self.give_up_button.pack(pady=5)

        self.guesses_label = tk.Label(self.root, text="Guesses left: {}".format(self.guesses))
        self.guesses_label.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", fg="black")
        self.result_label.pack(pady=10)

        self.boxes_frame = tk.Frame(self.root)
        self.boxes_frame.pack(pady=10)
        self.char_boxes = []

        self.close_button = tk.Button(self.root, text="Close", command=self.root.destroy)
        self.close_button.pack(pady=10)

        self.new_button = tk.Button(self.root, text="New Game", command=newgame)
        self.new_button.pack(pady=10)

    def show_rules(self):
        rules_text = (
            "Welcome to WORDLE!!!\n\n"
            "There will be a random 5 letter word selected every time you play!\n"
            "You will get 6 tries to guess this word correctly.\n"
            "If a letter in the word you guess is in the correct word, the alphabet will appear as a yellow box.\n"
            "If the word you guess has an alphabet in the same position as it is in the final word, "
            "it will be displayed as a green box.\n"
            "Good luck!"
        )
        rules_window = tk.Toplevel(self.root)
        rules_window.title("Rules")
        rules_label = tk.Label(rules_window, text=rules_text, padx=10, pady=10)
        rules_label.pack()

    def attempt_wordle(self):
        guess = self.guess_entry.get().lower()
        if not self.is_valid_guess(guess):
            self.show_invalid_guess_warning()
            return

        if self.guesses > 0:
            guess_list = list(guess)
            result = []

            # Count occurrences of each character in the actual word
            word_char_counts = {}
            self.word3 = list(self.word)
            for i in range(5):
                if self.word[i] in word_char_counts:
                    word_char_counts[self.word[i]] += 1
                else:
                    word_char_counts[self.word[i]] = 1

            for i in range(5):
                char = guess_list[i]
                color = None

                # Check for correct placement (green)
                if char == self.word[i]:
                    color = "green"
                    #print(self.word3)
                    #print(char)
                    self.word3.remove(char)
                # Check for correct character but wrong placement (yellow)
                elif char in self.word3:
                    color = "yellow"
                    self.word3.remove(char)
                    
                self.word3 = list(self.word)
                result.append([char, color])
                
            self.attempts.append(guess)
            self.previous_attempts.append(result)
            self.update_boxes()

            self.guesses -= 1
            self.guesses_label.config(text="Guesses left: {}".format(self.guesses))
            
            if all(box[1] == "green" for box in result):
                self.show_congratulations()
            else:
                self.result_label.config(text="Your Guesses:", fg="blue")
                
    def is_valid_guess(self, guess):
        if len(guess)==5 and guess.isalpha():
            if guess not in self.attempts:
                #print(self.attempts)
                if guess in self.words:
                    return True
        

    def show_invalid_guess_warning(self):
        invalid_guess_window = tk.Toplevel(self.root)
        invalid_guess_window.title("Invalid Guess")
        invalid_label = tk.Label(invalid_guess_window, text="Please enter a valid 5-letter alphabetic string.")
        invalid_label.pack(padx=10, pady=10)

    def update_boxes(self):
        for line_frame in self.char_boxes:
            line_frame.destroy()
        self.char_boxes = []

        for attempt in self.previous_attempts:
            line_frame = tk.Frame(self.boxes_frame)
            for char_info in attempt:
                char, color = char_info
                char_box = tk.Label(line_frame, text=char, bg=color, width=4, height=2, font=("Helvetica", 16))
                char_box.pack(side="left")
            line_frame.pack()
            self.char_boxes.append(line_frame)

    def show_congratulations(self):
        congratulations_window = tk.Toplevel(self.root)
        congratulations_window.title("Congratulations!")
        congrats_label = tk.Label(congratulations_window, text="Congratulations! You guessed the word!", padx=10, pady=10)
        congrats_label.pack()

    def give_up(self):
        self.guesses = 0
        correct_word_window = tk.Toplevel(self.root)
        correct_word_window.title("Correct Word")
        correct_word_label = tk.Label(correct_word_window, text=f"The correct word is '{self.word2}'.", padx=10, pady=10)
        correct_word_label.pack()

def newgame():
    global root
    if __name__ == "__main__":
        if root:
            root.destroy()
        root = tk.Tk()
        game = WordleGame(root)
        root.mainloop()           

root = None
newgame()
