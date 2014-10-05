import PIL.Image

def in_set(C):
	Z = 0
	for iteration in range(1, 600):
		if abs(Z) > 2:
			return False
		Z = Z ** 2 + C
	return True

def get_complex(x, y, width, height):
	return complex(-2 + 3.0/width * x, 1 - 2.0/height * y)

def render(width, height):
	mandel = PIL.Image.new('RGBA', (width, height))
	for y in range(height):
		row = []
		for x in range(width):
			C = get_complex(x, y, width, height)
			if in_set(C):
				mandel.putpixel((x,y), (255, 255, 255, 0))
	mandel.show()

print render(1200,800)




