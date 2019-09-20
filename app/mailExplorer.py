import getpass, imaplib

M = imaplib.IMAP4_SSL('ssl0.ovh.net')
print("created IMAP4 object")
M.login('contact@thomas-pouvreau.fr', getpass.getpass())
print("Login in")
M.select()
print("about to retrieve mails")
typ, data = M.search(None, 'ALL')
for num in data[0].split():
	typ, data = M.fetch(num, '(RFC822)')
	print('message %s\n%s\n'%(num, data[0][1]))

print("closing connection")
M.close()
print("logging out")
M.logout()
