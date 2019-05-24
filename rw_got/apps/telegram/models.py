from django.db import models


class User(models.Model):
    external_id = models.BigIntegerField(db_index=True, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    is_bot = models.BooleanField()
    language_code = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username \
               or str(self.last_name) + ' ' + str(self.first_name)


class Chat(models.Model):
    external_id = models.BigIntegerField(db_index=True, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    all_members_are_administrators = models.NullBooleanField(null=True)

    def __str__(self):
        return self.title \
               or self.username \
               or str(self.last_name) + ' ' + str(self.first_name)


class IncomingMessage(models.Model):
    external_id = models.BigIntegerField()
    text = models.TextField(blank=True, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.text or super(IncomingMessage, self).__str__()


class OutgoingMessage(models.Model):
    text = models.TextField(blank=True, null=True, default=None)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    photo_url = models.URLField(blank=True, default=None, null=True)
    creation_date = models.DateTimeField(blank=True, auto_now_add=True)
    reply_to = models.ForeignKey(IncomingMessage, on_delete=models.CASCADE,
                                 blank=True, default=None, null=True)

    def __str__(self):
        return self.text or self.photo_url

    def save(self, *args, **kwargs):
        if self.id is None:
            from rw_got.apps.telegram.bot import Bot
            Bot().send_message(self)
        super(OutgoingMessage, self).save(*args, **kwargs)
