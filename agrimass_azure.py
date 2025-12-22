import msal
import requests
import time
import tkinter as tk
from tkinter import filedialog

# ===== CONFIGURE HERE =====
CLIENT_ID = "<YOUR-ID-HERE>"
TENANT_ID = "<YOUR-TENANT-ID-HERE>"
shared_mailbox = "<YOUR-SHARED-MAILBOX-HERE>" # If you use one (example: no-replay@domain.com)
# =========================

# Authentication Endpoint
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["Mail.Send"]

# Public App Creation
app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY)

# Interactive Login
result = app.acquire_token_interactive(scopes=SCOPE, prompt="select_account")

if "access_token" not in result:
    print("Authentication Error:", result.get("error_description"))
    exit(1)

access_token = result["access_token"]

# Headers with token
headers = {"Authorization": f"Bearer {access_token}"}

# Open the file explorer: choose the recipients list
root = tk.Tk()
root.withdraw()

file_destinatari = filedialog.askopenfilename(
    title="Select the txt file with the recipients emails",
    filetypes=[("Text files", "*.txt")]
)

if not file_destinatari:
    print("No file selected, exit...")
    exit(1)

try:
    with open(file_destinatari, "r") as f:
        destinatari = [line.strip() for line in f if line.strip()]
except Exception as e:
    print("Error reading file:", e)
    exit(1)

# Subject input
subject = input("E-mail subject: ").strip()

# Multi-line email body input (HTML or text)
print("E-mail body. Type 'END' on a new line to end.")
lines = []
while True:
    line = input()
    if line.strip() == "END":
        break
    lines.append(line)
body_content = "\n".join(lines)

# Format selection: text or HTML
content_type = input("Send e-mail as HTML? (y/n): ").strip().lower()
if content_type == "y":
    content_type = "HTML"
else:
    content_type = "Text"

# Mail sending cycle (we put the shared mailbox on 'from')
for to_email in destinatari:
    email_msg = {
        "message": {
            "subject": subject,
            "body": {"contentType": content_type, "content": body_content},
            "toRecipients": [{"emailAddress": {"address": to_email}}],
            "from": {"emailAddress": {"address": shared_mailbox}}
        }
    }

    endpoint = "https://graph.microsoft.com/v1.0/me/sendMail"
    try:
        response = requests.post(endpoint, headers=headers, json=email_msg)
        if response.status_code == 202:
            print(f"✅ Email sent to {to_email}")
        else:
            print(f"❌ Error sending to {to_email}: {response.status_code} {response.text}")
    except Exception as e:
        print(f"❌ Error sending to {to_email}: {e}")

    time.sleep(3)
