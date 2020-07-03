from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definitions """

    list_display = (
        "room",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )

    pass
