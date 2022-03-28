from django.contrib import admin

from appbmi.models import BmiUser
from appbmi.models import UserDiet
from appbmi.models import UserBmi

# we should create class that is referenced to app model to link all the attributes of models to admin
class BmiUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name','last_name', 'username', 'user_email')
    list_filter = ('first_name',)

# Register your models here.
admin.site.register(BmiUser, BmiUserAdmin)
admin.site.register(UserDiet)
admin.site.register(UserBmi)

# customizing admin panel titles
admin.site.site_header = "Django BMI" # site brand or header
admin.site.site_title = "Django BMI 2022" # title
admin.site.index_title = "Admin Dashboard"

