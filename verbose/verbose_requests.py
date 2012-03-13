import sys
import requests

# 1
verbose_config = {'verbose': sys.stderr}
req = requests.get('http://www.codemotion.es', config=verbose_config)

# 2
s = requests.session()
s.config['verbose'] = sys.stderr
req = s.get('http://www.codemotion.es')
