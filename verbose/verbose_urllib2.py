import urllib2

h = urllib2.HTTPHandler(debuglevel=1)
opener = urllib2.build_opener(h)
request = urllib2.Request('http://www.codemotion.es')
opener.open(request).read()
