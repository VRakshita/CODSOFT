import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=10)

        self.tasks_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=40, height=15, font=("Arial", 12))
        self.tasks_listbox.pack(pady=10)

        add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#00cc66", fg="white", font=("Arial", 12))
        add_button.pack(side=tk.LEFT, padx=5)

        view_button = tk.Button(self.root, text="View Tasks", command=self.view_tasks, bg="#0099cc", fg="white", font=("Arial", 12))
        view_button.pack(side=tk.LEFT, padx=5)

        update_button = tk.Button(self.root, text="Update Task", command=self.update_task, bg="#ff9900", fg="white", font=("Arial", 12))
        update_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, bg="#ff3333", fg="white", font=("Arial", 12))
        delete_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("To-Do List", "No tasks in the list.")
        else:
            tasks_text = "\n".join(self.tasks)
            messagebox.showinfo("To-Do List", f"Tasks in the list:\n{tasks_text}")

    def update_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            selected_task = self.tasks_listbox.get(selected_index)
            updated_task = simpledialog.askstring("Update Task", "Enter updated task:", initialvalue=selected_task)
            if updated_task:
                self.tasks[self.tasks.index(selected_task)] = updated_task
                self.tasks_listbox.delete(selected_index)
                self.tasks_listbox.insert(selected_index, updated_task)

    def delete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            selected_task = self.tasks_listbox.get(selected_index)
            self.tasks_listbox.delete(selected_index)
            self.tasks.remove(selected_task)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
