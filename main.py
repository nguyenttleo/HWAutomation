import imaplib
import base64
import os
import email
import seleniumFuncs as submit
import time

while True:
    email_user = 'YOUR-GMAIL-ADDRESS'
    email_pass = 'YOUR-PASSWORD'

    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)

    mail.login(email_user, email_pass)

    mail.select('"[Gmail]/Sent Mail"')

    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()

    assignRead = open("assignmentname.txt", "r")
    lastAssignment = assignRead.read()
    oldassignRead = open("oldAssignments.txt", "r")
    oldAssignOpen = oldassignRead.read()
    oldAssignments = oldAssignOpen.split("\n")
    oldList = []
    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)' )
        raw_email = data[0][1]
    # converts byte literal to string removing b''
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        # if "Calculus BC" in email_message:
        # downloading attachments
        for part in email_message.walk():
            # this part comes from the snipped I don't understand yet...
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()
            if bool(fileName):
                subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
                aName = subject.split(" Message-Id: ")
                aName0 = aName[0]
                aName2 = aName0.split("\n")
                aName1 = aName2[0]
                if aName1 not in oldList:
                    oldList.append(aName1)
                filePath = os.path.join('PATH-TO-HWImages', aName1 + ".pdf")
                if not os.path.isfile(filePath) :
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
                    downloaded = True
                    r = open("assignmentname.txt", "w")
                    r.write(aName1)
                    r.close()
                    print('Downloaded "{file}" from email titled "{subject}" is "{confirmation}".'.format(file=fileName,
                                                                                                          subject=subject,
                                                                                                          confirmation=downloaded))
                else:
                    downloaded = False
                    print("Download status is: {confirmation}".format(confirmation=downloaded))

    print(oldList)
    assignRead = open("assignmentname.txt", "r")
    latestAssignment = assignRead.read()
    print("Latest Assignment: " + latestAssignment)
    # print("Old Assignments: " + assignment for assignment in oldAssignments)
    print("Old Assignments: ")
    for assignment in oldAssignments:
        print(assignment)
    if latestAssignment not in oldAssignments:
        submit.submitHW()
    appendOld = open("oldAssignments.txt", "a+")
    for item in oldList:
        if item not in oldAssignments:
            appendOld.write(item + "\n")
    appendOld.close()
    time.sleep(5)
