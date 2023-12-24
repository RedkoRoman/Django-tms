from django.contrib import admin

from info.models import InfoBlog

# admin.site.register(InfoBlog)


# Register your models here.

@admin.register(InfoBlog)
class InfoBlogAdmin(admin.ModelAdmin):
    # pass
    list_display = ('name', 'id', 'rating', 'price', 'is_deleted')
    search_fields = ('name', 'rating')
    list_filter = ('is_deleted', )
    sortable_by = ('rating', 'price')