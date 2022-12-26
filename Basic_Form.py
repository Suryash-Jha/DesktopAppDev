import tkinter as tk
root= tk.Tk()

def show_entry_fields():
    print("First Name: %s Last Name: %s" % (entry1.get(), entry2.get()))


root.geometry("400x400")
root.title("Basic Form")
frameFirst= tk.Frame(root)
frameFirst.pack()
frameSecond= tk.Frame(root)
frameSecond.pack()

label1 = tk.Label(frameFirst, text='First Name')
label2 = tk.Label(frameSecond, text='Last Name')
entry1 = tk.Entry(frameFirst)
entry2 = tk.Entry(frameSecond)
label1.pack(side=tk.LEFT)
entry1.pack(side=tk.LEFT)
label2.pack(side=tk.LEFT)
entry2.pack(side=tk.LEFT)
btn= tk.Button(root, text='Submit', command=show_entry_fields)
btn.pack(side=tk.BOTTOM)

root.mainloop()
