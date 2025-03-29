import tkinter as tk
from tkinter import messagebox
import subprocess

def send_ping():
    site = entry_site.get()
    count = entry_count.get()

    if not site:
        messagebox.showerror("Error", "Please enter a site to ping.")
        return

    if not count.isdigit() or int(count) <= 0:
        messagebox.showerror("Error", "Please enter a valid number of pings.")
        return

    try:
        # Execute the ping command with the specified number of pings
        result = subprocess.run(
            ["ping", "-n", count, "-l", "65535", site],  # '-n' specifies the number of pings
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            messagebox.showinfo("Ping Result", f"Ping successful:\n{result.stdout}")
        else:
            messagebox.showerror("Ping Result", f"Ping failed:\n{result.stderr}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("PingPongDeathTool v.1.0.")

# Create and place widgets
tk.Label(root, text="Enter site to ping:").pack(pady=5)
entry_site = tk.Entry(root, width=30)
entry_site.pack(pady=5)

tk.Label(root, text="Enter number of pings:").pack(pady=5)
entry_count = tk.Entry(root, width=10)
entry_count.pack(pady=5)

ping_button = tk.Button(root, text="Ping", command=send_ping)
ping_button.pack(pady=10)

# Run the application
root.mainloop()