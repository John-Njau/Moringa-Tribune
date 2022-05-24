from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    
   
    
    class Meta:
        verbose_name_plural = 'Editors'
        ordering = ('first_name',)
        
    def __str__(self):
            return self.first_name
    
    def save_editor(self):
        self.save()
            
class tags(models.Model):
    name  = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'tags'
    
# one to many relationship
class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(tags)
    
    def save_article(self):
        self.save()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Articles'
    
# many to many relationships
