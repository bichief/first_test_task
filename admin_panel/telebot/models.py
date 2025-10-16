from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CreatedModel(models.Model):
    """Абстрактная модель. Добавляет дату создания."""
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Users(CreatedModel):
    telegram_id = models.BigIntegerField(
        verbose_name='Telegram ID',
        help_text='Telegram ID'
    )

    name = models.CharField(
        max_length=5000,
        null=True,
        verbose_name='Имя',
        help_text='Имя'
    )

    username = models.CharField(
        max_length=5000,
        null=True,
        verbose_name='Юзернейм',
        help_text='Юзернейм'
    )
