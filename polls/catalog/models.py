from django.db import models
from django.urls import reverse
import uuid


# Create your models here.


###Book Author Gener BookInstanse Language

class Genre(models.Model):
    name = models.CharField(max_length=200,help_text='Enter a Book gener(science fiction,action)')
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    summary = models.TextField(max_length=1000,help_text='Enter the maximum number of words')
    isbn = models.CharField('ISBN',max_length=15,unique=True,help_text='13 digit numbers Require')
    genre =models.ManyToManyField(Genre,help_text='please select at least one genre')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    pass

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField(blank=True,null=True)
    date_of_death = models.DateTimeField('Died',blank=True,null=True)

    class Meta:
        ordering =['last_name','first_name']

    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name} ,{self.first_name}'




class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text ='Unique Id')
    book = models.ForeignKey('Book',on_delete=models.RESTRICT,null= True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True)
    LOAN_STATUS = (
        ('m', 'maintenance'),
        ('o', 'on loan'),
        ('a', 'available'),
        ('m', 'reserved'),
    )
    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m',help_text='Book status')

    class Meta:
        ordering =['due_back']

    def __str__(self):
        return f' {self.id}{self.book}'



    pass

class Language(models.Model):
    pass

