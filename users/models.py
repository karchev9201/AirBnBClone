from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_JAPANESE = "jp"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_JAPANESE, "Japanese"))

    CURRENCY_USD = "usd"
    CURRENCY_YEN = "yen"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_YEN, "YEN"))

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICES)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_ENGLISH
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_USD
    )
    superhost = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    email_verification_key = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.username

    def verify_email():
        pass
