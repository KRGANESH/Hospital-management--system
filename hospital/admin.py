from django.contrib import admin
from .models import *

admin.site.register(patient_details)
admin.site.register(doctor_details)
admin.site.register(appointment)
admin.site.register(lab_tests)
admin.site.register(lab_technician)
