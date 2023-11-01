from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio=models.TextField()
    location=models.CharField(max_length=200)

class Question(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    details = models.TextField()
    tags = models.TextField()
    posted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='answer_user')
    details = models.TextField()
    posted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.details
    
class Comments(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='comment_user')
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    posted_time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

class UpVotes(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='upvotes_user')
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)

class DownVotes(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='downvotes_user')
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)


    