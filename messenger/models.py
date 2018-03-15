from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    date_sent = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=250, blank=True)
    body = models.TextField(blank=True)
    addressee = models.ForeignKey(User, null=True,
                                  on_delete=models.SET_NULL, related_name="my_messages")
    sender = models.ForeignKey(User, null=True,
                               on_delete=models.SET_NULL, related_name="sent_messages")
    read_mark = models.BooleanField(default=False)

    @property
    def __str__(self):
        return "From: {} / To: {} / Subj: {}".format(self.sender.username,
                                                     self.addressee.username,
                                                     self.subject)