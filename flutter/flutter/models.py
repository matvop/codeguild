from django.db import models


class Flutt(models.Model):
    user_name = models.CharField(
        max_length=32,
        blank=False,
        default='Anonymous'
    )
    comment = models.CharField(
        max_length=400,
        blank=False
    )
    datetime = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )
    ordering_fields = ('datetime', 'user_name')

    def __str__(self):
        return '{} {} {}'.format(
            self.datetime,
            self.user_name,
            self.comment,
        )

    def __repr__(self):
        return 'user={!r} datetime={!r} comment={!r}'.format(
            self.user_name,
            self.datetime,
            self.comment,
        )

    class Meta:
        ordering = ('-datetime',)
