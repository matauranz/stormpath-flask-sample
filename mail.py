
import smtplib
import email.utils
from email.mime.text import MIMEText
def mymail():
		#to  ='echo@tu-berlin.de'
		to ='matauranz@gmail.com'
		#to ='marjorietaylor31@icloud.com'
		# Create the message
		msg = MIMEText("<h1>Someone accesed stormpath steve today ...</h1> \n http://0.0.0.0:5000")
		msg['To'] = email.utils.formataddr(('Recipient', to))
		msg['From'] = email.utils.formataddr(('Sender', 'matauranz@gmail.com'))
		msg['Subject'] = 'Stormpath app...'
		
		server = smtplib.SMTP("smtp.gmail.com",587)
		#server = smtplib.SMTP("localhost",7777)=
		#session = smtplib.SMTP('smtp.gmail.com', 587) 
		server.ehlo() 
		server.starttls()
		
		
		GMAIL_USERNAME='matauranz@gmail.com'
		GMAIL_PASSWORD='steve1956'
		
		
		server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
		server.set_debuglevel(0) # show communication with the server
		print msg
		
		try:
		    sender= 'matauranz@gmail.com'
		    server.sendmail( sender , [ to ], msg.as_string())
		
		finally:
		    
		    print "done...."
		    server.quit()
		    