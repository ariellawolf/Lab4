#!/usr/bin/python37all
import cgi
import cgitb
cgitb.enable()
import json
data = cgi.FieldStorage()
brightness_level = data.getvalue('slider')
LED = data.getvalue('light')
dataDump = {"slider":brightness_level, "light":LED}
with open('led-pwm.txt', 'w') as f:
  json.dump(dataDump,f)
print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/blinkingPWM.py" method="POST">')
print('<input type="range" name="slider" min="0" max="100" value="%s"><br>' % brightness_level)
print('<input type="submit" value="Change LED brightness">')
print('</form>')
print('Brightness = %s' % brightness_level)
print('</html>')