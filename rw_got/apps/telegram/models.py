from django.db import models


class User(models.Model):
    external_id = models.IntegerField(db_index=True, unique=True,)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, blank=True)
    is_bot = models.BooleanField()
    language_code = models.CharField(max_length=100, blank=True)


class Chat(models.Model):
    external_id = models.IntegerField(db_index=True, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    all_members_are_administrators = models.BooleanField()


class IncomingMessage(models.Model):
    external_id = models.IntegerField()
    text = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(blank=True)


class OutgoingMessage(models.Model):
    external_id = models.IntegerField(db_index=True, unique=True)
    text = models.TextField(blank=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(blank=True, auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.id is None:
            from rw_got.apps.telegram.bot import Bot
            Bot().send_message(self)
        super(OutgoingMessage, self).save(*args, **kwargs)
