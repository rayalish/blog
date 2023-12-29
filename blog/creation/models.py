from django.db import models
import uuid
from authe.models import User



def uniq_name_upload(instance, filename):
    new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
    return f'avatars/{new_file_name}'

class Category(models.Model):
    name = models.CharField(max_length=100, null = False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    


    
class Blog(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to=uniq_name_upload)
    publish_date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    

    def __str__(self):
        return self.title
    
    def to_json(self):
        return {
            'image': self.image,
            'publish_date': self.publish_date,
            'title': self.title,
            'description': self.description,
            'author': self.author,
            'category': self.category,
        }
    
class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Blog, on_delete=models.CASCADE)