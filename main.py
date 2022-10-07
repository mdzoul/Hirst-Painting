import colorgram
import random as r
import turtle as t


def color(num_colors):
    """Extracts color palette from .jpg file"""
    colors = colorgram.extract('Kirby_and_The_Forgotten_Land_Icon.jpg', num_colors)

    colors_in_jpg = []
    for i in range(0, num_colors):
        extract_colors = colors[i]
        rgb = extract_colors.rgb

        rgb_tuple = (rgb[0], rgb[1], rgb[2])
        colors_in_jpg.append(rgb_tuple)

    return colors_in_jpg


def draw_dot(num_colors):
    """Draws the dot"""
    t.colormode(255)
    dot_color = r.choice(color(num_colors))

    # dot(size=, color=)
    alex.dot(20, dot_color)
    alex.penup()
    alex.fd(40)


def painting(size):
    for n in range(1, size):
        for j in range(2):
            for dot in range(n):
                # Choose number of colors to sample from .jpg
                draw_dot(30)
            alex.rt(90)


alex = t.Turtle()
alex.speed(0)
alex.hideturtle()

# Change the size of painting
painting(15)

screen = t.Screen()
screen.exitonclick()
