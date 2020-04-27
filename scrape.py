#!/bin/python3
# import requests
import pprint
import requests_html

URL = 'https://500px.com/search?submit=Submit+Query&q=portra400&type=photos'
# page = requests.get(URL)
session = requests_html.HTMLSession()
page = session.get(URL)

page.html.render(scrolldown=2000, keep_page=True)

pp = pprint.PrettyPrinter(indent=4)

sel = 'body'
# pp.pprint(page.html.page)
content = page.html.page.find(sel, first=True)

pp.pprint(content)
