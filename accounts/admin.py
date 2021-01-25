from django.contrib import admin
from .models import UserAccount, Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'first_name', 'last_name', 'is_active', 'is_author')
    list_display_links = ('id', 'email',)
    search_fields = ('name', 'first_name', 'last_name',)
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    fields = ('name', 'email', 'password', 'first_name', 'last_name',)
    readonly_fields = ('is_author',)
    save_on_top = True


admin.site.register(UserAccount)
admin.site.register(Author, AuthorAdmin)