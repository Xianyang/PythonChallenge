import urllib2, re

# solution 1 this is my solution

basic_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
next_nothing = basic_nothing = '12345'
# next_nothing = basic_nothing = '8022'
# next_nothing = basic_nothing = '63579'

while int(next_nothing):
    url = basic_url + next_nothing
    response = urllib2.urlopen(url).read()
    print response
    finding = re.search('\d+', response)
    if finding:
        next_nothing = finding.group(0)
    else:
        break

# first round: Yes. and the next nothing is 16044, Divide by two and keep going.

# solution 2 - better solution
import urllib2, re
basic_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
next_nothing = '63579'

while True:
    try:
        response = urllib2.urlopen(basic_url % next_nothing).read()
        print response
        next_nothing = re.search('\d+', response).group(0)
    except:
        break


