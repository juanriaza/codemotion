import requests
import lxml.html
import os


URL_CEPSTRAL = 'http://cepstral.com/demos/'
FILE_NAME = 'demo.wav'

req = requests.get(URL_CEPSTRAL)
html = req.content
tree = lxml.html.fromstring(html)
form = tree.forms[0]
form_values = dict(form.form_values())
form_values.update({'content': 'codemotion rocks', 'submit': 'Say It!'})
wav_req = requests.get(URL_CEPSTRAL + 'cepcom_demo.cgi/cepstral.wav', params=form_values)
local_file = open(FILE_NAME, 'wb')
local_file.write(wav_req.raw.read())
local_file.close()
os.system('mplayer %s' % FILE_NAME)
