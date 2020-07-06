from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):

    """ HomeView Definitions """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"


class RoomDetail(DetailView):

    """ RoomDetail Definitions """

    model = models.Room
