import imaplib
import email

class Controller():

	def __init__(self, session=None, view=None):
		self.database_session = session
		self.view = view 

	def connect_imap(self, imap_server_url, email_address, password):
		self.mail_session = imaplib.IMAP4_SSL(imap_server_url)
		self.mail_session.login(email_address, password)
		return "connected"
	
	def close_imap_connection(self):
		try:
			self.mail_session.close()
		except Exception as e:
			print(e)
			print("Select must be done first")
		try:
			self.mail_session.logout()
			return "disconnected"
		except Exception as e:
			print(e)
			return "failed to disconnect"

	def search_emails(self, mail_box=None):
		self.mail_session.select(mail_box)	
		return self.mail_session.search(None, 'ALL')

	def retrieve_emails(self):
		# example I got from doc, needs to dig a bit more
		typ, data = self.search_emails()
		print(f"here is the type: {typ}")
		print(f"here is the data list:{data}")
		'''
		for num in data[0].split():
			typ, data = self.mail_session.fetch(num, '(RFC822)')
			print('message %s\n%s\n'%(num, data[0][1]))
		'''
		return 'retrieved emails'

	def retrieve_email(self, num):
		self.mail_session.select()# to select which mailbox -default is INBOX
		typ, data = self.mail_session.fetch(num, '(RFC822)')
		raw_email = data[0][1].decode('utf-8')
		return email.message_from_string(raw_email)
		
	'''

	def get_all_emails(self):
		return self.session.query(Mail).all()

	def get_email(self, id):
		return self.session.query(Mail).filter(Mail.id == id)
	
	def delete_email(self, id):
		self.session.delete(self.session.query(Mail).filter(Mail.id == id))
		
	'''	
