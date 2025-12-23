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
           \______/            GMAIL                                                 
    

    """
    print(header)

def run_agrimass_gmail():
    print_header()
    
    # 1. Credentials
    sender_email = input("Enter your Gmail address: ")
    # Using getpass for security (hides the App Password while typing)
    password = getpass.getpass("Enter your Gmail App Password (hidden): ")

    # 2. Email Content
    subject = input("Enter Email Subject: ")
    print("\nPaste your HTML code below. Type 'END' on a new line and press Enter to finish:")
    
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    html_content = "\n".join(lines)

    # 3. Loading Recipients
    try:
        with open("mailing_list.txt", "r") as file:
            recipients = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("\n[!] Error: 'mailing_list.txt' not found. Please create it and restart.")
        return

    # 4. Sending Process
    server = None
    try:
        print(f"\nConnecting to Gmail SMTP server...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
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
            
            # Anti-spam delay (Gmail is strict, 3-4 seconds is ideal)
            time.sleep(4)

        print("\nCampaign completed successfully!")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Tip: Make sure you are using a 16-character 'App Password', not your main account password.")
    
    finally:
        if server:
            server.quit()

if __name__ == "__main__":
    run_agrimass_gmail()
