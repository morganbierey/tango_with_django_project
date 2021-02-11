from django.contrib import admin
from rango.models import Category, Page

#second from.. added in ex5.6
# Register your models here.

#class below created chapter 5 ex5

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')

#class added 6.3
# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}



#below changed chapter 5 ex , added PageAdmin
admin.site.register(Page,PageAdmin)

# Update the registration to include this customised interface ex6.3
admin.site.register(Category, CategoryAdmin)

