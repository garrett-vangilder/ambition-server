
from django.conf.urls import url
from .views import ListTeamsName


urlpatterns = [
    url('', ListTeamsName),
]
