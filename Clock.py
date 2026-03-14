import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

root = tk.Tk()
root.title("Clock")
root.geometry("400x200")
root.configure(bg="#1e1e2e")

clock_label = tk.Label(
    root, 
    font=("Arial", 60, "bold"), 
    bg="#1e1e2e", 
    fg="#89b4fa"
)
clock_label.pack(expand=True)

update_time()
root.mainloop()