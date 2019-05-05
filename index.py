#!/anaconda3/bin/python
import os, cgi, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()
# import cgitb
# cgitb.enable()
print("Content-Type: text/html")
print()

'''
#view.py 로 이동
def getList():
    files = os.listdir('data')
# 맥OS 특성 상 맨 앞 히든파일 하나 pop으로 제거 (.dataStore 어쩌구 안 생기면 필요없을 수도 있음)
# files.pop(0)
    listStr = ''
    for item in files:
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(
                name=item)
    return listStr
'''

form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form["id"].value
    description = open('data/' + pageId, 'r').read()
    title = sanitizer.sanitize(title)
    # description = description.replace('<', '&lt;')
    # description = description.replace('>', '&gt;')
    description = sanitizer.sanitize(description)
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    title = pageId = 'Welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action = ''
print('''<!doctype html>
<html>
<head>
  <title>WEB2 - Python</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB for Python lectures</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="create.py">create</a>
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(
    title=title,
    desc=description,
    listStr=view.getList(),
    update_link=update_link,
    delete_action=delete_action))

# desc=description,
# listStr=view.getList(),
# update_link=update_link,
# delete_action=delete_action))
