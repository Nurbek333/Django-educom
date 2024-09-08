from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/teachers/')
    job_title = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    bio = models.TextField()
    facebook = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    google_plus = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/events/')
    date = models.DateField()

    def __str__(self):
        return self.title
    

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    thumbnail = models.ImageField(upload_to='courses/thumbnails/')


    def __str__(self):
        return self.title


class Notice(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    additional_content = models.TextField(blank=True, null=True)  # Add this field for extra content
    url = models.URLField(max_length=200, blank=True, null=True)  # Optional download link

    def __str__(self):
        return self.title

    def formatted_date(self):
        return self.date.strftime('%d %b, %Y')
    

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    author = models.CharField(max_length=255)
    excerpt = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    read_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.first_name
    

class FunFact(models.Model):
    title = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

class About(models.Model):
    image = models.ImageField(upload_to='about_images/')
    content = models.TextField()

    def __str__(self):
        return f"About Section - {self.id}"
    

class SuccessStory(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    content = models.TextField()

    def __str__(self):
        return self.title