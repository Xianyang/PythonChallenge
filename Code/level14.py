from PIL import Image

source = Image.open('../Resource/wire_level14.png')
target = Image.new(source.mode, (100, 100))

def is_boundary(x, y, i):
    if x == 100 or y == 100 or x == -1 or y == -1:
        return True
    if target.getpixel((x, y)) != (0, 0, 0):
        return True

    return False

x, y = 0, 0
dir = 'E'

for i in xrange(0, 10000):
    target.putpixel((x, y), source.getpixel((i, 0)))
    if dir == 'E':
        x += 1
        if is_boundary(x, y, i + 1):
            dir = 'S'
            x -= 1
            y += 1
    elif dir == 'S':
        y += 1
        if is_boundary(x, y, i + 1):
            dir = 'W'
            y -= 1
            x -= 1

    elif dir == 'W':
        x -= 1
        if is_boundary(x, y, i + 1):
            dir = 'N'
            x += 1
            y -= 1

    elif dir == 'N':
        y -= 1
        if is_boundary(x, y, i + 1):
            dir = 'E'
            y += 1
            x += 1

# target.show()

# solution 2
from PIL import Image

src = Image.open('../Resource/wire_level14.png')
dst = Image.new(src.mode, (100, 100))
x, y, idx = -1, 0, 0            # back a step
steps = [1,0, 0,1, -1,0, 0,-1]
while idx < 10000:
    nx, ny = x + steps[0], y + steps[1]
    if 0 <= nx < 100 and 0 <= ny < 100 \
            and dst.getpixel((nx, ny)) == (0, 0, 0):
        x, y = nx, ny
        dst.putpixel((x, y), src.getpixel((idx, 0)))
        idx += 1
    else:
        steps = steps[2:] + steps[:2] # turn
# dst.show()
