from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'classe', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'bio', 'avatar', 'ecole')
    search_fields = ('first_name', 'last_name', 'ecole')


    def nom_complet(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"