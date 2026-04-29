import tkinter as tk, math, datetime as dt
win = tk.Tk()
win.title('Hodiny')

velkost = 800
s1 = velkost/2
s2 = velkost/2
kratka_ruc = 75   
dlha_ruc = 150
hrubka_h = 3
hrubka_s = 1
canvas = tk.Canvas(win, width=velkost, height=velkost, bg='white')
canvas.pack()

ruckicka_minut = canvas.create_line(s1, s2, s1,  s2 - dlha_ruc, width = hrubka_h, fill= 'black')

canvas.create_oval(240, 240, 560, 560)
def draw(): #na pankaca - mazeme vse
    canvas.delete("all")
    cas = dt.datetime.now()
    #print(cas.hour,cas.minute,cas.second)
    for i in range(1, 13):
        canvas.create_text(s1+170*math.cos(math.radians(i*30-90)),s2+170*math.sin(math.radians(i*30-90)) , font='Times 15 italic bold', text=i)

    uhol_minuta = math.radians(cas.minute * 6 - 90)   
    canvas.create_line(s1, s2, s1+dlha_ruc*math.cos(uhol_minuta),  s2+dlha_ruc*math.sin(uhol_minuta), width = hrubka_h, fill= 'black')
    #print(canvas.coords(ruckicka_minut))
    uhol_sekunda = math.radians(cas.second * 6 - 90)   
    canvas.create_line(s1, s2, s1+dlha_ruc*math.cos(uhol_sekunda),  s2+dlha_ruc*math.sin(uhol_sekunda), width = hrubka_s, fill= 'black')

    uhol_hodina = math.radians(cas.hour * 30 + cas.minute*0.5 - 90)   
    canvas.create_line(s1, s2, s1+kratka_ruc*math.cos(uhol_hodina),  s2+kratka_ruc*math.sin(uhol_hodina), width = hrubka_h, fill= 'black')
    #canvas.itemconfig(ruckicka_minut,)
    canvas.after(1000,draw)

canvas.coords(ruckicka_minut,0,0,100,100)
print(canvas.coords(ruckicka_minut))
draw()
win.mainloop()