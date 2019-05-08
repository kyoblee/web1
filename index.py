#!/anaconda3/bin/python
# 2019.5 완료
import cgi, os, view
import html_sanitizer

sanitizer = html_sanitizer.Sanitizer()
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
print('''
<!doctype html>
<html>
<head>
  <title>WEB2 - Python</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB2 Python</a></h1>
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
        title = title,
        desc = description,
        listStr = view.getList(),
        update_link = update_link,
        delete_action = delete_action
    )
)
