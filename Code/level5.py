import pickle, urllib

handle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(handle)
handle.close()

for elt in data:
    for e in elt:
        a = e[1] * e[0]
    print "".join([e[1] * e[0] for e in elt])