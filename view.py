#!/anaconda3/bin/python
print("Content-Type: text/html")
print()
import os, html_sanitizer

def getList():
    sanitizer = html_sanitizer.Sanitizer()
    files = os.listdir('data')
    # 맥OS 특성 상 맨 앞 히든파일 하나 pop으로 제거 (.dataStore 어쩌구 안 생기면 필요없을 수도 있음)
    # files.pop(0)
    listStr = ''
    for item in files:
        item = sanitizer.sanitize(item)
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr
