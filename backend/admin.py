from django.contrib import admin
from backend.models import User


# USER ADMIN DISPLAY CODE
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'isMaried')
    list_filter = ('age', 'isMaried')
    search_fields = ('name', 'email')


# USER MODEL CONNECTED
admin.site.register(User, UserAdmin)
