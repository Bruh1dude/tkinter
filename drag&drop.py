import tkinter as tk 
win = tk.Tk()
win.title("Drag & Drop")
pos_x = -1
pos_y = -1
def click_it(event):
    global pos_x, pos_y
    print("Clicked",event.x,event.y)
    objekty = canvas.find_overlapping(event.x,event.y,event.x+1,event.y+1)
    print("objekty",objekty)    
    if obj_deez in objekty:
        pos_x = event.x
        pos_y = event.y

def move_it(event):
    global pos_x, pos_y
    #print("pressed & dragged",event.x,event.y)
    if pos_x != -1 and pos_y <= 200:
        vector_x = event.x - pos_x 
        vector_y = event.y - pos_y
        pos_x = event.x
        pos_y = event.y
        canvas.move(obj_deez,vector_x,vector_y)

def end_it(event):
    global pos_x, pos_y
    #print("end",event.x,event.y)
    pos_x = -1
    pos_y = -1

canvas = tk.Canvas(win, width=800, height=800, bg='white')
canvas.pack()
obj_deez = canvas.create_rectangle(0,0,100,100,fill="hotpink",outline="salmon")


canvas.bind("<Button-1>", click_it)
canvas.bind("<B1-Motion>",move_it)
canvas.bind("<ButtonRelease-1>",end_it)

win.mainloop()