import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('Kirby_and_The_Forgotten_Land_Icon.jpg', 6)

first_color = colors[0]
rgb = first_color.rgb

r = rgb[0]
g = rgb[1]
b = rgb[2]

color1 = (r, g, b)
print(color1)