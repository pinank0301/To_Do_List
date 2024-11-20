import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Task list to hold task data
tasks = []

# Function to add a task
def add_task():
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        tasks.append({"Task": task, "Status": "Pending"})
        update_task_list()
        task_entry.delete(0, tk.END)

# Function to delete a selected task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if not selected_task_index:
        messagebox.showwarning("Warning", "No task selected!")
    else:
        task_index = selected_task_index[0]
        tasks.pop(task_index)
        update_task_list()

# Function to mark a selected task as done
def mark_done():
    selected_task_index = task_listbox.curselection()
    if not selected_task_index:
        messagebox.showwarning("Warning", "No task selected!")
    else:
        task_index = selected_task_index[0]
        tasks[task_index]["Status"] = "Done"
        update_task_list()

# Function to update the task list display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        status = task["Status"]
        display_text = f"{idx + 1}. {task['Task']} ({status})"
        task_listbox.insert(tk.END, display_text)

# GUI Components
frame = tk.Frame(root)
frame.pack(pady=10)

# Entry box for adding tasks
task_entry = tk.Entry(frame, width=30)
task_entry.pack(side=tk.LEFT, padx=5)

# Add Task button
add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Action buttons
button_frame = tk.Frame(root)
button_frame.pack()

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

mark_done_button = tk.Button(button_frame, text="Mark as Done", command=mark_done)
mark_done_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()
