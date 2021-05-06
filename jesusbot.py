import smtplib

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.connect('smtp.gmail.com', 587)

sender = 'JChrist21thehillorg@gmail.com'
password = 'ThisIsAHuman1'
receiverlist = ['PStone21@thehill.org']


mail.starttls()
mail.login(sender, password)


message = f"""From: deansofficedemerit@thehill.org <deansofficedemerit@thehill.org>
To: {receiverlist}
Subject: Demerit Notice

Dear QTang21,

This is your notice of an infraction.  Please sign into your MyBackpack account for the details.

If this is an error, please print the first page of the infraction.  Have the person who reported you sign it and bring it to the Deans Office within 48 hours. 

Sincerely,

Deans Office


"""
amoutOfEmails = int(input("how many emails you bitch boi: "))

for i in range(0, amoutOfEmails, 1):
    mail.sendmail(sender, receiverlist, message)         
    print(f"[{i + 1}] out of [{amoutOfEmails}] sent")
print("Finsihed you fuck")

mail.quit()