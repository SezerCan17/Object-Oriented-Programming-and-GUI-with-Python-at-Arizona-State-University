import tkinter as tk

def draw_bulls_eye(canvas):
    
    radii = [100, 80, 60, 40, 20]
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    
   
    for i in range(len(radii)):
       
        x0 = 150 - radii[i]
        y0 = 150 - radii[i]
        x1 = 150 + radii[i]
        y1 = 150 + radii[i]
        
       
        canvas.create_oval(x0, y0, x1, y1, fill=colors[i])


root = tk.Tk()
root.title("Bull's-eye")
root.geometry("300x300")


canvas = tk.Canvas(root, width=300, height=300, bg='white')
canvas.pack()


draw_bulls_eye(canvas)


root.mainloop()
