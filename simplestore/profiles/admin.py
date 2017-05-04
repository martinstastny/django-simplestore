from django.contrib import admin
from .models import Profile

class ProfilesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':("name",)}

admin.site.register(Profile,ProfilesAdmin)