#!/anaconda3/bin/python
import os
import cgi
import view
# import cgitb
# cgitb.enable()
print("Content-Type: text/html")
print()

files = os.listdir('data')

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/' + pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''<!doctype html>
<html>
<head>
  <title>WEB2 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB!!!!!</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="create.py">create</a>
      <form action="process_update.py" method="post">
          <input type="hidden" name="pageId" value="{form_default_title}">
          <p><input type="text" name="title" placeholder="Title" value="{form_default_title}"></p>
          <p><textarea rows="5" name="description" placeholder="Description">{form_default_description}</textarea></p>
          <p><input type="submit"></p>
      </form>
</body>
</html>
'''.format(
    title=pageId,
    desc=description,
    #    listStr=listStr,
    listStr=view.getList(),
    form_default_title=pageId,
    form_default_description=description))

# desc=description,
# listStr=view.getList(),
# update_link=update_link,
# delete_action=delete_action))
