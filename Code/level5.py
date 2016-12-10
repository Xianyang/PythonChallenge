import pickle, urllib

handle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(handle)
handle.close()

# solution 1
# for elt in data:
#     print "".join([e[1] * e[0] for e in elt])

# solution 2
print '\n'.join([ reduce(lambda x, y: x + y[0] * y[1], line, '') for line in data])
