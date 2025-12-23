# AgriMass
*Free mass mail marketing tool*

<img width="769" height="439" alt="agrimass" src="https://github.com/user-attachments/assets/7770c228-1ed8-46ef-98d6-16d11c1dc520" />


# AgriMass - A Free and Unlimited Mass Mailing Tool  

## 📖 Project Background  
My company needed a mass mailing tool to reach all our customers, and I was tasked with finding a suitable one. I initially opted for MailChimp, leveraging its trial period since the free version is quite limited. After completing the task, I wondered:  

> *Why do all these tools come with restrictions or require a paid plan?*  
> *Why not create an independent, unlimited, and free tool that does the same job?*  

And so... ***AgriMass*** *was born.* 🚀  

---
## What is AgriMass?

AgriMass is a versatile, free open-source tool for bulk email delivery. 

It offers seamless integration with ***your own SMTP servers***, ***Gmail***, and ***Microsoft Graph API (Microsoft 365)***, allowing you to manage large-scale communications ***using your existing infrastructure without subscription fees.***

---

## ⚙️ How It Works  

1. **Download the repository**

     ```bash
         git clone https://github.com/Uriel-SG/AgriMass.git
      ```    
2. **Prepare your recipient list** by adding email addresses to the `mailing_list.txt` file  
3. **Design a professional email template** using a **free MailChimp account** or on **[beefree.io](https://beefree.io/)** (recommended)
4. **Copy the template in ***HTML*** format**  
5. **Run AgriMass**:  
   - If using **your own mail server** with your domain, remember to modify `agrimass.py` with your **smtp server** and your **server credentials**. After that, you are ready:  
     ```bash
     python agrimass.py
     ```  
   - If using a **Gmail** account, keep in mind that Gmail imposes a daily limit on sent emails. If this works for your needs, feel free to proceed:  
     ```bash
     python agrimass_gmail.py
     ```
   - If using a **Microsoft** 365 account: configuration instructions and Graph API setup are covered *in the next sectiion*.
    
6. **Enter your credentials**, email subject, and *paste the HTML content of your MailChimp/beefree template*.  
   *(If the terminal warns you about a long input, just proceed and confirm.)*  
7. Press Enter... and ***BOOM! Your emails are sent.*** 

🎉 **Simple, fast, and free!**  

---

## 🪟 Microsoft 365 Instruction

### 1. Azure Configuration

Follow these steps to register your application in the Azure portal:

- *Access the Portal:* Navigate to [https://portal.azure.com](portal.azure.com) and log in with an Administrator account.

- *Microsoft Entra ID:* From the left-hand menu, select `Microsoft Entra ID`.

- *App Registrations:* Under the `Manage` section on the left sidebar, click on `App registrations`.

- *Create New:* Click the `+ New registration` button.

- *Initial Setup:*

     a. Enter a Name for your application.

     b. If prompted for a "Redirect URI", enter: `http://localhost`.

     c. Click `Register`.

- *Save Credentials:* Once created, the application overview will display several details. Copy and save the following:

     a. **Application (client) ID**

     b. **Directory (tenant) ID**

- *Configure Permissions:*

     a. Inside your registered app, click on `API permissions` (or `Add Permission`).

     b. Select `Microsoft Graph`.

     c. Choose `Delegated permissions`.

     d. Search for and check the `mail.send` permission.

     e. Click `Add permissions` to finalize.

- *Authentication Verification:* To ensure everything is correct, click on `Authentication` in the left menu and verify that the URI is present. If it is missing:

     a. Click `+ Add a platform`.

     b. Select `Mobile and desktop applications`.

     c. Enter the URI: `http://localhost`.

*Note: Ensure that you grant admin consent for the permissions if your organization's policy requires it to enable the mail.send functionality.*


### 2. Sending via Shared Mailboxes (Microsoft 365)

While you can send emails directly from your personal account, *Microsoft 365 also allows you to use Shared Mailboxes as the sender.*

***Why use Shared Mailboxes?*** 

The main advantage is flexibility: as an admin, you can create as many shared mailboxes as you need (e.g., no-reply@yourdomain.com, marketing@yourdomain.com) at no extra licensing cost.

- **Configuration Steps:**

     a. *Permissions:* You must have "Send As" permissions for the specific mailbox. This is managed through the Microsoft 365 Admin Center: select the desired shared mailbox and add your user account to the "Send As" permission group.

     b. *Example:* you may granted yourself permissions for no-reply@yourdomain.com.

     c. *Sending Strategy:* Once permissions are active, you can use any of these shared addresses as your sender identity, making it ideal for professional bulk messaging or departmental notifications.

**Ready to Go: To start sending, simply configure the Client ID, Tenant ID, and the Shared Mailbox address within the Python script. Once these parameters are set, your environment is fully ready for deployment.**

### 3. Running the script

Once your configuration is complete, follow these steps to start your campaign:

- *Launch agrimass_azure.py:* Run the Python script from your terminal.

- *Authentication*: A browser window will automatically open. Log in with your Microsoft/Google account to authorize the session.

- *Select Recipients*: Choose the .txt file containing your recipient list (one email per line).

- *Email Subject*: Enter your desired subject line directly into the terminal.

- *Insert Email Body*: Paste your previously copied HTML code into the prompt.

- *Send Command*: After pasting the HTML, press Enter, type END on a new line, and press Enter again to confirm.

- *Delivery*: The script will begin sending emails automatically, with a 3-second delay between each message to ensure stability and avoid spam filters.

---

## E-mail design (BeeFree)

*This section provides an optional but very good workflow to easily create professional HTML email templates.*

To design your custom email:

1. *Access the Platform "BeeFree"* as mentioned before: Go to **[beefree.io](https://beefree.io/)** and log in to your account.

2. *Design your Template:* Create a new template from scratch or use their drag-and-drop editor to customize it to your liking.

3. *Export the Code:* Click on "Export" and copy the HTML Code of your finished template.

     - *Note: The free tier typically allows up to 6 exports per month.*

4. *Save Locally:* You can paste the copied HTML into a .txt or .html file to store it locally for future use within AgriMass.

***Once you launch AgriMass, when prompted for the email body, simply paste the copied HTML code—and you're all set!***

---

## 📩 Why Use AgriMass?  
✅ **No limitations** – Send as many emails as you need  
✅ **No paid plans** – 100% free and open-source  
✅ **Customizable** – Use your own mail server or Gmail  
✅ **Easy to use** – Just a few simple steps  

🔗 **Contribute & Improve**  
Feel free to contribute, report issues, or suggest improvements! 💡  

---
📌 *Made with ❤️ for a hassle-free email experience.*  
