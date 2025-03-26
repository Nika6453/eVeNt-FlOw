from django.contrib import admin

from .models import Category, Public, Private, PrivateCat

admin.site.register(Category)
admin.site.register(Public)
admin.site.register(Private)
admin.site.register(PrivateCat)