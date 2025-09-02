# educational_tool_fixed.py
# darkboss1bd - Educational Toolkit with Hacker Animation

import tkinter as tk
from tkinter import ttk
import webbrowser
import random
import sys

# --- Error Handling: Check if Tkinter is available ---
try:
    import tkinter as tk
except ImportError:
    print("❌ Tkinter is not available. Install Python with Tk support.")
    sys.exit(1)

# Main Application
class EducationalToolkit:
    def __init__(self, root):
        self.root = root
        self.root.title("darkboss1bd - Educational Toolkit")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        # --- Banner ---
        self.create_banner()

        # --- Canvas for Matrix Rain ---
        self.canvas = tk.Canvas(self.root, width=880, height=400, bg="black", highlightthickness=0)
        self.canvas.pack(pady=10)
        self.matrix_rain = MatrixRain(self.canvas)
        self.matrix_rain.animate()

        # --- Info Buttons (Telegram & Website) ---
        self.create_info_links()

        # --- Learning Resources Table ---
        self.create_resources_table()

        # --- Footer ---
        self.create_footer()

    def create_banner(self):
        banner_frame = tk.Frame(self.root, bg="black")
        banner_frame.pack(pady=10)

        tk.Label(
            banner_frame,
            text="🔥 DARKBOSS1BD 🔥",
            font=("Courier", 24, "bold"),
            fg="lime",
            bg="black"
        ).pack()

        tk.Label(
            banner_frame,
            text="Learn Coding Like a Hacker",
            font=("Arial", 12),
            fg="white",
            bg="black"
        ).pack()

    def create_info_links(self):
        info_frame = tk.Frame(self.root, bg="black")
        info_frame.pack(pady=5)

        tk.Label(
            info_frame,
            text="🔗 Connect with Me:",
            fg="white",
            bg="black",
            font=("Arial", 11)
        ).grid(row=0, column=0, padx=5)

        def open_telegram():
            webbrowser.open("https://t.me/darkvaiadmin")

        def open_website():
            webbrowser.open("https://serialkey.top/")

        tk.Button(
            info_frame,
            text="📱 Telegram: @darkvaiadmin",
            fg="cyan",
            bg="black",
            bd=0,
            font=("Arial", 10, "underline"),
            cursor="hand2",
            command=open_telegram,
            activeforeground="yellow"
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            info_frame,
            text="🌐 Website: serialkey.top",
            fg="cyan",
            bg="black",
            bd=0,
            font=("Arial", 10, "underline"),
            cursor="hand2",
            command=open_website,
            activeforeground="yellow"
        ).grid(row=0, column=2, padx=10)

    def create_resources_table(self):
        tree_frame = tk.Frame(self.root)
        tree_frame.pack(pady=10, padx=20, fill="both", expand=False)

        columns = ("Language", "Resource", "Link")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=8)

        self.tree.heading("Language", text="Language")
        self.tree.heading("Resource", text="Resource")
        self.tree.heading("Link", text="🔗 Click to Open")

        self.tree.column("Language", width=150, anchor="center")
        self.tree.column("Resource", width=300, anchor="center")
        self.tree.column("Link", width=300, anchor="center")

        # Add Sample Resources
        self.resources = [
            ("Python", "Python Official Docs", "https://docs.python.org/3/"),
            ("Python", "Real Python", "https://realpython.com/"),
            ("HTML", "MDN HTML Guide", "https://developer.mozilla.org/en-US/docs/Web/HTML"),
            ("CSS", "MDN CSS Guide", "https://developer.mozilla.org/en-US/docs/Web/CSS"),
            ("JavaScript", "MDN JS Guide", "https://developer.mozilla.org/en-US/docs/Web/JavaScript"),
            ("PHP", "PHP Manual", "https://www.php.net/manual/en/"),
            ("Python", "Automate Boring Stuff", "https://automatetheboringstuff.com/"),
            ("Web Dev", "W3Schools", "https://www.w3schools.com/"),
            ("JS", "JavaScript.info", "https://javascript.info/"),
            ("PHP", "PHP The Right Way", "https://phptherightway.com/"),
        ]

        for res in self.resources:
            self.tree.insert("", "end", values=res)

        self.tree.pack()

        # Bind click event
        self.tree.bind("<Button-1>", self.on_link_click)

    def on_link_click(self, event):
        region = self.tree.identify_region(event.x, event.y)
        column = self.tree.identify_column(event.x)
        if region == "cell" and column == "#3":  # Only on Link column
            row_id = self.tree.identify_row(event.y)
            if row_id:
                values = self.tree.item(row_id, "values")
                if values and len(values) > 2:
                    url = values[2]
                    if url.startswith("http"):
                        webbrowser.open(url)

    def create_footer(self):
        footer = tk.Label(
            self.root,
            text="© 2025 darkboss1bd | Stay Curious, Keep Coding! | Your Success is My Code",
            fg="gray",
            bg="black",
            font=("Arial", 9)
        )
        footer.pack(side="bottom", pady=10)

# --- Matrix Rain Effect ---
class MatrixRain:
    def __init__(self, canvas):
        self.canvas = canvas
        self.symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]{}|;:,.<>? "
        self.font_size = 12
        self.columns = 0
        self.drops = []
        self.chars = []
        self.speed = 50
        self.setup_drops()

    def setup_drops(self):
        self.canvas.update_idletasks()
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        self.columns = max(1, width // self.font_size)
        self.drops = [random.randint(-20, 0) for _ in range(self.columns)]
        self.chars = [" " for _ in range(self.columns)]

    def animate(self):
        try:
            self.canvas.delete("matrix")
            width = self.canvas.winfo_width()
            height = self.canvas.winfo_height()
            if width <= 1 or height <= 1:
                self.canvas.after(self.speed, self.animate)
                return

            self.columns = max(1, width // self.font_size)

            # Adjust drops array if window resized
            while len(self.drops) < self.columns:
                self.drops.append(random.randint(-20, 0))
                self.chars.append(" ")
            while len(self.drops) > self.columns:
                self.drops.pop()
                self.chars.pop()

            for i in range(self.columns):
                char = random.choice(self.symbols)
                x = i * self.font_size
                y = (self.drops[i] - 1) * self.font_size
                if 0 <= y < height and 0 <= x < width:
                    self.canvas.create_text(
                        x, y, text=char, fill="green", font=("Courier", self.font_size), tags="matrix", anchor="nw"
                    )
                self.chars[i] = char

                self.drops[i] += 1
                if self.drops[i] * self.font_size > height and random.random() > 0.975:
                    self.drops[i] = 0
            self.canvas.after(self.speed, self.animate)
        except Exception as e:
            print(f"Animation error: {e}")
            self.canvas.after(self.speed, self.animate)  # Keep trying

# --- Main Execution ---
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = EducationalToolkit(root)
        root.mainloop()
    except Exception as e:
        tk.messagebox.showerror("Application Error", f"An error occurred:\n{e}")
        print(f"Error: {e}")
        input("Press Enter to exit...")
