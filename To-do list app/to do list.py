import tkinter as tk
from tkinter import ttk, messagebox

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        messagebox.showinfo('Task Added', f'Task "{task}" added.')

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            messagebox.showinfo('Task Deleted', f'Task "{deleted_task}" deleted.')
        else:
            messagebox.showerror('Error', 'Invalid task index.')

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] = f'[Completed] {self.tasks[task_index]}'
            messagebox.showinfo('Task Completed', f'Task marked as completed: "{self.tasks[task_index]}"')
        else:
            messagebox.showerror('Error', 'Invalid task index.')

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("400x650+400+100")
        self.master.resizable(False, False)

        # Set background color to light blue
        self.master.configure(bg='#add8e6')

        self.style = ttk.Style()
        self.style.configure('Rounded.TButton', borderwidth=2, relief='groove', foreground='black', background='#add8e6')

        self.todo_list = TodoList()

        self.label = tk.Label(self.master, text="Enter Task:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master, width=40)
        self.entry.pack(pady=10)

        self.add_button = ttk.Button(self.master, text="Add Task", command=self.add_task, style='Rounded.TButton')
        self.add_button.pack(pady=5)

        self.delete_button = ttk.Button(self.master, text="Delete Task", command=self.delete_task, style='Rounded.TButton')
        self.delete_button.pack(pady=5)

        self.complete_button = ttk.Button(self.master, text="Mark Completed", command=self.mark_completed, style='Rounded.TButton')
        self.complete_button.pack(pady=5)

        self.list_label = tk.Label(self.master, text="Task List:")
        self.list_label.pack(pady=5)

        self.listbox = tk.Listbox(self.master, width=40, height=15)
        self.listbox.pack()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.todo_list.add_task(task)
            self.update_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning('Warning', 'Please enter a task.')

    def delete_task(self):
        try:
            task_index = int(self.entry.get()) - 1
            self.todo_list.delete_task(task_index)
            self.update_task_list()
            self.entry.delete(0, tk.END)
        except ValueError:
            messagebox.showwarning('Warning', 'Please enter a valid task index.')

    def mark_completed(self):
        try:
            task_index = int(self.entry.get()) - 1
            self.todo_list.mark_completed(task_index)
            self.update_task_list()
            self.entry.delete(0, tk.END)
        except ValueError:
            messagebox.showwarning('Warning', 'Please enter a valid task index.')

    def update_task_list(self):
        self.listbox.delete(0, tk.END)
        for i, task in enumerate(self.todo_list.tasks):
            self.listbox.insert(tk.END, f'{i + 1}. {task}')

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
