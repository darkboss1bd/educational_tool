import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import random

# Main Window
root = tk.Tk()
root.title("darkboss1bd - Educational Toolkit")
root.geometry("900x700")
root.resizable(False, False)
root.configure(bg="black")

# --- Hacker Animation (Matrix Rain) ---
class MatrixRain:
    def __init__(self, canvas):
        self.canvas = canvas
        self.width = canvas.winfo_reqwidth()
        self.height = canvas.winfo_reqheight()
        self.symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.font_size = 10
        self.columns = max(1, int(self.width / self.font_size))
        self.drops = [0] * self.columns
        self.chars = [" "] * self.columns
        self.speed = 30

    def animate(self):
        self.canvas.delete("matrix")
        for i in range(self.columns):
            if self.drops[i] > 0:
                char = random.choice(self.symbols)
                x = i * self.font_size
                y = (self.drops[i] - 1) * self.font_size
                self.canvas.create_text(x, y, text=char, fill="green", font=("Courier", self.font_size), tags="matrix", anchor="nw")
                self.chars[i] = char
            self.drops[i] += 1
            if self.drops[i] * self.font_size > self.height and random.random() > 0.975:
                self.drops[i] = 0
            elif self.drops[i] == 1 and random.random() > 0.9:
                self.drops[i] = 1
        self.canvas.after(self.speed, self.animate)

# --- Banner Frame ---
banner_frame = tk.Frame(root, bg="black")
banner_frame.pack(pady=10)

banner_label = tk.Label(
    banner_frame,
    text="🔥 DARKBOSS1BD 🔥",
    font=("Courier", 24, "bold"),
    fg="lime",
    bg="black"
)
banner_label.pack()

subtitle = tk.Label(
    banner_frame,
    text="Learn Coding Like a Hacker",
    font=("Arial", 12),
    fg="white",
    bg="black"
)
subtitle.pack()

# --- Canvas for Matrix Rain ---
canvas = tk.Canvas(root, width=880, height=500, bg="black", highlightthickness=0)
canvas.pack(pady=10)

matrix = MatrixRain(canvas)
matrix.animate()

# --- Info Frame ---
info_frame = tk.Frame(root, bg="black")
info_frame.pack(pady=10)

# Your Info with Links
def open_telegram():
    webbrowser.open("https://t.me/darkvaiadmin")

def open_website():
    webbrowser.open("https://serialkey.top/")

tk.Label(info_frame, text="🔗 Connect with Me:", fg="white", bg="black", font=("Arial", 12)).grid(row=0, column=0, padx=10)

telegram_btn = tk.Button(
    info_frame,
    text="Telegram: @darkvaiadmin",
    fg="cyan",
    bg="black",
    bd=0,
    font=("Arial", 10, "underline"),
    cursor="hand2",
    command=open_telegram
)
telegram_btn.grid(row=0, column=1, padx=5)

website_btn = tk.Button(
    info_frame,
    text="Website: serialkey.top",
    fg="cyan",
    bg="black",
    bd=0,
    font=("Arial", 10, "underline"),
    cursor="hand2",
    command=open_website
)
website_btn.grid(row=0, column=2, padx=5)

# --- Learning Resources Treeview ---
tree_frame = tk.Frame(root, bg="black")
tree_frame.pack(pady=10)

tree = ttk.Treeview(
    tree_frame,
    columns=("Language", "Resource", "Link"),
    show="headings",
    height=8
)

tree.heading("Language", text="Language")
tree.heading("Resource", text="Resource")
tree.heading("Link", text="Click to Open")

tree.column("Language", width=150, anchor="center")
tree.column("Resource", width=300, anchor="center")
tree.column("Link", width=300, anchor="center")

# Insert Data
resources = [
    ("Python", "Python Official Docs", "https://docs.python.org/3/"),
    ("Python", "Real Python Tutorials", "https://realpython.com/"),
    ("HTML", "MDN Web Docs - HTML", "https://developer.mozilla.org/en-US/docs/Web/HTML"),
    ("CSS", "MDN Web Docs - CSS", "https://developer.mozilla.org/en-US/docs/Web/CSS"),
    ("JavaScript", "MDN Web Docs - JS", "https://developer.mozilla.org/en-US/docs/Web/JavaScript"),
    ("PHP", "PHP Official Manual", "https://www.php.net/manual/en/"),
    ("Python", "Automate the Boring Stuff", "https://automatetheboringstuff.com/"),
    ("Web Dev", "W3Schools", "https://www.w3schools.com/"),
    ("JS", "JavaScript.info", "https://javascript.info/"),
    ("PHP", "PHP The Right Way", "https://phptherightway.com/"),
]

for res in resources:
    tree.insert("", tk.END, values=res)

tree.pack()

# Make links clickable
def on_tree_click(event):
    item = tree.identify_row(event.y)
    column = tree.identify_column(event.x)
    if item and column == "#3":  # Only on "Link" column
        values = tree.item(item, "values")
        if values:
            webbrowser.open(values[2])

tree.bind("<Button-1>", on_tree_click)

# --- Footer ---
footer = tk.Label(
    root,
    text="© 2025 darkboss1bd | Stay Curious, Keep Coding!",
    fg="gray",
    bg="black",
    font=("Arial", 10)
)
footer.pack(pady=10)

# Run the app
root.mainloop()