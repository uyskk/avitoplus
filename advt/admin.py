from django.contrib import admin

from .models import Advert, Like, Comment


class LikeInline(admin.StackedInline):

    model = Like
    extra = 3


class CommentInline(admin.StackedInline):

    model = Comment
    extra = 3


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['title', 'photo']}),
        ('Детальная информация', {'fields': ['text', 'price', 'address']}),
        ('Дополнительная информация', {'fields': ['create_at', 'update_at', 'is_liked']}),
    ]
    inlines = [LikeInline, CommentInline]
    readonly_fields = ['is_liked', 'create_at', 'update_at']
    list_display = ['title', 'price', 'address']
    search_fields = ['title', 'text']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Детальная информация', {'fields': ['advt', 'user']}),
        ('Дополнительная информация', {'fields': ['create_at', 'update_at']}),
    ]
    readonly_fields = ['create_at', 'update_at']
    list_display = ['create_at', 'update_at']
    search_fields = ['create_at', 'update_at', 'advt__title', 'user__username']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['text']}),
        ('Детальная информация', {'fields': ['advt', 'user']}),
        ('Дополнительная информация', {'fields': ['create_at', 'update_at']}),
    ]
    readonly_fields = ['create_at', 'update_at']
    list_display = ['text', 'create_at', 'update_at']
    search_fields = ['create_at', 'update_at', 'advt__title', 'user__username']
