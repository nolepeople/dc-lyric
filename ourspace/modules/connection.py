import speedtest

def convert(c):
    step = 1000.0

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if c < step:
            return "%3.1f %s" % (c, x)
        c /= step

def SpeedtestResult():
    a = speedtest.Speedtest()
    a.get_best_server()
    ping = a.results.ping
    download = convert(a.download())
    upload = convert(a.upload())

    return f"""```
ping: {ping} ms
upload: {upload}
Donwload: {download}
```"""

