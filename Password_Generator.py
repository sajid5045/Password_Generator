import random
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.num_passwords_label = tk.Label(self.frame, text="How many passwords do you want to generate?")
        self.num_passwords_label.grid(row=0, column=0, pady=5)

        self.num_passwords_entry = tk.Entry(self.frame)
        self.num_passwords_entry.grid(row=0, column=1, pady=5)
        self.num_passwords_entry.bind("<KeyRelease>", self.add_length_input)

        self.min_length_label = tk.Label(self.frame, text="Minimum length of password should be 3")
        self.min_length_label.grid(row=1, column=0, columnspan=2, pady=5)

        self.length_labels = []
        self.length_entries = []

        self.generate_button = tk.Button(self.frame, text="Generate Passwords", command=self.generate_passwords)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack(pady=10)

    def add_length_input(self, event=None):
        for widget in self.length_labels + self.length_entries:
            widget.grid_forget()
        self.length_labels = []
        self.length_entries = []

        num_passwords = int(self.num_passwords_entry.get()) if self.num_passwords_entry.get().isdigit() else 0

        for i in range(num_passwords):
            label = tk.Label(self.frame, text=f"Enter the length of Password #{i + 1}:")
            label.grid(row=i + 3, column=0, pady=5)
            self.length_labels.append(label)

            entry = tk.Entry(self.frame)
            entry.grid(row=i + 3, column=1, pady=5)
            self.length_entries.append(entry)

    def generate_passwords(self):
        try:
            num_passwords = int(self.num_passwords_entry.get())
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid number of passwords.")
            return

        password_lengths = []
        for i in range(num_passwords):
            try:
                length = int(self.length_entries[i].get())
            except ValueError:
                length = 3
            if length < 3:
                length = 3
            password_lengths.append(length)

        passwords = self.generate_password(password_lengths)

        self.result_text.delete(1.0, tk.END)
        for i in range(num_passwords):
            self.result_text.insert(tk.END, f"Password #{i + 1} = {passwords[i]}\n")

    def generate_password(self, pwlength):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        passwords = []

        for i in pwlength:
            password = ""
            for j in range(i):
                next_letter_index = random.randrange(len(alphabet))
                password = password + alphabet[next_letter_index]

            password = self.replace_with_number(password)
            password = self.replace_with_uppercase_letter(password)

            passwords.append(password)

        return passwords

    def replace_with_number(self, pword):
        for i in range(random.randrange(1, 3)):
            replace_index = random.randrange(len(pword) // 2)
            pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
        return pword

    def replace_with_uppercase_letter(self, pword):
        for i in range(random.randrange(1, 3)):
            replace_index = random.randrange(len(pword) // 2, len(pword))
            pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
        return pword


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

