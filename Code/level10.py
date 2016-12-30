# a = [1, 11, 21, 1211, 111221,


# this is a look-and-say sequence

import re

def describe(s):
    sequence = re.findall('1+|2+|3+', s)
    return ''.join(str(len(x)) + x[0] for x in sequence)

s = '1'
for i in range(30):
    s = describe(s)

print len(s)
