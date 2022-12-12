from tkinter.ttk import Style
from django.contrib import admin
from .models import Post
from django.contrib.auth.models import Group
from django.utils.html import format_html


# Register your models here.

class CustomAdminPost(admin.ModelAdmin):
    list_display=('author_name','less_content') #shows column to be listed
    list_filter=('author_name','title')
    search_fields=('author_name',)
    list_per_page=2 #to get record on next page
    list_display_links=('author_name','less_content',)#to get the link 
    save_on_top=True

    def less_content(self,obj):
        # return obj.content[ :10]
        return format_html(f'<span Style="color:red;"> {obj.content[ :10]}</span>')


#to change the heading of admin
admin.site.site_header='Blog admin panel'
admin.site.site_title='custom Admin Panel'



admin.site.register(Post,CustomAdminPost)
#unregister your Model
admin.site.unregister(Group)