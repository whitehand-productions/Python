# I made this program to remind everyone that they are loved! 


import tkinter as tk

index = 0
colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink']


# Main function
def main():
    global canvas, l_oval, r_oval, triangle, root
    root = tk.Tk()
    root.title("Affirmation")
    root.geometry("500x500")
    canvas = tk.Canvas(root, width=500, height=500, bg="yellow")
    canvas.pack()
    # Setting up window & canvas

    l_oval = canvas.create_oval(170, 160, 250, 240, fill="red")
    r_oval = canvas.create_oval(250, 160, 330, 240, fill="red")
    triangle = canvas.create_polygon(170, 200, 330, 200, 250, 350, fill="red")
    # Shapes for heart

    words = canvas.create_text(250, 400, text="I LOVE YOU", font=("Arial", 24))
    change_color()
    root.mainloop()
    # Runs the window

# This function is created for how I'll change the colors of the heart
def change_color():
    global index
    canvas.itemconfig(l_oval, fill=colors[index])
    canvas.itemconfig(r_oval, fill=colors[index])
    canvas.itemconfig(triangle, fill=colors[index])
    # This is used to make changes to the shapes in the heart

    index = (index + 1) % len(colors)
    root.after(500, change_color)
    # Every 500 miliseconds, the color changes
    
# This is used to run my main function
if __name__ == "__main__": 
    main()