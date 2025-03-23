import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Dati di accesso
sender_email = str(input("Inserisci la tua email: "))

password = str(input("Inserisci la tua password: "))

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

# Connessione al server SMTP del tuo dominio
try:
    server = smtplib.SMTP('YOUR-SMTP-SERVER', 587)  # Modifica con il server SMTP giusto
    server.starttls()  # Avvia la connessione sicura
    server.login('SERVER-USER', 'PASSWORD')  # Nome utente e password per SMTP
    print("Connessione riuscita!")

    for mail in receiver_email:
        print(f"Invio in corso a {mail}")

        # Creazione del messaggio
        msg = MIMEMultipart()
        msg['From'] = sender_email  # Il tuo indirizzo di email
        msg['To'] = mail
        msg['Subject'] = subject

        # Aggiungi il corpo dell'email
        msg.attach(MIMEText(html_content, 'html'))

        # Invia l'email
        server.sendmail(sender_email, mail, msg.as_string())
        print(f"Email inviata con successo a {mail}!")

        # Pausa tra l'invio di un'email e l'altra
        time.sleep(4)

except smtplib.SMTPException as e:
    print(f"Errore SMTP: {e}")

finally:
    # Chiudi la connessione al server SMTP
    server.quit()
