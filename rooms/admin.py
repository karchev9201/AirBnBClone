from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.Rule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definitions """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definitions """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")},),
        (
            "More About the Space",
            {"classes": ("collapse",), "fields": ("amenities", "facility", "rule")},
        ),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths"),},),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("price",)

    list_filter = (
        "instant_book",
        "host__superhost",
        "city",
        "room_type",
        "amenities",
        "facility",
        "rule",
        "country",
    )

    raw_id_fields = ("host",)

    search_fields = ["=city", "^host__username"]

    filter_horizontal = (
        "amenities",
        "facility",
        "rule",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definitions """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        print(dir(obj.photo_file))
        return mark_safe(f'<img width="50px" src="{obj.photo_file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
