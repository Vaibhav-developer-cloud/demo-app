from django.contrib import admin
from .models import Book,BookInstance,Author,Language,Genre
# Register your models here.

# admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
# admin.site.register(Author)
admin.site.register(Language)


class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name','first_name','date_of_birth','date_of_death')
    list_filter = ('date_of_birth','first_name')
    list_per_page = 10

admin.site.register(Author,AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','summary','isbn')
    list_filter = ('title',)
    list_per_page = 10

admin.site.register(Book,BookAdmin)