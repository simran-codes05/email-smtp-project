#importing smtp library
import smtplib

#creating a session
s = smtplib.SMTP('smtp.gmail.com', 587) #(server location, port number)
#start TLS
s.starttls()
#Authentication login
s.login("sender_email","senderapp_password")#aap password
#message want to send
message = "This is trial message"
#send the message
s.sendmail("sender_email","receiver_email",message)
#session stop
s.quit()

print("Email send successfully")