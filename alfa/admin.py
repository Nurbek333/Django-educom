from django.contrib import admin
from .models import Teacher,Event,Course,Notice,BlogPost,Comment,Contact,FunFact,About,SuccessStory

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'subject')
    search_fields = ('name', 'job_title', 'subject')
    fields = ['name', 'image', 'job_title', 'subject', 'bio', 'facebook', 'twitter', 'google_plus', 'linkedin']

admin.site.register(Teacher, TeacherAdmin)

# admin
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)

admin.site.register(Event, EventAdmin)


admin.site.register(Course)


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')

admin.site.register(Notice, NoticeAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    search_fields = ('title', 'author', 'content')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at')
    search_fields = ('name', 'text')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["first_name", "email"]


@admin.register(FunFact)
class FunFactAdmin(admin.ModelAdmin):
    list_display = ('title', 'count', 'description')


admin.site.register(About)

@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url')
    search_fields = ('title',)

