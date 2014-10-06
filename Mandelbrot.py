'''
renders mandelbrot set.
'''

import PIL.Image
from multiprocessing import Pool

def in_set(((x,y), C)):
    '''
    Tests whether complex number 'C' is in the set. 
    returns number of iterations before escape. If C is in set,
    returns 600.
    '''
    Z = 0
    for iteration in range(1, 600):
        if abs(Z) > 2:
            return (x, y), iteration
        Z = Z ** 2 + C
    return (x, y), 600

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
    # for each grid coordinate create tuple in form ((x,y), C)
    # and append to list 'l' for input into pool.map()
    coord_complex_pairs = [] 
    for y in range(height):
        for x in range(width):
            C = get_complex(x, y, width, height)
            coord_complex_pairs.append(((x,y), C))
    pool = Pool()
    #create dictionary in form (x,y): number of iterations before escape
    results = dict(pool.map(in_set, coord_complex_pairs))     
    for x,y in results:
        color = get_color(results[x,y])
        mandel.putpixel((x, y), color)
    mandel.show()
    
render(2400,1600)
