import tkinter as tk
from tkinter import messagebox


# Add a task
def add_task():
    task = task_entry.get().strip()

    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")


# Delete selected task
def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")


# Mark task as completed
def complete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task)

        if not task.startswith("✓ "):
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, "✓ " + task)

    except IndexError:
        messagebox.showwarning("Warning", "Please select a task!")


# Clear all tasks
def clear_tasks():
    if task_listbox.size() > 0:
        confirm = messagebox.askyesno(
            "Confirm",
            "Are you sure you want to clear all tasks?"
        )

        if confirm:
            task_listbox.delete(0, tk.END)


# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg="#f2f2f2")


# Title
title_label = tk.Label(
    root,
    text="To-Do List",
    font=("Arial", 24, "bold"),
    bg="#f2f2f2",
    fg="#333333"
)
title_label.pack(pady=20)


# Entry frame
entry_frame = tk.Frame(root, bg="#f2f2f2")
entry_frame.pack(pady=10)


task_entry = tk.Entry(
    entry_frame,
    width=30,
    font=("Arial", 14)
)
task_entry.pack(side=tk.LEFT, padx=5)


add_button = tk.Button(
    entry_frame,
    text="Add",
    width=8,
    command=add_task
)
add_button.pack(side=tk.LEFT)


# Task list
task_listbox = tk.Listbox(
    root,
    width=45,
    height=15,
    font=("Arial", 13),
    selectmode=tk.SINGLE
)
task_listbox.pack(pady=15)


# Buttons
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=10)


complete_button = tk.Button(
    button_frame,
    text="Complete",
    width=12,
    command=complete_task
)
complete_button.grid(row=0, column=0, padx=5)


delete_button = tk.Button(
    button_frame,
    text="Delete",
    width=12,
    command=delete_task
)
delete_button.grid(row=0, column=1, padx=5)


clear_button = tk.Button(
    button_frame,
    text="Clear All",
    width=12,
    command=clear_tasks
)
clear_button.grid(row=0, column=2, padx=5)


# Press Enter to add a task
task_entry.bind("<Return>", lambda event: add_task())


# Start application
root.mainloop()