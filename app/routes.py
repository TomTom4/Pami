from app import app
from app import controller
from flask import request


control = controller.Controller()


@app.route('/api/login', methods=['POST'])
def login():
    data = request.form
    print(data)
    try:
        response = control.connect_imap(data["server_url"], data["email"],
                                        data["password"])
        if response == "connected":
            return "true"
    except Exception:
        return "false"


@app.route('/api/logout')
def logout():
    response = control.close_imap_connection()
    if response == "disconnected":
        return "true"
    return "false"


@app.route('/mailboxes')
def list_mailboxes():
    return control.list_mailboxes()


@app.route('/search_emails')
def search(mailbox=None):
    return control.search_emails(mailbox)


@app.route('/emails')
def retrieve_emails():
    return control.retrieve_emails()


@app.route('/email')
def retrieve_mail(id):
    return control.retrieve_email(id)
