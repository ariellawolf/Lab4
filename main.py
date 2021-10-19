#!/usr/bin/python37all
# Save file as /usr/lib/cgi-bin/test.py
print(""”

Content-type:text/html\n\n
<html>
<body>
<form action="/cgi-bin/test.py" method="POST"
<input type="submit" value="create a new page">
</form>
</body>
</html>

""")
