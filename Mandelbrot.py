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
	for y in range(height):
		row = []
		for x in range(width):
			C = get_complex(x, y, width, height)
			if in_set(C):
				row.append('*')
			else:
				row.append(' ')
		print ' '.join(row)

print render(120,80)



