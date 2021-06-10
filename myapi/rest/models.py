from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
from rest_framework.exceptions import ValidationError
from django .contrib.auth.models import User
from django.db.models import Q


class Friend(models.Model):

    user1 = models.ForeignKey(User, models.CASCADE, related_name="friends")
    user2 = models.ForeignKey(User, models.CASCADE, related_name="_unused_friend_relation")

    class Meta:
        unique_together = ("user1", "user2")
        verbose_name = "Friendship"
        verbose_name_plural = "Friendships"

    def save(self, *args, **kwargs):

        # If entry already exists but in opposite order, throw an exception
        if Friend.objects.filter(Q(user1=self.user2) & Q(user2=self.user1)).exists():
            raise ValidationError("Entry already exists")

        if self.user1 == self.user2:
            raise ValidationError("Users cannot be friends with themselves.")

        super(Friend, self).save(*args, **kwargs)

    def __str__(self):
        string = self.user1.get_username() + ' : ' + self.user2.get_username()
        return string



