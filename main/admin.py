from django.contrib import admin
from .models import Product, Tag
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import *


@admin.register(User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('phone_number',  "address",  )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Basket)
admin.site.register(Advantage)
admin.site.register(Favorite_food)
admin.site.register(Branch)
admin.site.register(Vacancy)
admin.site.register(Send_request)
admin.site.register(Job_benefit)
admin.site.register(Career)
admin.site.register(About_job)
admin.site.register(New)
admin.site.register(About_us)
admin.site.register(Resume)
admin.site.register(Image)
admin.site.register(Testimonial)
admin.site.register(Contact)
admin.site.register(Info)

