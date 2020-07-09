from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.AbstractTimeStamped):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Ojbect Definition"""

    pass


class Amenity(AbstractItem):

    """Amenity Ojbect Definition"""

    class Meta:
        verbose_name_plural = "Amenities"

    pass


class Facility(AbstractItem):

    """Facility Ojbect Definition"""

    class Meta:
        verbose_name_plural = "Facilities"

    pass


class Rule(AbstractItem):

    """Rule Ojbect Definition"""

    class Meta:
        verbose_name = "House Rule"

    pass


class Photo(core_models.AbstractTimeStamped):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    photo_file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.AbstractTimeStamped):

    """ Room Model Definition """

    name = models.CharField(max_length=140, default="")
    description = models.TextField(null=False)
    country = CountryField()
    city = models.CharField(max_length=80, default="")
    price = models.IntegerField(default=0)
    address = models.CharField(max_length=140, default="")
    guests = models.IntegerField(default=0)
    beds = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE, null=True
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facility = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    rule = models.ManyToManyField("Rule", related_name="rooms", blank=True)

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_rating = 0
        if len(all_reviews) != 0:
            for review in all_reviews:
                all_rating += review.rating_avg()
            return round(all_rating / len(all_reviews), 2)
        else:
            return 0

    total_rating.short_description = "RATING"
