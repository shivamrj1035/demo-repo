from django.contrib import admin
from .models import Contacts, Tasks, Notes
# Register your models here.
admin.site.register(Contacts)
admin.site.register(Tasks)
admin.site.register(Notes)


