import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Dati di accesso
sender_email = str(input("Inserisci la tua email di gmail: "))

password = str(input("Inserisci la tua password per le app: "))

subject = str(input("Inserisci l'oggetto della mail: "))

print("Inserisci il testo html e lascia una riga vuota per terminare:")

lines = []
while True:
    line = input()
    if line == "":  # Se l'utente preme solo Invio, termina l'input
        break
    lines.append(line)

html_content = "\n".join(lines)

with open("mailing_list.txt", "r") as file:
    receiver_email = file.read().splitlines()

for mail in receiver_email:
    print(f"Invio in corso a {mail}")

    # Creazione del messaggio
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = mail
    msg['Subject'] = subject

    # Corpo dell'email in formato HTML
    

    # Aggiungi il corpo dell'email
    msg.attach(MIMEText(html_content, 'html'))

    # Connessione al server SMTP (ad esempio Gmail)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Avvia la connessione sicura
    server.login(sender_email, password)

    # Invia l'email
    server.sendmail(sender_email, mail, msg.as_string())

    # Chiudi la connessione al server SMTP
    server.quit()

    print(f"Email inviata con successo a {mail}!")

    time.sleep(4)
