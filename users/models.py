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

    avatar = models.ImageField(blank=True)
    gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICES)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, default="en", blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, default="usd", blank=True
    )
    superhost = models.BooleanField(default=False)
