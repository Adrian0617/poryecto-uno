from django.contrib import admin
from .models import Blog

# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')


admin.site.register(Blog)
