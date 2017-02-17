from django.core.management.base import BaseCommand, CommandError
from todo.models import Project, Task, Tag
from django.contrib.auth.models import User, Group
from todo.mail import *
import datetime

class Command(BaseCommand):
    help = "Sends daily todo email"

    def handle(self, *args, **options):

        user = User.objects.get(username='mike')
        body, html = generate_daily_email(user)
        try:


            send_mail(user.email,'Your Tasks For {}'.format(datetime.date.today().strftime("%B %d, %Y")),body,html)
            self.stdout.write("task email sent successfully")
        except:
            self.stdout.write("task email failed")
