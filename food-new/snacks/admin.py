from django.contrib import admin
from snacks.models import Food1,Order1,Regis1,payments
from snacks.forms import paymentpg

class FoodAdmin(admin.ModelAdmin):
	list_display=['ssnacks','veg_or_nonveg','description','price','image_url','follow_author','book_available']
class regisorder(admin.ModelAdmin):
	list_display=['sName','eEmail','sphone','sAddress','sCode','sAgree']
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['s_snacks1','s_price1','s_image_url','ccardno1', 'Expires', 'CSC', 'F_name', 'Address1', 'City', 'State1', 'Post_code', 'Mobile_no',]

admin.site.register(Food1, FoodAdmin)
admin.site.register(Order1)
admin.site.register(Regis1, regisorder)
admin.site.register(payments, PaymentsAdmin)

# Register your models here.
