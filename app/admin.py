from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
  list_display = ['id','first_name','nid']
@admin.register(Bikepost)
class BikePostAdmin(admin.ModelAdmin):
  list_display=['id','post_user','bike_name']
@admin.register(Rentbike)
class RentBikeAdmin(admin.ModelAdmin):
  list_display=['id','rent_user','post_user','pick_up_location','pick_up_date','pick_up_time']