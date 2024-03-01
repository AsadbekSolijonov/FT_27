from django.contrib import admin
from blog_app.models import Blog, Comment


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_field', 'body_field', 'created_date', 'created_time', 'updated_date', 'updated_time')

    def title_field(self, obj):
        return self.short_text(obj.title)

    def body_field(self, obj):
        return self.short_text(obj.body)

    def short_text(self, text, max_len=10):
        if len(text) > max_len:
            return f"{text[:max_len]}..."
        return text

    def created_date(self, obj):
        return obj.created.strftime('%Y.%m.%d')

    def created_time(self, obj):
        return obj.created.strftime('%H:%M')

    def updated_date(self, obj):
        return obj.created.strftime('%Y.%m.%d')

    def updated_time(self, obj):
        return obj.created.strftime('%H:%M')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'blog', 'message', 'created', 'updated')
