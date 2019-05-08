#!/anaconda3/bin/python
import os, cgi, view

files = os.listdir('data')
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/' + pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''
<!doctype html>
<html>
<head>
  <title>WEB2 Python - create</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB2 Python</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="create.py">create</a>
      <form action="process_create.py" method="post">
          <p><input type="text" name="title" placeholder="Title"></p>
          <p><textarea rows="5" name="description" placeholder="Description"></textarea></p>
          <p><input type="submit"></p>
      </form>
</body>
</html>
'''.format(
    title = pageId,
    desc = description,
    listStr = view.getList()
    )
)
