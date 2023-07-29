from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Question(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='question_images/', null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    opta=models.CharField(max_length=500,default='')
    optb=models.CharField(max_length=500,default='')
    optc=models.CharField(max_length=500,default='')
    optd=models.CharField(max_length=500,default='')
    ans=models.CharField(max_length=500,default='')


    def __str__(self) -> str:
        return f'{self.text} of {self.section} section'


class Quizlog(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    exam= models.ForeignKey(Exam, on_delete=models.CASCADE)
    section= models.ForeignKey(Section, on_delete=models.CASCADE)
    score=models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.user} scored {self.score} in {self.section} of {self.exam} exam'
