import requests

# Define the login URL
login_url = "https://webmail.syriatel.sy"

# Define the login credentials
login_data = {
    "user": "dch@dch.syriatel.sy",
    "pass": "xBk99p*60",
    "_task": "login",
}

# Send the login request and save the response to a variable
session = requests.Session()
response = session.post(login_url, data=login_data, verify=False)

# Check if the login was successful
if response.status_code == 200:
    print("Login successful.")
else:
    print("Login failed. exit")
    exit()


for cookie in session.cookies:
    print(cookie)
exit()
# Define the compose URL
compose_url = "https://webmail.syriatel.sy"


# Define the compose data
compose_data = {
    "_task": "mail",
    # "_action": "send",
    # "_id":"195862145663dbf421e8423"
    "_attachments": "",
    "_from": "26",
    "_to": "mostafa@cellusys.com",
    "_subject": "test_email_subject",
    "_message": "Tetsemail",
    # "_cc": "",
    # "_bcc": "",
    # "_replyto": "",
    # "_followupto": "",
    # "_draft_saveid": "",
    "_draft": "1",
    # "_is_html": "1",
    # "_framed": "1",
    # "editorSelector": "html",
    # "_mdn": "",
    # "_dsn": "",
    # "_priority": "0",
    "_store_target": "INBOX.Sent",
}

# Send the compose request
response = session.post(compose_url, data=compose_data)

# Check if the mail was sent successfully
if response.status_code == 200:
    print("Mail sent successfully.")
else:
    print("Failed to send mail.")

print(response.text)
