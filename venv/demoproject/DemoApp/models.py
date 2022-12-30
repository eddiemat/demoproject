from django.db import models
import uuid
# Create your models here.

class Project(models.Model):
    title= models.CharField(max_length=200 )
    tags= models.ManyToManyField('Tags')
    description= models.TextField(null=True, blank= True)
    demo_link= models.CharField(max_length=2000, null=True, blank=True)
    source_link=models.CharField(max_length=2000, null=True, blank=True)
    vote_total= models.IntegerField(default=0, blank=True, null=True)
    vote_ratio= models.IntegerField(default=0, blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return self.title



class Review(models.Model):
    VOTE_TYPE= (
        ('up', 'up'),
        ('down', 'down')
    )
    #owner=
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    body =  models.TextField(null=True, blank= True)
    value = models.CharField(max_length=100, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return self.value

class Tags(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
       return self.name

