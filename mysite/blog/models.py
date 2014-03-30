from django.db import models
from django.utils import timezone
from django.contrib import admin
from packages.generic import gmodels
from packages.generic.gmodels import content_file_name,content_file_name_same
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings as stg
import os
import Image as PImage


from embed_video.fields import EmbedVideoField


# Create your models here.
class Conference(models.Model):
    title = models.CharField(max_length=160)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=160)
    position = models.PositiveIntegerField(default='0')
    
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        model = self.__class__
        
        if self.position is None:
            # Append
            try:
                last = model.objects.order_by('-position')[0]
                self.position = last.position + 1
            except IndexError:
                # First row
                self.position = 0
        
        return super(Category, self).save(*args, **kwargs)


class Code(models.Model):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to=content_file_name_same,blank=True)
    git_link = models.URLField(blank=True)
    programming_language = models.CharField(max_length=40)
    details = models.TextField(max_length=600,blank=True)
    
    def __str__(self):
        return str(self.title)
    

class Publication(models.Model):
    title = models.CharField(max_length=160)
    authors = models.CharField(max_length=220,null=True)
    link = models.URLField(null=True, blank=True)
    file = models.FileField(upload_to=content_file_name_same, null=True, blank=True)
    short = models.CharField(max_length=50,null=True)
    bibtex = models.TextField(max_length=1000)
    conference_id = models.ForeignKey(Conference)
    year = models.PositiveIntegerField(default=datetime.now().year,
        validators=[
            MaxValueValidator(datetime.now().year + 2),
            MinValueValidator(1800)
        ])
    
  #  def __init__(self, *args, **kwargs):
        
#        super(Publication, self).__init__(*args, **kwargs)
#        if int(self.conference_id.i) != 0:
 #           self.conference =  Conference.objects.get(id=int(self.conference_id))
    
    def __str__(self):
        return self.title
    
    def fullStr(self):
        return "%s, \"%s\", %s, %s " % (self.authors, self.title, self.conference_id.title, self.year) 
   

    
class Project(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    mtext = models.TextField(max_length=1000,blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    category_id = models.ForeignKey(Category)
    position = models.PositiveIntegerField(default='0') 
    publications = models.ManyToManyField(Publication, null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        model = self.__class__
        
        if self.position is None:
            # Append
            try:
                last = model.objects.order_by('-position')[0]
                self.position = last.position + 1
            except IndexError:
                # First row
                self.position = 0
        
        return super(Project, self).save(*args, **kwargs)
    
    def get_images(self):
        return [y for y in ProjectImage.objects.filter(entity_id_id__exact=self.id)]
    
    def getFirstImage(self):
        try:
            p = ProjectImage.objects.filter(entity_id_id__exact=self.id)[0]
        except IndexError:
            p = None
            
        if None != p:
            return p
        else:
            return "default.png"
 
    def get_videos(self):
        return [str(y) for y in ProjectVideo.objects.filter(entity_id_id__exact=self.id)]
 
    def get_publications(self):
        return [p for p in self.publications.all()]
 
    class Meta:
        ordering = ('position',)

    def __str__(self):
        return self.title
    
    
    

class ProjectImage(gmodels.GImage):
    entity_id = models.ForeignKey(Project)
    
    



class ProjectVideo(models.Model):
    entity_id = models.ForeignKey(Project)
    
    link = EmbedVideoField(null=True)  # same like models.URLField()
    
    def __str__(self):
        return str(self.link)
    
    
    
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    readonly_fields = ('image_tag',)


    
class ProjectVideoInline(admin.TabularInline):
    model = ProjectVideo
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline, ProjectVideoInline, ]
    
    class Media:
        js = ('admin/js/listreorder.js',)
    
    list_display = ('position',)
    list_display_links = ('title',)
    list_display = ('title', 'position',)
    list_editable = ('position',)

 
    
    

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    date_created = models.DateTimeField(default=timezone.now)
    category_id = models.ForeignKey(Category)
    position = models.PositiveIntegerField(default='0') 

    def save(self, *args, **kwargs):
        model = self.__class__
        
        if self.position is None:
            # Append
            try:
                last = model.objects.order_by('-position')[0]
                self.position = last.position + 1
            except IndexError:
                # First row
                self.position = 0
        
        return super(Article, self).save(*args, **kwargs)
    
    def get_images(self):
        return [y for y in ArticleImage.objects.filter(entity_id_id__exact=self.id)]
    

    def getFirstImage(self):
        try:
            p = ArticleImage.objects.filter(entity_id_id__exact=self.id)[0]
        except IndexError:
            p = None
            
        if None != p:
            return p
        else:
            return "default.png"
 
 
    class Meta:
        ordering = ('position',)

    def __str__(self):
        return self.title    
    

class ArticleImage(gmodels.GImage):
    entity_id = models.ForeignKey(Article)




class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1
    readonly_fields = ('image_tag',)



class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageInline, ]
    
    class Media:
        js = ('admin/js/listreorder.js',)
    
    list_display = ('position',)
    list_display_links = ('title',)
    list_display = ('title', 'position',)
    list_editable = ('position',)


class CodeSnippet(models.Model):
    title = models.CharField(max_length=160)
    programming_language = models.CharField(max_length=120)
    text = models.TextField(max_length=500)
    code = models.TextField(max_length=1000)
    
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    
    

   




