import tkinter as tk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
from dashboard import open_dashboard


def check_login():
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect("student_clinic_record.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM staff WHERE username = ? AND password = ?",
                   (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        root.destroy()
        open_dashboard(username)
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")


# ============================
# MAIN WINDOW
# ============================
root = tk.Tk()
root.title("EVSU Student Clinic - Staff Login")
root.geometry("750x500")
root.config(bg="#800000")  # EVSU Maroon

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Fixed window size
window_width = 750
window_height = 500
root.geometry(f"{window_width}x{window_height}")

# Disable resizing
root.resizable(False, False)

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate x and y coordinates for the window to be centered
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the geometry to center the window
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# ============================
# SHADOW FRAME (for smooth card effect)
# ============================
shadow = tk.Frame(root, bg="#5a0000", width=380, height=360)
shadow.place(relx=0.5, rely=0.5, anchor="center")
shadow.grid_propagate(False)

# ============================
# MAIN CARD FRAME (white smooth box)
# ============================
center_frame = tk.Frame(root, bg="white", width=360, height=340)
center_frame.place(relx=0.5, rely=0.5, anchor="center")
center_frame.grid_propagate(False)

# Extra padding using internal frame
content = tk.Frame(center_frame, bg="white")
content.pack(padx=25, pady=30, fill="both")

# ============================
# LOGIN UI
# ============================

# === Load Image ===

logo_img = Image.open("EVSU_Official_Logo.png")
logo_img = logo_img.resize((120, 120))   # Resize image
logo_photo = ImageTk.PhotoImage(logo_img)

# === Logo Label ===
logo_label = tk.Label(content, image=logo_photo, bg="white")
logo_label.image = logo_photo  # Keep reference to avoid garbage collection
logo_label.pack(pady=(0, 10))


title_label = tk.Label(content,
                       text="EVSU Clinic Record",
                       font=("Arial", 18, "bold"),
                       fg="#800000",
                       bg="white")
title_label.pack(pady=10)

# Username
tk.Label(content, text="Username:", bg="white",
         font=("Arial", 12)).pack(pady=(10, 3))
entry_username = tk.Entry(content, font=("Arial", 12), width=28)
entry_username.pack(pady=(0, 10))

# Password
tk.Label(content, text="Password:", bg="white",
         font=("Arial", 12)).pack(pady=(10, 3))
entry_password = tk.Entry(content, font=("Arial", 12), show="*", width=28)
entry_password.pack(pady=(0, 10))

# Login button
login_button = tk.Button(content,
                         text="LOGIN",
                         font=("Arial", 12, "bold"),
                         bg="#FFCC00",
                         fg="black",
                         width=20,
                         pady=6,
                         command=check_login)
login_button.pack(pady=20)

root.mainloop()
