from django.db import models

from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    """ Messages of our chan """

    class Meta:
        verbose_name = u"Сообщение"
        verbose_name_plural = u"Сообщения"
        db_table = "msgs"

    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    reply_to = models.ForeignKey("Message", null=True, on_delete=models.CASCADE, )  # (self)

    def __str__(self):
        return self.text
