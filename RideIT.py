import tkinter as tk
from tkinter import messagebox

def bookscreen():
    # Hide the start screen and show the booking screen
    start.pack_forget()
    bookscreen.pack(pady=20)

root = tk.Tk()
root.title("RideIT")

# Start Screen
start = tk.Frame(root)
start.pack(pady=20)

startsec = tk.Label(start, text="Welcome to RideIT", font=("Arial", 25))
startsec.pack(pady=10)

book = tk.Button(start, text="Book", command=bookscreen)
book.pack(pady=20)

root.mainloop()