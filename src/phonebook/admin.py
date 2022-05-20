from django.contrib import admin

# Register your models here.

from .models import Persone, Phone

admin.site.register(Persone)
admin.site.register(Phone)