# the answer is 'equality'

# solution 1
s = ''.join([line.rstrip() for line in open('../Resource/ocr.txt')])

occurrence = {}
for c in s: occurrence[c] = occurrence.get(c, 0) + 1
average = len(s) // len(occurrence)
print ''.join(c for c in s if occurrence[c] < average)


# solution 2
import string
print filter(lambda x: x in string.letters, s)


# solution 3


