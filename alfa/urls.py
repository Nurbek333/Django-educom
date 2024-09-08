from django.urls import path
from .views import index,about,blog_single,blog,ContactView,course_single,courses,events,notice_single,notice,teacher_single
from . import views


urlpatterns = [
    path('',index, name="index-page"),
    path('about/',about, name="about-page"),
    path('blog_single/',blog_single, name="blog_single-page"),
    path('blog/',blog, name="blog-page"),
    path("contact/",ContactView.as_view(),name="contact-page"),
    path('course_single/',course_single, name="course_single-page"),
    path('courses/',courses, name="courses-page"),
    path('events/',events, name="events-page"),
    path('notice_single/',notice_single, name="notice_single-page"),
    path('notice/',notice, name="notice-page"),
    path('teacher_single/',teacher_single, name="teacher_single-page"),
]