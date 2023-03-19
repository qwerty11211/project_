from django.contrib import admin
from .models import User, Appointments, Medications


admin.site.register(User)

admin.site.register(Appointments)
admin.site.register(Medications)
