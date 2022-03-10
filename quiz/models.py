from turtle import title
from django.db import models
from django.forms import IntegerField
from idna import intranges_contain

class Category(models.Model):
    name =models.CharField(max_length=300)
    
    
    def __str__(self):
        return self.name
    
class Quizzes(models.Model):
    class Meta:
        verbose_name=("Quiz")
        verbose_name_plural=('quizzes')
        ordering=['id']
    title=models.CharField(max_length=300,default=("New Quiz"), verbose_name=("Quiz Title"))
    category= models.ForeignKey(
        Category, default=0, on_delete=models.DO_NOTHING)
    data_created=models.DateTimeField(auto_now_add=True)    
    
    
    def __str__(self):
        return self.title
    
class Updated(models.Model):
    date_updated=models.DateTimeField(
        verbose_name=('Last Updated'), auto_now=True)
    class Meta:
        abstract=True
       
      
    
    
class Question(Updated):
    class Meta:
        verbose_name=(" Question")
        verbose_name_plural=(' Questions')
        ordering=['id']
    SCALE= (
         (0, ('Fundamental')),
         (1, ('Beginner')),
         (2, ('Intermediate')),
         (3, ('Advanced')),
         (4, ('Expert')),
       
     )
    TYPE=(
        (0, ('Multiple Choice')),
    )
    
    quiz= models.ForeignKey(
        Quizzes ,related_name='question', on_delete=models.DO_NOTHING)
    tecnique= models.IntegerField(
        choices=TYPE, default=0, verbose_name=('Type of Question'))
    title=models.CharField(max_length=300, verbose_name=('Title'))
    difficulty= models.IntegerField(
        choices=SCALE, default=0, verbose_name=('Difficulty'))
    date_create= models.DateTimeField( auto_now_add=True,verbose_name=('Date Created')) 
    is_active=models.BooleanField(
    default=False,verbose_name=('Activate Status'))
    
    
     
    def __str__(self):
        return self.title
class Answer(Updated):
    class Meta:
        verbose_name=("Answer")
        verbose_name_plural=('Answers')
        ordering=['id']
    
    Question= models.ForeignKey(
        Question ,related_name='answer', on_delete=models.DO_NOTHING)    
    answer_text=models.CharField(
        max_length=300, verbose_name=('Answer Text'))
    is_right=models.BooleanField(default=False)
    
    
    
    

    