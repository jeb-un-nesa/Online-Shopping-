from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('Mobile_no', 'user_type',)}),
    )

admin.site.register(CustomUser, MyUserAdmin)
