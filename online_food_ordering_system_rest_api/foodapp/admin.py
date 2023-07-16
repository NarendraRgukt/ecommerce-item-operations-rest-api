from django.contrib import admin
from foodapp import models
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

class UserModel(admin.ModelAdmin):
    list_display=('name','email','is_active','is_staff')
    
admin.site.register(get_user_model(),UserModel)
admin.site.register(models.Item)

