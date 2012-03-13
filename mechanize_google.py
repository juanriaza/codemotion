import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.79 Safari/535.11')]
br.open('http://google.com')
br.select_form(nr=0)
br.form['q'] = 'codemotion'
br.submit()


def filter_link(link):
    link_attrs = dict(link.attrs)
    link_class = link_attrs.get('class', None)
    return link_class == 'l'

valid_links = filter(filter_link, br.links())

for link in valid_links:
    print link.url
