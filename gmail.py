import smtplib
from email.message import EmailMessage
msg=EmailMessage()
msg['From']='6870883@stud.nau.edu.ua' #email sender
msg['To']=['dzigalchuk.stas@gmail.com','stanislawiii@icloud.com'] #email getters
msg['subject']=input('Enter the subject of mail: ') # subject of mail
msg.set_content(input('Enter The Text of input: ')) # text of mail

smtp_server=smtplib.SMTP('smtp.gmail.com',587) #starting our smtp server
smtp_server.starttls()
smtp_server.login(msg['From'],'stas.dzygalchuk')
smtp_server.send_message(msg)
smtp_server.quit()