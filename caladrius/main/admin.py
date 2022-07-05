from django.contrib import admin
from .models import ToDoList, Item, Patient, Doctor, Appointments
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointments)
