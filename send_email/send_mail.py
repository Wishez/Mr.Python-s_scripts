#!C:/Users/rory_/AppData\Local/Programs/Python/Python36/python.exe

import cgi
import html
import smtplib


form = cgi.FieldStorage()

name = form.getfirst('name', 'Empty.')
tel = form.getfirst('tel', 'Empty.')
email = form.getfirst('email', 'Empty.')
birthday = form.getfirst('birthday', 'Empty.')
message = form.getfirst('message', 'Run your imagination.')

name = html.escape(name)
tel = html.escape(tel)
email = html.escape(email)
birthday = html.escape(birthday)
message = html.escape(message)



print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
		<html>
		<head>
			<title>Обработка данных форм</title>
			<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  		<link rel="stylesheet" href="../style.css">
		</head>
		<body>
			<div class='container'>""")

print("<h1>Проверь свой e-mail!</h1>")
# print("<p>Name: {}</p>".format(name))
# print("<p>Telephone: {}</p>".format(tel))
# print("<p>E-mail: {}</p>".format(email))
# print("<p>Birthday: {}</p>".format(birthday))
# print("<p>Message: {}</p>".format(message))

print("""</div>
		</body>
	   </html>""")
# myEmail = 'shiningfinger@list.ru'
# say = 'Hi, my name is ' + name + ",\n" + 'my birthday is ' + birthday + ".\n" + 'M: ' + message + "\n" +'You can call me to this telephone ' + tel + " or just write me to this e-mail" + email + '\n' + 'Now, you know almost everything about me.'
		
# smtpObj = smtplib.SMTP('smtp.mail.ru', 465)
# smtpObj.starttls()
# smtpObj.login('shiningfinger@list.ru', 'ruking198237645')
# smtoObj.sendmail("shiningfinger@list.ru", "shiningfinger@list.ru", say)
# smtoObj.quit()