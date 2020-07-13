import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string


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

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakako"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "KAKAO"),
    )

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
    email_verified = models.BooleanField(default=False)
    email_verification_key = models.CharField(max_length=120, blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )

    age = "age"
    dict_test = {age: 44}

    def __str__(self):
        return self.username

    def verify_email(self):
        if self.email_verified is False:
            verification_key = uuid.uuid4().hex[:20]
            self.email_verification_key = verification_key
            html_message = render_to_string(
                "emails/verify_email.html", {"verification_key": verification_key}
            )
            send_mail(
                "Verify airbnb clone account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return

