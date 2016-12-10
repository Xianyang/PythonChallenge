# the answer is 'equality'

# solution 1
s = ''.join([line.rstrip() for line in open('../Resource/ocr.txt')])

occurrence = {}
for c in s: occurrence[c] = occurrence.get(c, 0) + 1
average = len(s) // len(occurrence)
print ''.join(c for c in s if occurrence[c] < average)


# solution 2
import string
print filter(lambda x: x in string.letters and s.count(x) <= 100, s)


# solution 3
occurrence = {}
output = ''
for c in s:
    if c in occurrence.keys():
        continue
    else:
        count = occurrence[c] = s.count(c)
        if count < 100:
            output += c

print output

# solution 4
print ''.join(c for c in s if c.isalpha() and s.count(c) < 100)

