import tkinter as tk
from tkinter import messagebox
import time

class DisappearingTextApp:
    def __init__(self, root):
        self.root = root
        self.text = tk.Text(self.root, height=10, width=50)
        self.text.pack(pady=10)
        self.start_button = tk.Button(self.root, text="Start", command=self.start_disappearing_text)
        self.start_button.pack(pady=5)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_disappearing_text, state=tk.DISABLED)
        self.stop_button.pack(pady=5)
        self.save_button = tk.Button(self.root, text="Save", command=self.save_text)
        self.save_button.pack(pady=5)
        self.timer_running = False
        self.last_keypress_time = time.time()
        self.text.bind("<Key>", self.reset_timer)
        self.text.focus_set()  # Set initial focus to the text widget

    def start_disappearing_text(self):
        self.timer_running = True
        self.last_keypress_time = time.time()
        self.check_inactivity()
        self.text.focus_set()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        messagebox.showinfo("Haptic Feedback", "Started! You will be notified if there's no activity for 5 seconds.")
        self.trigger_haptic_feedback()

    def check_inactivity(self):
        if self.timer_running:
            current_time = time.time()
            if current_time - self.last_keypress_time >= 5:
                self.text.delete("1.0", tk.END)
                messagebox.showinfo("Haptic Feedback", "Text has been deleted due to inactivity.")
                self.trigger_haptic_feedback()
            else:
                self.root.after(1000, self.check_inactivity)  # Check every second

    def reset_timer(self, event):
        self.last_keypress_time = time.time()

    def stop_disappearing_text(self):
        self.timer_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        messagebox.showinfo("Haptic Feedback", "Stopped! You can resume writing.")
        self.trigger_haptic_feedback()

    def save_text(self):
        with open("text.txt", "w") as f:
            f.write(self.text.get("1.0", tk.END))
        messagebox.showinfo("Haptic Feedback", "Text saved to file!")
        self.trigger_haptic_feedback()

    def trigger_haptic_feedback(self):
        # Placeholder for haptic feedback, e.g., vibration
        print("Haptic feedback triggered")  # Replace with actual haptic feedback code if available

root = tk.Tk()
root.title("Disappearing Text App")
app = DisappearingTextApp(root)
root.mainloop()
