import sys
import requests


verbose_config = {'verbose': sys.stderr}
req = requests.get('http://www.codemotion.es', config=verbose_config)
