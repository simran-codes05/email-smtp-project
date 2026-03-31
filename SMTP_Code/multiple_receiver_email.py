#importing SMTP library
import smtplib

#create a list to stores the receiver's email
Emails = [""]
password = ''
#for loop to fetch the list
for email in Emails:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("simranneman3@gmail.com",password)
    message = "Hello, \n\n This email from simran\n\n Bye"
    s.sendmail("simranneman3@gmail.com",email,message)
    s.quit()
print("Emails send successfully to receivers.")
    

