from django.contrib import admin

# Register your models here.
from  .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'category', 'author', 'publish',
                    'status')
    list_filter   = ('status', 'category', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields       = ('author',)
    date_hierarchy      = 'publish'
    list_per_page       = 10
    list_editable       = ('status',) 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug','publish']
    prepopulated_fields = {'slug': ('name',)}