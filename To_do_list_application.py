import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Description: {self.description}\nDeadline: {self.deadline}\nStatus: {status}"


class ToDoListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List Application")
        self.geometry("400x300")

        self.tasks = []

        self.description_label = tk.Label(self, text="Task Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(self)
        self.description_entry.pack()

        self.deadline_label = tk.Label(self, text="Task Deadline:")
        self.deadline_label.pack()
        self.deadline_entry = tk.Entry(self)
        self.deadline_entry.pack()

        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(self)
        self.task_listbox.pack()

        self.delete_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.mark_completed_button = tk.Button(self, text="Mark as Completed", command=self.mark_task_completed)
        self.mark_completed_button.pack()

        self.display_button = tk.Button(self, text="Display Tasks", command=self.display_tasks)
        self.display_button.pack()

    def add_task(self):
        description = self.description_entry.get()
        deadline = self.deadline_entry.get()
        task = Task(description, deadline)
        self.tasks.append(task)
        self.task_listbox.insert(tk.END, task.description)
        messagebox.showinfo("Task Added", "Task added successfully.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.tasks[task_index]
            self.task_listbox.delete(selected_index)
            messagebox.showinfo("Task Deleted", "Task deleted successfully.")
        else:
            messagebox.showerror("Error", "No task selected.")

    def mark_task_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            task = self.tasks[task_index]
            task.mark_completed()
            self.task_listbox.itemconfig(selected_index, fg="green")
            messagebox.showinfo("Task Completed", "Task marked as completed.")
        else:
            messagebox.showerror("Error", "No task selected.")

    def display_tasks(self):
        messagebox.showinfo("Tasks", "\n\n".join(str(task) for task in self.tasks))

if __name__ == "__main__":
    todo_app = ToDoListApp()
    todo_app.mainloop()
