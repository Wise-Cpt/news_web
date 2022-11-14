from django.db import models
# from tinymce import models as tinymce_models



# Create your models here.

class Image(models.Model):
    title               = models.CharField(max_length=254,verbose_name="Titre de l'image'")

    def __str__(self):
        return self.title

class Article(models.Model):
    title               = models.CharField(max_length=254, verbose_name="Titre de l'article")
    # description         = tinymce_models.HTMLField(verbose_name='Description', blank=True, null=True)
    description         = models.TextField(verbose_name='Description', blank=True, null=True)
    image               = models.ForeignKey(Image,on_delete=models.CASCADE, verbose_name="L'image de l'article", related_name="image_of_article")

    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name                = models.CharField(max_length=254, verbose_name="Nom de la categorie")
    parent              = models.ForeignKey("self",on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

