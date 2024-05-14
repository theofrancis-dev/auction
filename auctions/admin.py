from django.contrib import admin

# Register your models here.
from .models import Category, SubCategory, Auction, Comment, WatchList, Avatar
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Auction)
admin.site.register(Comment)
admin.site.register(WatchList)

class AvatarAdmin (admin.ModelAdmin):
    list_display = ( 'url', 'tag', 'user')

admin.site.register(Avatar)




