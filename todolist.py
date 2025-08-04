import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_list()
    except:
        messagebox.showwarning("Warning", "Select a task to delete")

def update_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# GUI setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")
root.resizable(False, False)

tk.Label(root, text="To-Do List", font=("Arial", 18)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

tk.Button(root, text="Add Task", font=("Arial", 12), command=add_task).pack(pady=5)
tk.Button(root, text="Delete Selected", font=("Arial", 12), command=delete_task).pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 12), width=25, height=10)
listbox.pack(pady=10)

root.mainloop()
