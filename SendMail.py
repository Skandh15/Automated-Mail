import smtplib

try:
    user = 'skandhof@gmail.com'
    recipient = 'tavishi.pandey@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, "9719428232")
    message = """\
Subject: Hey love

This mail will remind you that i love you. 
  
Hugs and Kisses to mooshooo. """
    server.sendmail(user, recipient, message)
    print("Email Sent")
    # print(message)
except Exception as exception:
    print(exception)
finally:
    server.quit()
