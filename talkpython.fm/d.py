#!/usr/bin/env python

import lxml.html as html
import requests
from StringIO import StringIO
from subprocess import check_call


def download(url, output_name=None):
  try:
    args = ['wget', url]
    if output_name:
      args.extend(['-O', output_name])
    check_call(args)
  except:
    print 'Except:', url


base_url = 'https://talkpython.fm'
episodes_all = base_url + '/episodes/all'
data = requests.get(episodes_all)
io = StringIO(data.content)
page = html.parse(io)
table = page.getroot().find_class('table table-hover episodes').pop()
rows = table.getchildren()[1].getchildren()

links = []
for row in rows:
  link = row.getchildren()[2].getchildren()[0].attrib['href'] 
  link = link.replace('/episodes/show', '/episodes/download')
  links.append(base_url + link+ '.mp3')

links.reverse()

for index, link in enumerate(links):
  download(link, 'talkpython.fm-{0:03d}.mp3'.format(index))

