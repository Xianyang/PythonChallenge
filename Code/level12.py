from PIL import Image
from cStringIO import StringIO

s = open("../Resource/evil2.gfx", "rb").read()
for i in range(5):
    piece = s[i::5]  # every fifth byte, starting at i
    im = Image.open(StringIO(piece))
    f = open("../Resource/level12_output/%d.%s" % (i, im.format.lower()), "wb")
    f.write(piece)
    f.close()

f = open("../Resource/evil2.gfx", "rb").read()
for i in range(5):
    open("image"+str(i)+".dat", "wb").write(f[i::5])