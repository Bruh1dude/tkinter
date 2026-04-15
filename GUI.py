import tkinter as tk
win = tk.Tk()
win.title("These damned jews")
pocitadlo = 1

def action():
    global pocitadlo
    print(f"action is coming: {pocitadlo}")
    pocitadlo += 1 
    farba1 = canvas.itemcget(obj2, "fill")
    farba2 = canvas.itemcget(obj3, "fill")
    print(farba1)
    if farba1 == "black":
        canvas.itemconfig(obj2,fill="yellow")
    else:
        canvas.itemconfig(obj2,fill="black")
    if farba2 == "blue":
        canvas.itemconfig(obj3,fill="black")
    else:
        canvas.itemconfig(obj3,fill="blue")


canvas = tk.Canvas(win, width=800, height=800, bg="beige")
canvas.pack() #vytvorene objekty dava pod seba
button = tk.Button(win,text="Click me ",width=50,bg="hotpink", command=action)
button.pack()

obj1 = canvas.create_line(50,50,800,800)
obj2 = canvas.create_rectangle(100,100,500,600, fill="red", outline="blue")
obj3 = canvas.create_oval(400,400,800,700, fill="salmon", outline="blue")
print(obj1,obj2,obj3)
canvas.itemconfig(obj2,fill="black")
canvas.itemconfig(obj3,fill="blue")


win.mainloop()