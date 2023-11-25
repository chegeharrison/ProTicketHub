from django.contrib import admin
from .models import EventDb
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.
admin.site.register(EventDb)


# from django.contrib import admin
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields
#
# class RentalAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
#     }