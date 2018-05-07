from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from players.views import ListTeamsName, ListPositionsName, ListSalariesByTeam, ListSalariesByPosition

router = routers.DefaultRouter()
router.register(r'salary',
                ListSalariesByTeam, 'salary_by_team')
router.register(r'teams', ListTeamsName)
router.register(r'positions', ListPositionsName)
router.register(r'positions/salary', ListSalariesByPosition)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
