import tkinter as tk
import random
colors = ['green','red','gray','blue','orange']
random.shuffle(colors)
sirka = 40
dlzka = 300
cas = 60
stop = False
wires = []
win = tk.Tk()
win.title("pyrotechnika")

canvas = tk.Canvas(win, width=800, height=800, bg="beige")
canvas.pack()
for i in range(0,len(colors)):
    wires.append(canvas.create_rectangle(50,250+i*sirka,dlzka+200,250+(i+1)*sirka,fill=colors[i]))
winner = random.choice(wires)
print(winner)

datain = tk.Entry(win, width=20,fg="black",bg="white")
datain.pack()

print(datain.get)
def checker(event):
    global stop
    objekty = canvas.find_overlapping(event.x,event.y,event.x+1,event.y+1)
    print(datain.get())
    if winner in objekty:
        canvas.create_text(400,400,font='Times 80', text='Vyhral si!', fill='green')
        stop = True


hodiny = canvas.create_text(400,600,font='Times 80', text=cas, fill='red')
def timer():
    global cas, stop
    cas = cas - 1
    canvas.itemconfig(hodiny, text=cas)
    if cas > 0 :
        canvas.after(1000,timer)
    else:
        canvas.create_text(400,750,font='Times 80', text='Si mrtvy!', fill='red')
    




canvas.bind("<Button-1>", checker)

canvas.create_text(400,150, font='Times 30', text="Pyrotechink",fill="blue")
canvas.create_text(400,200, font='Times 20', text="označ správny káblik")

timer()

win.mainloop()