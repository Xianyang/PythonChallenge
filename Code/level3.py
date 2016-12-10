# the answer is 'linkedlist' and solution 4 is fastest in this filesh

import time

start_time = time.time()

# solution 1 - this is my solution
# time O(n), space O(1)
text = ''.join(line for line in open('../Resource/equality.txt'))
text = text.replace('\n', '')
result = ''

for i in range(len(text) - 8):
    t1 = text[i] + text[i + 4] + text[i + 8]
    t2 = text[i + 1 : i + 4] + text[i + 5: i + 8]

    if t1.islower() and t2.isupper():
        result += text[i + 4]

print result
time1 = time.time()
print 'solition 1 uses %f seconds' % (time1 - start_time)

# solution 2. this solution is posted on the wiki.
result = ''
znaki = [''] * 9
for letter in text:
    del znaki[0]
    znaki.append(letter)
    if not znaki[0].isupper() and \
        znaki[1].isupper() and \
        znaki[2].isupper() and \
        znaki[3].isupper() and \
        znaki[4].islower() and \
        znaki[5].isupper() and \
        znaki[6].isupper() and \
        znaki[7].isupper() and \
        not znaki[8].isupper():
        result += znaki[4]

print result
time2 = time.time()
print 'solition 2 uses %f seconds' % (time2 - time1)

# solution 3. this solution is posted on the wiki
import string
result = ''
for i in xrange(len(text) - 8):
    if [c for c in text[i:i+9] if c in string.ascii_lowercase] == [text[i], text[i + 4], text[i + 8]]:
        result += text[i + 4]

print result
time3 = time.time()
print 'solition 3 uses %f seconds' % (time3 - time2)

# solution 4 - use re. this solution is posted on the wiki
import re
result = ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text))
print result
time4 = time.time()
print 'solution 4 uses %f seconds' % (time4 - time3)
