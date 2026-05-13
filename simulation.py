#Game of life (What is this tetopear doing on the calculator)
import tkinter as tk

fr = open('glider-gun.txt','r')
height = int(fr.readline().strip())
width = int(fr.readline().strip())

dish1 = []
dish2 = []

def create_dishes(height,width):
    #idem spravit prazdny dish
    global dish1, dish2
    for i in range(height):
        dish2.append([0]*width)
        dish1.append([0]*width)
    #dish1 = dish2 nefunguje lebo su smerniky    
    x = 0
    y = 0
    #prechadzanie .txt po riadkoch
    for riadok in fr:
        x = 0
        for znak in riadok.strip():
            if znak != "-":
                dish1[y][x] = 1
            x += 1
        y += 1
    return(dish1)

def get_neighbours(dish,y,x):
    susedia = 0

    if x> 0 and y > 0: 
        if dish[y][x+1] == 1:
            susedia +=1
        if dish[y+1][x+1] == 1:
            susedia +=1
        if dish[y+1][x] == 1:
            susedia +=1
        if dish[y][x-1] == 1:
            susedia +=1

    elif x> 0 and y <30:
        if dish[y-1][x] == 1:
            susedia +=1
        if dish[y][x+1] == 1:
            susedia +=1
        if dish[y-1][x+1] == 1:
            susedia += 1
    elif x < 45 and y >0:
        if dish[y][x-1] == 1:
            susedia +=1
        if dish[y][x] == 1:
            susedia += 1
        

    return(susedia)

create_dishes(height,width)
get_neighbours(dish1,2,21)
print(get_neighbours(dish1,21,2))

#win = tk.Tk()
#win.title("Petri dish")

#canvas = tk.Canvas(win, width, height, bg="beige")
#canvas.pack()







#win.mainloop()
