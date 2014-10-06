import PIL.Image

def in_set(C):
    Z = 0
    for iteration in range(1, 600):
        if abs(Z) > 2:
            return iteration
        Z = Z ** 2 + C
    return 600

def get_complex(x, y, width, height):
    return complex(-2 + 3.0/width * x, 1 - 2.0/height * y)

def get_color(num):
    if num < 600:
        rgb = num  % 255
        return (0, 0, int(rgb))
    else:
        return (0, 0, 0)

def render(width, height):
    mandel = PIL.Image.new('RGBA', (width, height))
    for y in range(height):
        for x in range(width):
            C = get_complex(x, y, width, height)
            color = get_color(in_set(C))
            mandel.putpixel((x,y), color)
    mandel.show()
    
render(2400,1600)
