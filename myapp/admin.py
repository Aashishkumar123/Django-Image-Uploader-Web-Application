from django.contrib import admin
from .models import ImageUploader,Profile
# Register your models here.

@admin.register(ImageUploader)
class AdminImageUploader(admin.ModelAdmin):
        list_display = ['id','image_name','image','user','user_profile','date']

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
        list_display = ['id','user','image']
        list_editable = ('user',)
        list_filter = ['user']
        search_fields = ['user','image']
