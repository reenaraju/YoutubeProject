import csv
import smtplib
from email.message import EmailMessage
from pytube import YouTube


class YoutubeVideoDownload:

    def VideoDownload(self):
        with open("users.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for name, id, yl in reader:
                try:
                    links = yl
                    YouTube(links).streams.first().download(r'F:\Project2\YoutubeProject\videos')
                    print("Video downloaded!!")
                    x = True
                    YoutubeVideoDownload.SendMail(name, id, x)
                except Exception:
                    print("Video not downloaded!!")
                    x = False
                    YoutubeVideoDownload.SendMail(name, id, x)

    def SendMail(name, id, x):
        email_from = "********"
        email_password = "******"
        email_subject = "Youtube video download"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_from, email_password)
        email_msg1 = "Hello " + name + "\n\nVideo is downloaded successfully\n\n\nRegards\nYoutube Team"
        email_msg2 = "Hello " + name + "\n\nVideo is not downloaded successfully\n\n\nRegards\nYoutube Team"
        email = EmailMessage()
        email['From'] = email_from
        email['To'] = id
        email['Subject'] = email_subject
        if (x):
            email.set_content(email_msg1)
            server.send_message(email)
        else:
            email.set_content(email_msg2)
            server.send_message(email)

        print(f'Email sent to {name}')
        server.close()


a = YoutubeVideoDownload()
a.VideoDownload()
