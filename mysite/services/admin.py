from django.contrib import admin

from services.models import Service

class service_admin(admin.ModelAdmin):
    list_display=('service_icon', 'service_title', 'service_des')



admin.site.register(Service , service_admin)

# Register your models here.
