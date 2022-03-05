from django.contrib import admin
from . import models

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','mail','phone','subj','msg','ctime','uptime']
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display=['name', 'mail','phone','course_name','ctime','uptime']
admin.site.register(models.Question)
admin.site.register(models.Response)
admin.site.register(models.Contact,ContactAdmin)
admin.site.register(models.CourseRegistration, CourseRegistrationAdmin)
