```
Support:
➡️ Large file
➡️ Interruption resume
➡️ Progress indicator

How to:
python3 dl.py URL                FILENAME
python3 dl.py http://x.com/x.mp4 pirates.mp4
```

## Notes 📝 

### Range
```
res.status: 206
res.msg:    Partial Content

# REQ:
'Range': 'bytes=1000-2000'

# RES:
Content-Range: bytes 1000-2000/1105429424
Accept-Ranges: bytes
Content-Length: 1001 # ‼️ 1001
Content-Type: video/mp4; charset=utf-8

# REQ:
'Range': 'bytes=0-'

# RES:
Content-Range: bytes 0-20387229/20387230
Accept-Ranges: bytes
Content-Length: 20387230
Content-Type: video/mp4; charset=utf-8
```

### Content-Type
```
text/html; charset=UTF-8
image/png
video/mp4; charset=utf-8
```

### copyfileobj
Can’t implement progress indicator
```
f = open(fn, 'wb')
shutil.copyfileobj(res, f)
```

### res
```
pn(res.url)
pn(res.getheaders())
pn(res.headers)
pn(res.status)
pn(res.msg)
pn(res.getheader('content-type'))
pn(res.getheader('content-length'))
```

