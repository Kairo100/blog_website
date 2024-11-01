from django.contrib import admin

from . models import Category,Blogs

#in admin dashbord to display models/ database whole table
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name', 'created_at', 'updated_at')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','blog_image','status','is_feacherd','created_at', 'updated_at')
    #title ka ayuu ku xidhan yhy si loogo tagi karo page to page
    prepopulated_fields ={ 'slug':('title',)}
    #searching feild    
    search_fields =('id','title','category__category_name','status')
    list_editable = ('is_feacherd',)

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blogs,BlogAdmin)