from django.contrib import admin

from application.models import ContactMessage, Car

# Register your models here.
admin.site.register(ContactMessage)
admin.site.register(Car)
