from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display=('title','author','date_created')
# this helps in give a detailed view of admin site contents to be projected in admin site




admin.site.register(Post,PostAdmin)
admin.site.register(Comment)


# Register your models here.
