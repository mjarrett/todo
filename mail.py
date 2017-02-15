from todo.models import Project, Task, Tag
from django.contrib.auth.models import User, Group

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from subprocess import Popen, PIPE



def send_mail(mailto,subject,body,html):

    msg = MIMEMultipart('alternative')

    msg["From"] = "todo@mikejarrett.ca"
    msg["To"] = mailto
    msg["Subject"] = subject

    part1 = MIMEText(body, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    p = Popen(["/usr/bin/sendmail", "-t"], stdin=PIPE)
    p.communicate(msg.as_string())

def generate_daily_email(user):

    body = ''
    html = ''

    for group in sorted(user.groups.all(), key=lambda x: len(x.projects.all()),reverse=True):

        if len(group.projects.all()) > 0:

            for project in group.projects.all():
                html = "{}<br> <h2 style='color:green;'>{}</h2><ul>".format(html,project)
                body = "{}\n Tasks for {}:\n\n".format(body,project)

                for task in project.tasks.filter(iscomplete=False):
                    html = "{}  <li><h3>{}</h3><br>{}</li>".format(html,task,task.description)
                    body = "{}  - {}\n{}".format(body,task,task.description)


                html = "{} </ul>".format(html)


    return body, html
