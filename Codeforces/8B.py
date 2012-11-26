dct = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

def prog(dat):
	d = {}
	x, y = 0, 0
	val = 0
	d[(0, 0)] = 0
	for ch in dat:
		val += 1
		dx, dy = dct[ch]
		x += dx
		y += dy
		if (x, y) in d:
			return "BUG"
		d[(x, y)] = val
		for ch1 in "LRUD":
			dx, dy = dct[ch1]
			if (x + dx, y + dy) in d and d[(x + dx, y + dy)] < val - 1:
				return "BUG"
	return "OK"

dat = raw_input()
#print dat
print prog(dat)
