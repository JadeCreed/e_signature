from django.contrib import admin
from .models import User, Planting, Harvesting
# Register your models here.

admin.site.register(User)
admin.site.register(Planting)
admin.site.register(Harvesting)