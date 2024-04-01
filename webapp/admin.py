from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(contactform)

class testimonialAdmin(admin.ModelAdmin):
  list_display = ['name' , 'profession' , 'image' , 'feedback']
admin.site.register(testimonial,testimonialAdmin)

class servicesAdmin(admin.ModelAdmin):
  list_display = ['name' , 'profession' , 'image' , 'feedback']
admin.site.register(services,servicesAdmin)

class teamAdmin(admin.ModelAdmin):
  list_display = ['name' , 'designation' , 'image']
admin.site.register(team,teamAdmin)

class roomtestiAdmin(admin.ModelAdmin):
  list_display = ['name' , 'profession' , 'description' , 'image']
admin.site.register(roomtesti,roomtestiAdmin)

class roomtypeAdmin(admin.ModelAdmin):
  list_display = ['image' , 'type' , 'price' , 'beds' , 'bath' , 'wifi' , 'description']
admin.site.register(roomtype,roomtypeAdmin)

class abouttestiAdmin(admin.ModelAdmin):
  list_display = ['image' , 'name' , 'designation']
admin.site.register(abouttesti,abouttestiAdmin)

class bookingtableAdmin(admin.ModelAdmin):
  list_display =  ['name' , 'email' , 'date' , 'people' ,'timeslot', 'roomno', 'message']
admin.site.register(bookingtable,bookingtableAdmin)

class bookingdetailformAdmin(admin.ModelAdmin):
  list_display =  ['name' , 'email' , 'checkin' , 'checkout' , 'adultnum' , 'childnum' , 'roomnum' , 'request']
admin.site.register(bookingdetailform,bookingdetailformAdmin)


admin.site.register(UserProfile)

class cabdetailformAdmin(admin.ModelAdmin):
  list_display =  ['name' , 'date' , 'number' , 'airport','time']
admin.site.register(cabdetailform,cabdetailformAdmin)

class eventdetailformAdmin(admin.ModelAdmin):
  list_display =  ['name' , 'date' , 'people' , 'request', 'email']
admin.site.register(eventdetailform,eventdetailformAdmin)

class RegisterAdmin(admin.ModelAdmin):
  list_display = ['fname' , 'lname' , 'username' , 'email' , 'password1' , 'password2']
admin.site.register(Register,RegisterAdmin)