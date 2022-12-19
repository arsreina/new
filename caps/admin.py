from django.contrib import admin
from .models import *
from users.models import AppUser

admin.site.register(Collection)
admin.site.register(Category)
admin.site.register(Cap)
admin.site.register(Brand)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Size)
admin.site.register(AppUser)
