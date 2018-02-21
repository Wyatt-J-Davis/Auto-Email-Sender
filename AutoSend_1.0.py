from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#Function to pull contacts from the contact.txt file
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

#Reads temlate file and returns it as a template object
def read_template(filename):
    with open(filename, mode='r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)




def main(): 
	#Sets up server (s)
	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	s.starttls()
	s.login('YourEmail@email.com','EmailPassword')

	names, emails = get_contacts('contacts.txt') # read contacts
	message_template = read_template('body.txt')

 	#For each contact, send the email:
	for name, email in zip(names, emails):
		msg = MIMEMultipart()       # create a message

   		 # add in the actual person name to the message template
		message = message_template.substitute(PERSON_NAME=name.title())

    		# setup the parameters of the message
		msg['From']='whyit11@gmail.com'
		msg['To']=email
		msg['Subject']="TEST"

   	        # add in the message body
		msg.attach(MIMEText(message, 'plain'))

   		 # send the message via the server set up earlier. 
		s.send_message(msg)
    
		del msg
	
	#Terminate session	
	s.quit()

if __name__ == '__main__':
	main()
