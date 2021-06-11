from tkinter import *
import random

# window dimensions
height = 700
width = 700

# starting point
p_x = random.randint(1, width)
p_y = random.randint(1, height)
p = (p_x, p_y)


def chaos_game(x, y, z):
    window = Tk()
    window.title('Chaos Game')
    canvas = Canvas(window, height=height, width=width)
    speed = 10  # how fast points are added

    # draw starting point and three points of triangle
    canvas.create_oval(x[0], x[1], x[0] + 1, x[1] + 1, fill='#000')
    canvas.create_oval(y[0], y[1], y[0] + 1, y[1] + 1, fill='#000')
    canvas.create_oval(z[0], z[1], z[0] + 1, z[1] + 1, fill='#000')
    canvas.create_oval(p[0], p[1], p[0] + 1, p[1] + 1, fill='#000')

    def add_point():  # chooses triangle point, calculates midpoint, and draws new point

        global p
        direction = random.randint(1, 3)  # triangle point to move towards

        if direction == 1:
            new_p = (((x[0] + p[0]) / 2), ((x[1] + p[1]) / 2))
            canvas.create_oval(new_p[0], new_p[1], new_p[0] + 1, new_p[1] + 1, fill='#000')
        elif direction == 2:
            new_p = (((y[0] + p[0]) / 2), ((y[1] + p[1]) / 2))
            canvas.create_oval(new_p[0], new_p[1], new_p[0] + 1, new_p[1] + 1, fill='#000')
        else:
            new_p = (((z[0] + p[0]) / 2), ((z[1] + p[1]) / 2))
            canvas.create_oval(new_p[0], new_p[1], new_p[0] + 1, new_p[1] + 1, fill='#000')

        p = new_p  # update current point
        window.after(speed, add_point)  # draw new points recursively

    canvas.pack()
    window.after(speed, add_point)
    window.mainloop()


# choose triangle points for random triangle
# x_x = random.randint(1, width)
# x_y = random.randint(1, height)
# y_x = random.randint(1, width)
# y_y = random.randint(1, height)
# z_x = random.randint(1, width)
# z_y = random.randint(1, height)

# a more regular triangle
chaos_game((width/2, height/5), (width/5, height * (4/5)), (width * (4/5), height * (4/5)))

# random triangle
# chaos_game((x_x, x_y), (y_x, y_y), (z_x, z_y))
