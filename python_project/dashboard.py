import tkinter as tk
from tkinter import ttk
import sqlite3

# ==========================
# DATABASE HELPER FUNCTIONS
# ==========================


def get_records_summary():
    """Get simplified records for dashboard history"""
    conn = sqlite3.connect("student_clinic_record.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.student_id, s.name, s.courses, r.date
        FROM medical_records r
        JOIN students s ON r.student_id = s.student_id
        ORDER BY r.date DESC
    """)
    records = cursor.fetchall()
    conn.close()
    return records

# ==========================
# DASHBOARD WINDOW
# ==========================


def open_dashboard(username, open_checkup_form_callback=None, view_records_callback=None):
    dashboard = tk.Tk()
    dashboard.title("EVSU Clinic Dashboard")
    dashboard.geometry("900x650")
    dashboard.configure(bg="#800000")  # EVSU Maroon
    dashboard.resizable(False, False)

    # Center window on screen
    screen_width = dashboard.winfo_screenwidth()
    screen_height = dashboard.winfo_screenheight()
    x = (screen_width // 2) - (900 // 2)
    y = (screen_height // 2) - (650 // 2)
    dashboard.geometry(f"900x650+{x}+{y}")

    # ==========================
    # White center frame
    # ==========================
    center_frame = tk.Frame(dashboard, bg="white", width=850, height=550)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")
    center_frame.grid_propagate(False)

    content = tk.Frame(center_frame, bg="white")
    content.pack(padx=30, pady=30, fill="both", expand=True)

    # Welcome Label
    tk.Label(content, text=f"Welcome, {username}", font=("Arial", 20, "bold"),
             fg="#800000", bg="white").pack(pady=(0, 20))

    # ==========================
    # Create New Record Button
    # ==========================
    btn_new = tk.Button(content, text="Create New Record", font=("Arial", 14, "bold"),
                        bg="#FFCC00", fg="black", width=25, pady=10,
                        command=lambda: open_checkup_form_callback(dashboard) if open_checkup_form_callback else None)
    btn_new.pack(pady=(0, 10))

    # ==========================
    # View Existing Records Button
    # ==========================
    btn_view = tk.Button(content, text="View Existing Records", font=("Arial", 14, "bold"),
                         bg="#FF9900", fg="black", width=25, pady=10,
                         command=lambda: view_records_callback(dashboard) if view_records_callback else None)
    btn_view.pack(pady=(0, 20))

    # ==========================
    # History Red Frame
    # ==========================
    history_frame = tk.Frame(content, bg="#800000", width=800, height=250)
    history_frame.pack(pady=(0, 10))
    history_frame.pack_propagate(False)

    # Columns: Student ID, Name, Course/Section, Date/Time
    columns = ("student_id", "name", "course_section", "date")
    tree = ttk.Treeview(history_frame, columns=columns,
                        show="headings", height=10)
    tree.pack(fill="both", expand=True, padx=5, pady=5)

    # Scrollbar
    scrollbar = ttk.Scrollbar(
        history_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Headings
    tree.heading("student_id", text="Student ID")
    tree.heading("name", text="Name")
    tree.heading("course_section", text="Course / Section")
    tree.heading("date", text="Date / Time")

    # Column widths
    tree.column("student_id", width=100, anchor="center")
    tree.column("name", width=200, anchor="center")
    tree.column("course_section", width=150, anchor="center")
    tree.column("date", width=200, anchor="center")

    # Load records
    def load_history():
        for row in tree.get_children():
            tree.delete(row)
        records = get_records_summary()
        for r in records:
            tree.insert("", "end", values=r)

    load_history()

    dashboard.mainloop()


# Example usage:
# open_dashboard("Admin")
