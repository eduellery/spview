# Yep

def converte(d, h):
	x = '01/';
	# Dias
	if d == 0:
		x += '06'
	elif d == 1:
		x += '07'
	elif d == 2:
		x += '08'
	elif d == 3:
		x += '09'
	elif d == 4:
		x += '10'
	elif d == 5:
		x += '11'
	elif d == 6:
		x += '12'
	else:
		x = 'ERROR'
		return x
	x += '/13T'
	# Horas
	if h >= 0 and h < 19:
		x += '0'
		x += str(h/2)
	elif h >= 20 and h < 39:
		x += str(h/2)
	elif h >= 40 and h <= 47:
		x += str(h/2)
	else:
		x = 'ERROR'
		return x
	if h % 2 == 0:
		x += ':00:00Z'
	else:
		x += ':30:00Z'
	return x

print(converte(6,48));