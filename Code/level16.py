from PIL import Image

def straighten(source):
    target = source.copy()
    for y in range(source.size[1]):
        line = [source.getpixel((x, y)) for x in range(source.size[0])]
        index = line.index(195)
        new_line = line[index:] + line[:index]
        for x, pixel in enumerate(new_line):
            target.putpixel((x, y), pixel)


    return target

out = straighten(Image.open('../Resource/mozart_level16.gif'))
out.show()
