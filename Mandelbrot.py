'''
renders mandelbrot set.
'''

import PIL.Image

def in_set(C):
    '''
    Tests whether complex number 'C' is in the set. 
    returns number of iterations before escape. If C is in set,
    returns 600.
    '''
    Z = 0
    for iteration in range(1, 600):
        if abs(Z) > 2:
            return iteration
        Z = Z ** 2 + C
    return 600

def get_complex(x, y, width, height):
    '''
    translates graph coordinates (x,y) in image size (width, height)
    to complex number. Returns complex number.
    '''
    return complex(-2 + 3.0/width * x, 1 - 2.0/height * y)

def get_color(num):
    '''
    takes number and returns an HSV color. if number is greater 
    than 600, returns black
    '''
    if num < 600:
        hsv = num  % (360 / 6)
        return (int(hsv * 6), 360, 360)
    else:
        return (0, 0, 0)

def render(width, height):
    '''
    given width and height of image, returns an image of mandelbrot set.
    '''
    mandel = PIL.Image.new('HSV', (width, height))
    for y in range(height):
        for x in range(width):
            C = get_complex(x, y, width, height)
            color = get_color(in_set(C))
            mandel.putpixel((x,y), color)
    mandel.show()
    
render(1200,800)
