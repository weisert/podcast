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


template = 'https://golangshow.com/cdn/episodes/{0:03d}.mp3'

for i in range(1, 67):
  file_url = template.format(i)
  download(file_url)

download('https://golangshow.com/cdn/episodes/interview_bred.mp3', '029.mp3')
download('https://golangshow.com/cdn/episodes/interview_rob.mp3', '030.mp3')
download('https://golangshow.com/cdn/episodes/055_xyz.mp3', '055.mp3')

