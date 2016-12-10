# the answer is 'ocr'

import string

s = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq
glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

# solution 1 - use translate table
l = string.ascii_lowercase
table = string.maketrans(l, l[2:] + l[:2])

print string.translate(s, table)

# solution 2 - use ord() and chr()

o = ''
for c in s:
    if ord('a') <= ord(c) <= ord('z'):
        o += chr((ord(c) + 2 - ord('a')) % 26 + ord('a'))
    else:
        o += c

print o

# solution 3 - use map(), ord() and chr()

print ''.join(map(lambda x: x.isalpha() and chr((ord(x)+2-ord("a")) % 26 + ord("a")) or x, s))
print ''.join(map(lambda x: chr((ord(x)+2-ord("a")) % 26 + ord("a")) if x.isalpha() else x, s))
