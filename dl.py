import urllib.request as REQ
import sys
import os

pr = print
pn = lambda s: pr(s, '\n')

# Get argvs
url = sys.argv[1]
fn  = sys.argv[2]

# Globals
fn_part = fn + '.part'
is_range = True
bytes_start = 0
CHUNK = 1024 * 1024

# 🔎
if os.path.isfile(fn):
  pr('⚠️ File exists')
  exit()

# 🔎 check if server supports range
try:
  headers = {
    'User-Agent': 'Mozilla/5.0',
    'Range':      'bytes=0-'
  }
  req = REQ.Request(
    url, 
    headers=headers, 
    method='HEAD'
  )
  res = REQ.urlopen(req)
  pn(res.headers)
except Exception as e:
  pr('⚠️', e)
  exit()

is_range = res.getheader('accept-ranges') == 'bytes'

#
if is_range:
  if os.path.isfile(fn_part):
    bytes_start = os.path.getsize(fn_part)
else:
  if os.path.isfile(fn_part):
    os.remove(fn_part)

#
try:
  headers = {
    'User-Agent': 'Mozilla/5.0',
    'Range':      'bytes=%d-' % bytes_start
  }
  req = REQ.Request(url, headers=headers)
  res = REQ.urlopen(req)
  pn(res.headers)
except Exception as e:
  pr('⚠️', e)
  exit()

if is_range:
  file_len = int(
    res.getheader('content-range').split('/')[-1]
  )
else:
  file_len = int(res.getheader('content-length'))

copied = bytes_start - bytes_start % CHUNK
with open(fn_part, 'ab') as f:
  while True:
    chunk = res.read(CHUNK)
    if not chunk:
      pass

    f.write(chunk)

    copied += CHUNK
    if copied >= file_len:
      print('⏬✅')
      os.rename(fn_part, fn)
      break

    print('⏬', '%.2f%%' % (copied/file_len*100))
