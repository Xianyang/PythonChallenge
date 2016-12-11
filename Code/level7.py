from PIL import Image
import re, urllib, StringIO

# open the image
im = Image.open('../Resource/oxygen.png')
img = urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read() # read image to a string
im = Image.open(StringIO.StringIO(img))

# solution 1
line = [im.getpixel((i, 47)) for i in range(0, im.size[0], 7)]
ords = [r for r, g, b, a in line if r == g == b]
message = ''.join(map(chr, ords))
number_in_message = re.findall('\d+', message)
final_message = map(int, number_in_message)
print ''.join(map(chr, final_message))

# solution 2 - single line solution

print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords))))))

