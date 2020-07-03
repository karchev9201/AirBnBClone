from django.db import models
from django.utils import timezone
from core import models as core_models


class Reservation(core_models.AbstractTimeStamped):

    """ Reservation Model Definitions """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceld"

    STATUS_CHOICES = {
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceld"),
    }

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )

    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in.date() and now < self.check_out.date()

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out.date()

    is_finished.boolean = True
