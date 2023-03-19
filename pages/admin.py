from django.contrib import admin
from django.utils.html import format_html
from .models import Teams


@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html("<img src={} width='60' style='border-radius:50%' />".format(object.photo.url))
    
    thumbnail.short_description = "Team picture"
    
    list_display = ("id", "thumbnail", "first_name", "last_name", "designation", "facebook_link", "created_date",)
    list_display_links = ("id", "thumbnail", "first_name", "last_name",)
    search_fields = ("first_name", "last_name", "designation",)
    list_filter = ("designation",)