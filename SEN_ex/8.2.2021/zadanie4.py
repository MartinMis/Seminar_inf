f = open('let.txt', 'r')
heights = []

up_time, down_time, last_height, min_height_time = 0, 0, 0, 0

for line in f:
    line = line.strip()
    line = int(line)
    heights.append(line)

for height in heights:
    if height > last_height:
        up_time += 2
        last_height = height
    else:
        down_time += 2
        last_height = height

x = heights.index(min(heights))
min_height_time = 2*x+2

print("vrutlunik stupal ", up_time, 'min a klesal', down_time, 'min')
print('vrtulnik bol najblizsie k zemi na ', min_height_time, 'minute')
