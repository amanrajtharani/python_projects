import pandas as pd
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send an email with the results
def send_email(subject, message, from_, to_, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = from_
    msg['To'] = ", ".join(to_)  # Join multiple recipients with commas
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    try:
        server = sm.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_username, smtp_password)
        server.sendmail(from_, to_, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Read email addresses from Excel file
df = pd.read_excel('email.xlsx')
email_col = df.get("emails")
lemail = email_col.dropna().tolist()  # Drop NaN values and convert to list

# SMTP server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 465
smtp_username = "amantharani123@gmail.com"
smtp_password = "kpqf upzm pfgf svnp"
from_ = "amantharani123@gmail.com"

# Email content
subject = "Testing message"
message = "This is a test email sent from Python."

# Sending emails
send_email(subject, message, from_, lemail, smtp_server, smtp_port, smtp_username, smtp_password)
