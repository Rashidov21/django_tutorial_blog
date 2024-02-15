from django.contrib import admin
from .models import Category,Comment,Tag,Post,Rating
# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    
    prepopulated_fields = {"slug":('name',)}




admin.site.register(Comment)



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    
    prepopulated_fields = {"slug":('name',)}

admin.site.register(Post)
admin.site.register(Rating)