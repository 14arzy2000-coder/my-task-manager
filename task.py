import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("task meneger")
root.geometry("500x500")
root.config(bg="grey")

tasks = []

page_show = tk.Frame(root) # страница с меню
page_retur_menu = tk.Frame(root) # страница с действиями задачи

menu = tk.Label(page_show, text="меню задач", bg="lightblue", font=("Arial", 20)).pack()

tk.Button(page_show, text="показать задачи").pack()
tk.Button(page_show, text="добавить задачи").pack()
tk.Button(page_show, text="редактировать задачи").pack()
tk.Button(page_show, text="удалить задачи").pack()

def show_collection():
    page_show.pack_forget()
    page_retur_menu.pack(fill="both", expand=True)


# entry = tk.Entry(root, width=50, bg="white", fg="black")
# entry.pack()

# def add_task(event=None):
#     text = entry.get()
#     if text != "":
#         tasks.append(text)
#         entry.delete(0, "end")
#         messagebox.showinfo("готово", "задача добавлена")

# entry.bind("<Return>", add_task)

page_show.pack()
root.mainloop()
