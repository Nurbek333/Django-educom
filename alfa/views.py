from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages  # new
from django.urls import reverse  # new
from django.views.generic import View,TemplateView,DetailView,ListView
from .models import Teacher,Event,Course,Notice,BlogPost,Comment,Contact,FunFact,About,SuccessStory
from .bot import send_message
def index(request):
    teachers = Teacher.objects.all()
    events = Event.objects.all()
    courses = Course.objects.all()
    posts = BlogPost.objects.all()
    about_content = About.objects.first()
    stories = SuccessStory.objects.all()
    return render(request, "index.html", {'teachers': teachers, 'events': events, 'courses': courses, 'posts': posts, 'about_content': about_content, 'stories': stories})

def about(request):
    teachers = Teacher.objects.all()
    funfacts = FunFact.objects.all()
    about_content = About.objects.first()
    stories = SuccessStory.objects.all()
    return render(request,"about.html", {'teachers': teachers, 'funfacts': funfacts, 'about_content': about_content, 'stories': stories})

def blog_single(request):
    posts = BlogPost.objects.all()
    comments = Comment.objects.all()
    return render(request,"blog-single.html", {'posts': posts, 'comments': comments})

def blog(request):
    posts = BlogPost.objects.all()
    return render(request,"blog.html", {'posts': posts})

class ContactView(View):
    template_name = "contact.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs): 
        name = request.POST.get('first_name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('description', '')
        contact = Contact(first_name=name,email=email,description=message)
        contact.save()
        
        send_message(f"Ism: {name}\nEmail: {email}\nText:{message}")

        return HttpResponseRedirect(reverse('index-page'))  

def course_single(request):
    courses = Course.objects.all()
    return render(request,"course-single.html", {'courses': courses})

def courses(request):
    courses = Course.objects.all()
    return render(request,"courses.html", {'courses': courses})


def events(request):
    events = Event.objects.all()
    return render(request,"events.html", {'events': events})

def notice_single(request):
    notices = Notice.objects.all()
    return render(request,"notice-single.html",{'notices': notices})

def notice(request):
    notices = Notice.objects.all()
    return render(request,"notice.html",{'notices': notices})


def teacher_single(request):
    teachers = Teacher.objects.all()
    return render(request,"teacher-single.html", {'teachers': teachers})


