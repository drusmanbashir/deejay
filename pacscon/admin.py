from pacscon.models import PatientJpeg, Patient, Jpeg, System, Diagnosis
from django.contrib import admin

class JpegInline(admin.StackedInline):
    model = Jpeg
    extra = 0

class DiagnosisInline (admin.StackedInline):
    model = Diagnosis

class PatientAdmin(admin.ModelAdmin):
    fields = ['pat_id', 'pat_name', 'pat_birthdate', 'description', 'report',
             'diagnosis', 'system']
    list_display = ['id', 'pat_id', ]

class PatientJpegAdmin (admin.ModelAdmin):
    fields = ['pat_sex', 'pat_age', 'description', 'diagnosis', 'system',
              ]
    inlines = [
            JpegInline,
            ]
    list_display = ['id', ]


class JpegAdmin (admin.ModelAdmin):

    fields = ['patient_jpeg_fk', 'image',
              ]
    list_display = ['__unicode__', 'patient_jpeg_fk', 'thumbnail', 'ImSize', ]

admin.site.register(Patient, PatientAdmin)
admin.site.register(Diagnosis)
admin.site.register(System)
admin.site.register(Jpeg, JpegAdmin)
admin.site.register(PatientJpeg, PatientJpegAdmin)
