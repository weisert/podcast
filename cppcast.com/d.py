#!/usr/bin/env python

from subprocess import check_call

def download(url, output_name=None):
  try:
    args = ['wget', url]
    if output_name:
      args.extend(['-O', output_name])
    check_call(args)
  except:
    print 'Except:', url


links = [
  'http://traffic.libsyn.com/cppcast/Episode1.final.mp3',
  'http://traffic.libsyn.com/cppcast/Episode2.final.mp3',
  'http://traffic.libsyn.com/cppcast/Episode3.final.mp3',
  'http://traffic.libsyn.com/cppcast/Episode4.output.mp3',
  'http://traffic.libsyn.com/cppcast/Episode5.output.mp3',
  'http://traffic.libsyn.com/cppcast/Episode6.output.mp3'
]

for index, link in enumerate(links):
  download(link, 'cppcast-{0:03d}.mp3'.format(index + 1))

template = 'http://traffic.libsyn.com/cppcast/cppcast-{0:03d}.mp3'

for i in range(7, 66):
  file_url = template.format(i)
  download(file_url)

