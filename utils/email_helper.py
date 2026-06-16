import imaplib
import email
import re
import time
def extract_otp_from_email(username, app_password, subject_filter="Your Verification Code"):
    # Connect to the Gmail IMAP server
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    # Login
    mail.login(username, app_password)
    # Select the Inbox
    mail.select('inbox')
    print(f"\n[Email] Waiting for OTP email with subject: '{subject_filter}'...")
    # Wait up to 30 seconds for the email to arrive
    for i in range(15):
        # Search for all unread emails with the specific subject
        status, messages = mail.search(None, f'(UNSEEN SUBJECT "{subject_filter}")')
        email_ids = messages[0].split()
        if email_ids:
            # Get the most recent email
            latest_email_id = email_ids[-1]
            # Fetch the email contents
            status, msg_data = mail.fetch(latest_email_id, '(RFC822)')
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)
            # Extract the body text
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode()
            else:
                body = msg.get_payload(decode=True).decode()
            # Use RegEx to find exactly 6 digits!
            match = re.search(r'\b\d{6}\b', body)
            if match:
                otp = match.group(0)
                print(f"[Email] Successfully extracted OTP: {otp}")
                # Close connection and return
                mail.close()
                mail.logout()
                return otp
        # If no email found, wait 2 seconds and try again
        time.sleep(2)
    mail.close()
    mail.logout()
    raise Exception("OTP Email never arrived!")