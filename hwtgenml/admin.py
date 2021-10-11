from django.contrib import admin
from hwtgenml.models import *

# Register your models here.
admin.site.register(Vendor)
admin.site.register(VendorCollection)


class CaptionImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'recognized_text', 'saved_text', 'confidence_level']


class CollectionTextAdmin(admin.ModelAdmin):
    list_display = ['image', 'initial_text']


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['estimated_time', 'create_time', 'update_time']


admin.site.register(BoostrapModel)
admin.site.register(TestCaption)
admin.site.register(TestCaptionImage)
admin.site.register(CaptionImage, CaptionImageAdmin)
admin.site.register(Caption)
admin.site.register(UserModel, UserModelAdmin)
admin.site.register(Collection)
admin.site.register(CollectionImage)
admin.site.register(CollectionText, CollectionTextAdmin)
