from django.contrib import admin

from . import models


admin.site.register(models.Player)
admin.site.register(models.Position)
admin.site.register(models.Team)
