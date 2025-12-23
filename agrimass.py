import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import getpass

def print_header():
    header = r"""
             Welcome to
  /$$$$$$                      /$$ /$$      /$$                             
 /$$__  $$                    |__/| $$$    /$$$                             
| $$  \ $$  /$$$$$$   /$$$$$$  /$$| $$$$  /$$$$  /$$$$$$   /$$$$$$$ /$$$$$$$
| $$$$$$$$ /$$__  $$ /$$__  $$| $$| $$ $$/$$ $$ |____  $$ /$$_____//$$_____/
| $$__  $$| $$  \ $$| $$  \__/| $$| $$  $$$| $$  /$$$$$$$|  $$$$$$|  $$$$$$ 
| $$  | $$| $$  | $$| $$      | $$| $$\  $ | $$ /$$__  $$ \____  $$\____  $$
| $$  | $$|  $$$$$$$| $$      | $$| $$ \/  | $$|  $$$$$$$ /$$$$$$$//$$$$$$$/
|__/  |__/ \____  $$|__/      |__/|__/     |__/ \_______/|_______/|_______/ 
           /$$  \ $$                                                        
          |  $$$$$$/                                                        
           \______/                                                         
    

    """
    print(header)

def run_agrimass_smtp():
    print_header()
    
    # 1. Server Connection Details
    smtp_server = input("Enter SMTP Server address (e.g., mail.domain.com): ")
    try:
        smtp_port = int(input("Enter SMTP Port (usually 587 or 465): "))
    except ValueError:
        print("Invalid port. Defaulting to 587.")
        smtp_port = 587

    # 2. Authentication & Sender Details
    auth_user = input("Enter your SMTP Username (login): ")
    password = getpass.getpass("Enter your SMTP Password (hidden): ")
    sender_email = input("Enter the 'From' email address (Sender Display): ")

    # 3. Email Content
    subject = input("Enter Email Subject: ")
    print("\nPaste your HTML code below. Type 'END' on a new line and press Enter to finish:")
    
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    html_content = "\n".join(lines)

    # 4. Loading Recipients
    try:
        with open("mailing_list.txt", "r") as file:
            recipients = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Error: 'mailing_list.txt' not found. Please create it and restart.")
        return

    # 5. Sending Process
    server = None
    try:
        print(f"\nConnecting to {smtp_server}...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(auth_user, password)
        print("Authentication successful!\n")

        for index, recipient in enumerate(recipients, 1):
            print(f"[{index}/{len(recipients)}] Sending to {recipient}...")
            
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(html_content, 'html'))

            server.sendmail(sender_email, recipient, msg.as_string())
            print(f"Successfully sent to {recipient}")
            
            # Anti-spam delay
            time.sleep(3)

        print("\nCampaign completed successfully!")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
    
    finally:
        if server:
            server.quit()

if __name__ == "__main__":
    run_agrimass_smtp()
