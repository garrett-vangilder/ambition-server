from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from players.views import ListTeamsName

router = routers.DefaultRouter()
router.register(r'teams', ListTeamsName)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
