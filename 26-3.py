f = open('26gg.txt')
long, n = [int(x) for x in f.readline().split()]
data = [(int(x.split()), int(x.split())) for x in f.readlines()]
data = sorted(data, key = lambda x: x[1])
prev_dok, new_doklad, k, last_beginning = 0, 0, 0, 0

while new_doklad < long:
	new_doklad = long
for i in data:
	if i[0] >= prev_dok and i[1] <= new_doklad:
		last_beginning = i[0]
		new_doklad = i[1]
	if new_doklad < long:
		prev_dok = new_doklad
		k +=1
	print(k, last_beginning)
